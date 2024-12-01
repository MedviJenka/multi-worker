# Get the current script file path dynamically
$filePath = $MyInvocation.MyCommand.Path

# Get the parent directory two levels up
$projectDir = Split-Path -Path $filePath -Parent | Split-Path -Parent

# Extract the project name
$projectName = Split-Path -Path $projectDir -Leaf

# Output the project name
Write-Output "Project name: $projectName"
$appLocation = $projectName\server\core\engine.py
write-host $appLocation
# python $projectName\server\core\engine.py
#
#
# $DNS = ""
# $url = "http://127.0.0.1/api/dns?q=$dns"
# $response = Invoke-WebRequest -Uri $url -Method GET
# $response.Content
