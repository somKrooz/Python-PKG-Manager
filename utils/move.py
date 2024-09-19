import os
import shutil

os.rename(os.path.join(os.getcwd(),"dist","manager.exe"),os.path.join(os.getcwd(),"dist","krooz.exe"))
shutil.move(os.path.join(os.getcwd(),"dist","krooz.exe"), r"C:\Users\Krooz\kroozTOOL\krooz.exe")