$ErrorActionPreference = 'Stop'
$toolsDir = "$(Split-Path -parent $MyInvocation.MyCommand.Definition)"
$url = 'https://github.com/socialmediatvtweet-tech/download-format/releases/download/v1.0.0/osldown.exe'

$packageArgs = @{
    packageName   = $env:ChocolateyPackageName
    unzipLocation = $toolsDir
    fileType      = 'exe'
    url           = $url
    softwareName  = 'downloadformat*'
    checksum      = 'CE12C45F820C94C1106AB82FA64BB0EC1F258DD30C92480ACB20761B3A437D5A'
    checksumType  = 'sha256'
    silentArgs    = ''
    validExitCodes= @(0)
}

Install-ChocolateyPackage @packageArgs
