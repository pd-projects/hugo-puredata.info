@echo off

set cw=%~dp0

FORFILES /m *.md /s /C "cmd /c pandoc -f markdown -t html5 @FILE --template %cw%template.txt -o @FNAME.html"

