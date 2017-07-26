############################################################################################################
#
# Name: boxservicedownload.ps1
# Purpose: DOWNLOAD a file from the EIS box webservice for storage
# Author: Adam Lentz
# Version 1.0
# Params: 
# 1) URI: the url  to download from
# 2) TOKEN: security token for authorization
# 3) PATH: Box "path" to download the file
# 4) ENV: Box environment to download the file (e.g. PRD, PPRD)
# 5) FILENAME: the name of the file to download
# 6) FILEPATH: the place the new file should be downloaded to
# 7) DELETEFLAG: Whether or not file should be deleted upon download (just moved to a folder called deleted)
# 8) VERIFY: Whether or not the file should be verified with a corresponding md5
#
# NOTES: requires Powershell >=3.0
#############################################################################################################

#check args length
if ($args.Length -lt 6 -or $args.Length -gt 7)
{
	Write-Error "Wrong Command Format: boxservicepost.ps1 <host> <security token> <remote box path> <box environment> <file name> <delete flag> <md5 verification>"
	Exit 1
}

$uri = $args[0] 
$json_token = $args[1] 
$path = $args[2] 
$env = $args[3] 
$filename = $args[4] 
$deleteflag = $args[5]
if(args[6]){
	$md5=args[6]
}
else{
	$md5 = $null 
}

#create POST body

#create headers
$headers = @{}
$headers.Add("environment",$env)
$headers.Add("path",$path)
$headers.Add("Authorization", "Token "+$json_token)
$headers.Add("deleteflag", $deleteflag)

#download md5
if($md5 -eq 'Y'){
	#check powershell version
	[int]$MajorVersion = $PSVersionTable.PSVersion.Major
	Write-Host Version $MajorVersion

	#download md5 file for powershell 3.0 or less
	if($MajorVersion -lt 4){
		$headers.Add("filename", $filename+".md5")
		try {
			$md5result = Invoke-WebRequest -UseBasicParsing -Uri $uri -Method POST -Headers $headers
			# Write-Host $result
			}
			catch [System.Net.WebException] {
				Write-Error( "FAILED to reach '$uri': $_" )
				Write-Host "Process will continue without retrieving MD5.  File cannot be verified."
				$md5 = 'N'
				throw $_
			}
		$headers.Remove("filename")
	}
}


#create file header
$headers.Add("filename", $filename)

#invoke the service
try {
	$result = Invoke-WebRequest -UseBasicParsing -Uri $uri -Method POST -Headers $headers

}
catch [System.Net.WebException] {
    Write-Error( "FAILED to reach '$uri': $_" )
    throw $_
}

#only runs if md5 file was found earlier.
if($md5 -eq 'Y'){
	#converter for powershell 3.0 or less
	if($MajorVersion -lt 4){
		Write-Host "Old version.  Files greater than 2.0 GB cannot be converted."
		$md5object = New-Object -TypeName System.Security.Cryptography.MD5CryptoServiceProvider
		$hash = [System.BitConverter]::ToString($md5.ComputeHash([System.IO.File]::ReadAllBytes($result)))
		if($hash.hash - $md5result){
			Write-Output $result
		}

	}

	#converter for powershell 4.0 or greater
	else{
		Write-Host "Simple algorithm possible"
		$hash = Get-FileHash $result -Algorithm MD5
		Write-Host $hash.Hash
		if($hash.hash - $md5result){
			Write-Output $result
		}
	}
}
else{
	Write-Output $result
}

