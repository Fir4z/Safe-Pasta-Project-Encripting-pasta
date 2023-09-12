cls
@ECHO OFF
title PastaSegura
if EXIST "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}" goto UNLOCK
if NOT EXIST PastaSegura goto MDLOCKER
:UNLOCK
attrib -h -s "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"
ren "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}" PastaSegura
echo Folder Unlocked successfully
goto End

:MDLOCKER
md PastaSegura
echo Locker created successfully
goto End

open PastaSegura
:End