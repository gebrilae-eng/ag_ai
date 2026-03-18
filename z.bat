cd C:\ag_ai
git rm --force x.bat
git add -A
git commit -m "cleanup"
git push origin main
del x.bat 2>nul
