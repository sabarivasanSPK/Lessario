@echo off
echo ========================================================
echo STEP 1: Current Git Status
echo ========================================================
git status
echo.
echo Press any key to start the batch commits...
pause > nul

echo.
echo ========================================================
echo STEP 2: Committing Tech Lab (Scripts)
echo ========================================================
git add "04_Tech_Lab"
git commit -m "Git Batch: Organized Tech Lab with all Python scripts and automation tools"

echo.
echo ========================================================
echo STEP 3: Committing Script Department
echo ========================================================
git add "01_Script_Department"
git commit -m "Git Batch: Reorganized Script Department into episode-specific folders"

echo.
echo ========================================================
echo STEP 4: Committing Art Department
echo ========================================================
git add "02_Art_Department"
git commit -m "Git Batch: Organized Art Department character assets"

echo.
echo ========================================================
echo STEP 5: Committing Film Studio (E7 Project)
echo ========================================================
git add "03_Film_Studio"
git commit -m "Git Batch: Moved Episode 7 production files to Film Studio"

echo.
echo ========================================================
echo STEP 6: Final Cleanup
echo ========================================================
git add .
git commit -m "Git Batch: Final studio restructure cleanup and dashboard creation"

echo.
echo ========================================================
echo ALL BATCH COMMITS COMPLETE!
echo Your project is now safely backed up in 5 logical steps.
echo ========================================================
pause
