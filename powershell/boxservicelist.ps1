#####################################################################
#
# Name: boxservicelist.ps1
# Purpose: List all files in the EIS box webservice for storage
# Author: Adam Lentz
# Version 1.0
# Params: 
# 1) URI: the url  to POST to
# 2) TOKEN: security token for authorization
# 3) PATH: Box "path" to place the file
# 4) ENV: Box environment to place the file (e.g. PRD, PPRD)
#
# NOTES: requires Powershell >=3.0
######################################################################

#check args length
if ($args.Length -ne 4)
{
	Write-Error "Wrong Command Format: boxservicepost.ps1 <host> <security token> <remote box path> <box environment>"
	Exit 1
}

$uri = $args[0] 
$json_token = $args[1] 
$path = $args[2] 
$env = $args[3] 

$headers = @{}
$headers.Add("environment",$env)
$headers.Add("path",$path)
$headers.Add("Authorization", "Token "+$json_token)

#invoke the service
try {
    $result = Invoke-WebRequest -UseBasicParsing -Uri $uri -Method POST -Headers $headers 
    $resultObj = ConvertFrom-Json -InputObject $result
    foreach ($filename in $resultObj) {
        Write-Host $filename.filename
    }
}
catch [System.Net.WebException] {
    Write-Error( "FAILED to reach '$this.uri': $_" )
    throw $_
}
