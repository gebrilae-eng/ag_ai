cd C:\ag_ai
git rm --cached do_commit.bat 2>nul
git add -A
git commit -m "chore: remove do_commit.bat temp file"
git push origin main
