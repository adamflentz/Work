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
	Write-Error "Wrong Command Format: boxservicepost.ps1 <host> <security token> <remote box path> <box environment> <local file path>"
	Exit 1
}

$uri = $args[0] 
$json_token = $args[1] 
$path = $args[2] 
$env = $args[3] 

$headers = @{}
$headers.Add("environment",$this.env)
$headers.Add("path",$this.path)
$headers.Add("Authorization", "Token "+$this.json_token)

#invoke the service
try {
    $result = Invoke-WebRequest -UseBasicParsing -Uri $this.uri -Method POST -Headers $headers 
    Write-Host $result
}
catch [System.Net.WebException] {
    Write-Error( "FAILED to reach '$this.uri': $_" )
    throw $_
}
