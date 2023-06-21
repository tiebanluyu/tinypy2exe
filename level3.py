import os
import shutil
def level3(code,des):
    with open(des+"/code.py","w") as f:
        f.write(code)
    
    os.system(f"pyinstaller {des}/code.py")    
    
    # Usage example:
    
    exceptions = ["code.exe", "base_library.zip"]
    des=des+"/code"
    for filename in os.listdir(des):
        if filename.startswith("python"):
            exceptions.append(filename)
    delete_files_except(des, exceptions)
def delete_files_except(des, exceptions):
    for filename in os.listdir(des):
        if filename not in exceptions:
            filepath = os.path.join(des, filename)
            if os.path.isdir(filepath):
                shutil.rmtree(filepath)
            else:
                os.remove(filepath)

