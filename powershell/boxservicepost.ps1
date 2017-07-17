#####################################################################
#
# Name: boxservicepost.ps1
# Purpose: POST a file to the EIS box webservice for storage
# Author: Scott Stewart
# Version 1.0
# Params: 
# 1) URI: the url  to POST to
# 2) TOKEN: security token for authorization
# 3) PATH: Box "path" to place the file
# 4) ENV: Box environment to place the file (e.g. PRD, PPRD)
# 5) FILE: path to local file to POST
#
# NOTES: requires Powershell >=3.0
######################################################################

#check args length
if ($args.Length -ne 5)
{
	Write-Error "Wrong Command Format: boxservicepost.ps1 <host> <security token> <remote box path> <box environment> <local file path>"
	Exit 1
}

$uri = $args[0] 
$json_token = $args[1] 
$path = $args[2] 
$env = $args[3] 
$file = $args[4] 


#read file
$fileBin = [IO.File]::ReadAllBytes($file)
$enc = [System.Text.Encoding]::GetEncoding("iso-8859-1")
$fileEnc = $enc.GetString($fileBin)


#create POST body
$boundary = [System.Guid]::NewGuid().ToString()    
$LF = "`r`n"
$bodyLines = (
	"--$boundary",
	"Content-Disposition: form-data; name=`"file`"; filename=`"$file`"$LF",   
	$fileEnc,
	"--$boundary--$LF"
	) -join $LF

#create header
$headers = @{}
$headers.Add("Authorization", "Token "+$json_token)

#add path and environment to header
$values = @{}
$headers.Add("environment",$env)
$headers.Add("path",$path)


#invoke the service
try {
	$result = Invoke-WebRequest -UseBasicParsing -Uri $uri -Method POST -Headers $headers -Body $bodyLines -ContentType "multipart/form-data; boundary=`"$boundary`"" 
	Write-Host $result
}
catch [System.Net.WebException] {
    Write-Error( "FAILED to reach '$uri': $_" )
    throw $_
}

