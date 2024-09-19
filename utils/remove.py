import os
import shutil

if os.path.exists(os.path.join(os.getcwd(),"build")):
        shutil.rmtree(os.path.join(os.getcwd(),"build"),ignore_errors=True)
        shutil.rmtree(os.path.join(os.getcwd(),"dist"),ignore_errors=True)
        
        try:
                os.remove(os.path.join(os.getcwd(),"manager.spec"))
                os.remove(os.path.join(os.getcwd(),"move.spec"))

        except:
              print("Error..................................................")
               
else:
    print("UnBuild... State")