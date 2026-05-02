@echo off
echo ========================================================
echo Setting up Git LFS and Saving your files locally...
echo ========================================================
git lfs install
git lfs track "*.mp4"
git lfs track "*.png"
git lfs track "*.jpg"
git lfs track "*.jpeg"
git lfs track "*.pdf"
git add .gitattributes
git add .
git commit -m "Configure Git LFS and commit all files"

echo.
echo ========================================================
echo Git Commit with LFS Successful! Your files are saved locally.
echo You can close this window now.
echo ========================================================
pause
