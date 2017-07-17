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
######################################################################

Class BoxService{
    [String]$json_token
    [String]$path
    [String]$env
    [String]$uri
    [String]$download_path

    #standard getters and setters for methods
    SetToken([string]$tok_string){
        $this.json_token = $tok_string
    }
    SetPath([string]$path_string){
        $this.path = $path_string
    }
    SetEnv([string]$env_string){
        $this.env = $env_string
    }
    SetUri([string]$uri_string){
        $this.uri = $uri_string
    }
    SetDownloadPath([String]$download_string){
        $this.download_path = $download_string
    }

    [string]GetToken(){
        Write-Host $this.json_token
        return $this.json_token
    }
    [string]GetPath(){
        Write-Host $this.path
        return $this.path
    }
    [string]GetEnv(){
        Write-Host $this.env
        return $this.env
    }
    [string]GetUri(){
        Write-Host $this.uri
        return $this.uri
    }
    [string]GetDownloadPath(){
        Write-Host $this.download_path
        return $this.download_path
    }

    List(){
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

    }
    Post(){
        #get file
        [string]$file = Read-Host -Prompt "enter local file path"
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
        $headers.Add("Authorization", "Token "+$this.json_token)

        #add path and environment to header
        $values = @{}
        $headers.Add("environment",$this.env)
        $headers.Add("path",$this.path)


        #invoke the service
        try {
            $result = Invoke-WebRequest -UseBasicParsing -Uri $this.uri -Method POST -Headers $headers -Body $bodyLines -ContentType "multipart/form-data; boundary=`"$boundary`"" 
            Write-Host $result
        }
        catch [System.Net.WebException] {
            Write-Error( "FAILED to reach '$this.uri': $_" )
            throw $_
        }
    }
    
}

#create a BoxService object and get required info from the user
$box = New-Object BoxService
[string]$tok_input = Read-Host -Prompt 'Input your authentication token'
$box.SetToken($tok_input)
[string]$path_input = Read-Host -Prompt 'Input your path'
$box.SetPath($path_input)
[string]$env_input = Read-Host -Prompt 'Input your env'
$box.SetEnv($env_input)
[string]$uri_input = Read-Host -Prompt 'Input your url'
$box.SetUri($uri_input)

#create a menu for the user to interact with box data
do {
    [int] $choice = 0
    while($choice -lt 1 -or $choice -gt 4) {
        Write-Host "1 - list files"
        Write-Host "2 - download files"
        Write-Host "3 - upload files"
        Write-Host "4 - exit"
        [int] $choice = Read-Host -Prompt 'Input number corresponding to action in menu'
        switch($choice)
        {
            1 {Write-Host "`nListing Files:"; $box.List(); Write-Host "`n"}
            2 {
                #TODO add download function
                Write-Host "`nOption 2 selected.`n"
            }
            3 {Write-Host "`nUploading File:"; $box.Post(); Write-Host "`n"}
            4 {
                Write-Host "`nGoodbye`n"
                Exit 1
            }
            default {"`nPlease enter a number listed`n"}
        }
    }
} while ($choice -ne 4)
Write-Host ($box | Get-Member)

