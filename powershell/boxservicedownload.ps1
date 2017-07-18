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
# 6) DELETEFLAG: Whether or not file should be deleted upon download (just moved to a folder called deleted)
#
# NOTES: requires Powershell >=3.0
#############################################################################################################

#check args length
if ($args.Length -ne 6)
{
	Write-Error "Wrong Command Format: boxservicepost.ps1 <host> <security token> <remote box path> <box environment> <file name> <delete flag>"
	Exit 1
}

$uri = $args[0] 
$json_token = $args[1] 
$path = $args[2] 
$env = $args[3] 
$filename = $args[4] 
$deleteflag = $args[5]

#create POST body

#create headers
$headers = @{}
$headers.Add("environment",$env)
$headers.Add("path",$path)
$headers.Add("Authorization", "Token "+$json_token)
$headers.Add("filename", $filename)
$headers.Add("deleteflag", $deleteflag)
#invoke the service
try {
	$result = Invoke-WebRequest -UseBasicParsing -Uri $uri -Method POST -Headers $headers
	# Write-Host $result
	$result | Out-File $filename

}
catch [System.Net.WebException] {
    Write-Error( "FAILED to reach '$uri': $_" )
    throw $_
}

