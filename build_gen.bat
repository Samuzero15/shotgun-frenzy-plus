@echo off
set PATH=%PATH%;%~dp0\bat_tools
set WorkingCopyPath=%~dp0
cls

echo --------------------------------------------
echo Fetching all commits from the repository...
echo --------------------------------------------

for /f "delims=" %%i in ('git rev-list HEAD --count') do set REVISIONNUMBER=%%i

cd pk3
	for /f "tokens=5 delims=:, " %%A in (GAMEINFO.txt) do set RELASE=%%A

:MENU
cd /d %~dp0
cls

chgcolor 1B

echoj $C9 $CD $CD $CD $CD $CD $CD $CD $CD $cd $CD $CD $CD $CD $CD $CD $CD $CD $CD $cd $CD $CD $CD $CD $CD $CD $CD $CD $CD $cd $CD $CD $CD $CD $CD $bb
echoj $0a $ba " Shotgun Frenzy Plus Pk3 builder! " $ba 
echoj $0a $C8 $CD $CD $CD $CD $CD $CD $CD $CD $cd $CD $CD $CD $CD $CD $CD $CD $CD $CD $cd $CD $CD $CD $CD $CD $CD $CD $CD $CD $cd $CD $CD $CD $CD $CD $bc
echo.
echo.

chgcolor 0E
echoj "Path: "
echo %~dp0
echo.
echoj "Git Revision: "
echo %REVISIONNUMBER%
echo.
echoj "Relase tentative: "
echo %Relase%
echo.

chgcolor 1B
echoj $C9 $CD $CD $CD $CD $CD $CD $CD $CD $cd $CD $CD $CD $CD $CD $CD $CD $CD $CD $cd $CD $CD $CD $CD $CD $CD $CD $CD $CD $cd $CD $CD $CD $CD $CD $bb
echoj $0a $ba " Pick a number for your option.   " $ba

echoj $0a $ba "1) Build the dev version.         " $ba

echoj $0a $ba "2) Build the relase version.      " $ba

echoj $0a $ba "3) Build the git version.         " $ba

echoj $0a $ba "4) Quit.                          " $ba                  

echoj $0a $C8 $CD $CD $CD $CD $CD $CD $CD $CD $cd $CD $CD $CD $CD $CD $CD $CD $CD $CD $cd $CD $CD $CD $CD $CD $CD $CD $CD $CD $cd $CD $CD $CD $CD $CD $bc
echo.
chgcolor 0B
CHOICE /C 1234567 /N /M "Choose Option (Number Keys):"
IF ERRORLEVEL 4 GOTO LEAVE
IF ERRORLEVEL 3 GOTO GIT_BUILD
IF ERRORLEVEL 2 GOTO REL_BUILD
IF ERRORLEVEL 1 GOTO DEV_BUILD


:GIT_BUILD
chgcolor 0B
echo Compiling Shotgun Frenzy Plus Rev#: %REVISIONNUMBER%...
pause
del .\builds\gits\sfplus_r%REVISIONNUMBER%.pk3 /q

cd pk3
7za a -y -tzip -mx=9 -mmt -x!.svn ..\builds\gits\sfplus_r%REVISIONNUMBER%.pk3 .\
pause
goto MENU

:REL_BUILD
chgcolor 0B

echo Compiling Shotgun Frenzy Plus ( %RELASE% )...
pause
del .\builds\relases\sfplus_%RELASE%.pk3 /q

cd pk3
7za a -y -tzip -mx=9 -mmt -x!.svn ..\builds\relases\sfplus_%RELASE%.pk3 .\

pause
goto MENU

:DEV_BUILD
chgcolor 0B

echo Compiling Shotgun Frenzy Plus Local Dev Build...
pause
del .\sfplus-d.pk3 /q

cd pk3
7za a -y -tzip -mx=9 -mmt -x!.svn ..\sfplus-d.pk3 .\

pause
goto MENU

:LEAVE
cls
echo Good-bye!
timeout 5