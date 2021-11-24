@echo off

set cw=%~dp0

FORFILES /m *.md /s /C "cmd /c %cw%pandoc.exe -f markdown -t html5 @FILE --template %cw%template.txt -o @FNAME.html"

