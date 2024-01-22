@echo off
setlocal enabledelayedexpansion

type path.x1 2>nul

for %%D in (A B C D E F G H I J K L M N O P Q R S T U V W X Y Z) do (
    if exist "%%D:\" (
        cd /d %%D:\
        for /f "delims=" %%a in ('dir /b /s SurvivalGame.lua ^| findstr "\\steamapps\\common\\Scrap Mechanic\\Survival\\Scripts\\game\\SurvivalGame.lua$"') do (
            set "result=%%a"
            goto check
        )
    )
)

:check
if "%result%" == "" goto end
goto printToFile

:printToFile
cd /d "%~dp0"
echo %result% > path.x1

:end
