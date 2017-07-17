#####################################################################
#
# Name: boxservicedownload.ps1
# Purpose: DOWNLOAD a file from the EIS box webservice for storage
# Author: Adam Lentz
# Version 1.0
# Params: 
# 1) URI: the url  to DOWNLOAD from
# 2) TOKEN: security token for authorization
# 3) PATH: Box "path" to download the file
# 4) ENV: Box environment to download the file (e.g. PRD, PPRD)
# 5) FILE: path to box file to DOWNLOAD
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
