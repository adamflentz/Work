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

$filepath = $args[0]
$filename = Split-Path $filepath -leaf
$md5 = New-Object -TypeName System.Security.Cryptography.MD5CryptoServiceProvider
$hash = [System.BitConverter]::ToString($md5.ComputeHash([System.IO.File]::ReadAllBytes($filepath)))
Write-Host $hash

$hash | Out-File  ($filename+".md5")