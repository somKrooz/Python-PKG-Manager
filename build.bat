echo off

echo Task 1: Activating virtual environment
call .venv\Scripts\activate

echo Task 2: Removing Prebuild Files
python utils/remove.py

echo Task 3: Generating Executable  
pyinstaller src/manager.py  --onefile

echo Task 4: Moving Build  
python utils/move.py 

echo done
echo done
echo done
echo done
echo done

echo All tasks completed successfully. The executable is located at dist/manager.exe.

deactivate

cls

