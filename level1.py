from share import *

def level1(code:str):
    
    # Define the source file path
    src = "helloworld/helloworld.exe"
    
    # Copy the source file to the destination directory
    shutil.copy2(src, "dist/main.exe")