@echo off
echo ========================================================
echo Installing required tools...
echo ========================================================
pip install mammoth

echo.
echo ========================================================
echo Converting the Word Document to Markdown...
echo ========================================================
python convert_mammoth.py

echo.
echo ========================================================
echo Adding Dialogues...
echo ========================================================
python add_dialogues.py

echo.
echo ========================================================
echo ALL DONE! You can close this window now.
echo ========================================================
pause
