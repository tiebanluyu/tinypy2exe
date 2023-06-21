import shutil

def level1(code:str, des:str):
    # Define the source file path
    src = "helloworld/helloworld.exe"
    
    # Copy the source file to the destination directory
    shutil.copy2(src, des+"/main.exe")