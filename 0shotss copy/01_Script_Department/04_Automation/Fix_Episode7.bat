@echo off
echo ========================================================
echo Installing required tools...
echo ========================================================
pip install mammoth

echo.
echo ========================================================
echo Generating the CLEAN Master Script with Dialogues...
echo ========================================================
python generate_perfect_script.py

echo.
echo ========================================================
echo SUCCESS! 
echo Your new file "E7_Perfect_Script.md" is ready.
echo This file has CLEAN formatting and all Dialogues.
echo ========================================================
pause
