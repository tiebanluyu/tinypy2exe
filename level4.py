import os
import shutil
def level4(code,des):
    with open(des+"/code.py","w") as f:
        f.write(code)
    
    os.system(f"pyinstaller {des}/code.py")  