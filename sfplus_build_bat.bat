@echo off
set PATH=%PATH%;%~dp0\bat_tools
set WorkingCopyPath=%~dp0
cls

echo --------------------------------------------
echo Fetching all commits from the repository...
echo --------------------------------------------

for /f "delims=" %%i in ('git rev-list HEAD --count') do set REVISIONNUMBER=%%i

:MENU
cd /d %~dp0
cls

chgcolor 1B

echoj $C9 ================================== $bb
echoj $0a $ba " Shotgun Frenzy Plus Pk3 builder! " $ba 
echoj $0a $C8 ================================== $bc
echo.
echo.
echo.

chgcolor 01
echoj "Path: "
echo %~dp0
echo.
echoj "Git Revision: "
echo %REVISIONNUMBER%
echo.

chgcolor 0B

echo Pick a number for your option.
chgcolor 09
echoj 1) 
echo  Build with the local build.

echoj 2) 
echo  Build with the git build.

echoj 3) 
echo  Quit.

CHOICE /C 1234567 /N /M "Choose Option (Number Keys):"
IF ERRORLEVEL 3 GOTO LEAVE
IF ERRORLEVEL 2 GOTO GIT_BUILD
IF ERRORLEVEL 1 GOTO LOC_BUILD



:GIT_BUILD
chgcolor 0B
echo Compiling Shotgun Frenzy Plus Rev#: %REVISIONNUMBER% (Full Compression)...
del .\builds\sfplus_r%REVISIONNUMBER%.pk3 /q

cd pk3
7za a -y -tzip -mx=9 -mmt -x!.svn ..\builds\sfplus_r%REVISIONNUMBER%.pk3 .\
pause
goto MENU

:LOC_BUILD
echo Compiling Shotgun Frenzy Plus Local Dev Build...
del .\builds\sfplus.pk3 /q

cd pk3
7za a -y -tzip -mx=0 -mmt -x!.svn ..\builds\sfplus.pk3 .\
pause
goto MENU

:LEAVE
cls
echo Good-bye!
timeout 5