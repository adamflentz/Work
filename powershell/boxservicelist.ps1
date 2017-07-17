#####################################################################
#
# Name: boxservicelist.ps1
# Purpose: list all stored files in the EIS box webservice 
# Author: Adam Lentz
# Version 1.0
# Params: 
# 1) URI: the url  to list from
# 2) TOKEN: security token for authorization
# 3) PATH: Box "path" to list files
# 4) ENV: Box environment to list the files (e.g. PRD, PPRD)
#
# NOTES: requires Powershell >=3.0
####################################################$uri##################

# check aggs length
# 
Class BoxService{
    [String]$json_token
    [String]$path
    [String]$env
    [String]$uri
    List($uri, $json_token, $path, $env){
        
        #create headers
        $headers = @{}
        $headers.Add("environment",$env)
        $headers.Add("path",$path)
        $headers.Add("Authorization", "Token "+$json_token)

        #invoke the service
        try {
            $result = Invoke-WebRequest -UseBasicParsing -Uri $uri -Method POST -Headers $headers 
            Write-Host $result
        }
        catch [System.Net.WebException] {
            Write-Error( "FAILED to reach '$uri': $_" )
            throw $_
        }

    }
}
if ($args.length -ne 4)
            {$uri
                Write-Error "Wrong Command Format: boxservicelist.ps1 <host> <security token> <remote box path> <box environment>"
                Exit 1
            }

        $uri = $args[0]
        $json_token = $args[1]
        $path = $args[2]
        $env = $args[3]
$box = New-Object BoxService
$box.List
Write-Host ($box | Get-Member -MemberType Properties)

