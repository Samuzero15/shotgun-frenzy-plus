@echo off
set PATH=%PATH%;%~dp0\bat_tools
set WorkingCopyPath=%~dp0
cls

echo --------------------------------------------
echo Fetching all commits from the repository...
echo --------------------------------------------

for /f "delims=" %%i in ('git rev-list HEAD --count') do set REVISIONNUMBER=%%i

cd core
	for /f "tokens=2 delims=()" %%a in (GAMEINFO.txt) do set RELASE=%%a
		
	
echo %RELASE%
rem do set RELASE=%%A

pause

:MENU
cd /d %~dp0
cls

chgcolor 1B

echoj $C9 $CD $CD $CD $CD $CD $CD $CD $CD $CD $CD $CD $CD $CD $CD $CD $CD $CD $CD $CD $CD $CD $CD $CD $CD $cd $CD $CD $CD $CD $CD $CD $CD $CD $CD $cd $CD $CD $CD $CD $CD $bb
echoj $0a $ba " Shotgun Frenzy Plus Music packer! " $ba 
echoj $0a $C8 $CD $CD $CD $CD $CD $CD $CD $CD $CD $CD $CD $CD $CD $cd $CD $CD $CD $CD $CD $CD $CD $CD $CD $CD $cd $CD $CD $CD $CD $CD $CD $CD $CD $CD $cd $CD $CD $CD $CD $CD $bc
echo.
echo.

chgcolor 0E
echoj "Path: "
echo %~dp0
echo.
echoj "Relase tentative: "
echo %Relase%
echo.

chgcolor 1B
echoj $C9 $CD $CD $CD $CD $CD $CD $CD $CD $cd $CD $CD $CD $CD $CD $CD $CD $CD $CD $CD $cd $CD $CD $CD $CD $CD $CD $CD $CD $CD $cd $CD $CD $CD $CD $CD $bb
echoj $0a $ba " Pick a number for your option.    " $ba
echoj $0a $ba "1) Quick pack.                     " $ba
echoj $0a $ba "2) Compressed pack.                " $ba
echoj $0a $ba "3) Quit.                           " $ba                  

echoj $0a $C8 $CD $CD $CD $CD $CD $CD $CD $CD $cd $CD $CD $CD $CD $CD $CD $CD $CD $CD $CD $cd $CD $CD $CD $CD $CD $CD $CD $CD $CD $cd $CD $CD $CD $CD $CD $bc
echo.
chgcolor 0B
CHOICE /C 1234 /N /M "Which one? (Number Keys):"
IF ERRORLEVEL 3 GOTO LEAVE
IF ERRORLEVEL 2 GOTO REL_BUILD
IF ERRORLEVEL 1 GOTO DEV_BUILD

:REL_BUILD
echo Compiling Shotgun Frenzy Plus Music (%RELASE%)...
pause
del .\builds\relases\sfplus_mus_%RELASE%.pk3 /q

cd mus
7za a -y -tzip -mx=9 -mmt -x!.svn ..\builds\relases\sfplus_mus_%RELASE%.pk3 .\ && echo Sucess! && echoj $07

pause
goto MENU

:DEV_BUILD
chgcolor 0B

echo Compiling Shotgun Frenzy Plus Music Local Dev Build...
pause
del .\sfplus_mus-d.pk3 /q

cd mus
7za a -y -tzip -mx=0 -mmt -x!.svn ..\sfplus_mus-d.pk3 .\ && echo Sucess! && echoj $07

pause
goto MENU

:LEAVE
cls
chgcolor 0f
echo Thanks for trying this bat file!

echo The repository is on GitHub: https://github.com/Samuzero15/shotgun-frenzy-plus
echo See you soon!

timeout 10