#####################################################################
#
# Name: md5converter.ps1
# Purpose: Converts a local file to an md5 file
# Author: Adam Lentz
# Version 1.0
# Params: 
# 1) Path to the local file to be converted
# NOTES: requires Powershell >=3.0
######################################################################

#check args length
if ($args.Length -ne 1)
{
	Write-Error "Wrong Command Format: md5converter.ps1 <local file path>"
	Exit 1
}

#check powershell version
[int]$MajorVersion = $PSVersionTable.PSVersion.Major
Write-Host Version $MajorVersion

#get file path and name from argument
$filepath = $args[0]
$filename = Split-Path $filepath -leaf

#converter for powershell 3.0 or less
if($MajorVersion -lt 4){
    Write-Host "Old version.  Files greater than 2.0 GB cannot be converted."
    $md5 = New-Object -TypeName System.Security.Cryptography.MD5CryptoServiceProvider
    $hash = [System.BitConverter]::ToString($md5.ComputeHash([System.IO.File]::ReadAllBytes($filepath)))
    Write-Host $hash
    $hash | Out-File  ($filename+".md5")
}

#converter for powershell 4.0 or greater
else{
    Write-Host "Simple algorithm possible"
    $hash = Get-FileHash $filepath -Algorithm MD5
    Write-Host $hash.Hash
    $hash.hash | Out-File ($filename+".md5")
}
