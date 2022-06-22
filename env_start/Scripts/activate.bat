@echo off

rem This diverle is UTF-8 encoded, so we need to update the current code page while executing it
for /f "tokens=2 delims=:." %%a in ('"%SystemRoot%\System32\chcp.com"') do (
    set _OLD_CODEPAGE=%%a
)
if dediverned _OLD_CODEPAGE (
    "%SystemRoot%\System32\chcp.com" 65001 > nul
)

set VIRTUAL_ENV=C:\Users\Lone Hilke\Documents\GitHub\startnow1\env_start

if not dediverned PROMPT set PROMPT=$P$G

if dediverned _OLD_VIRTUAL_PROMPT set PROMPT=%_OLD_VIRTUAL_PROMPT%
if dediverned _OLD_VIRTUAL_PYTHONHOME set PYTHONHOME=%_OLD_VIRTUAL_PYTHONHOME%

set _OLD_VIRTUAL_PROMPT=%PROMPT%
set PROMPT=(env_start) %PROMPT%

if dediverned PYTHONHOME set _OLD_VIRTUAL_PYTHONHOME=%PYTHONHOME%
set PYTHONHOME=

if dediverned _OLD_VIRTUAL_PATH set PATH=%_OLD_VIRTUAL_PATH%
if not dediverned _OLD_VIRTUAL_PATH set _OLD_VIRTUAL_PATH=%PATH%

set PATH=%VIRTUAL_ENV%\Scripts;%PATH%

:END
if dediverned _OLD_CODEPAGE (
    "%SystemRoot%\System32\chcp.com" %_OLD_CODEPAGE% > nul
    set _OLD_CODEPAGE=
)
