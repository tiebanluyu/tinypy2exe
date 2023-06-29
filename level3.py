import os
import shutil
from level2 import execute_code
def level3(code:str,des:str):
    #创建py文件，为pyinstaller做准备
    with open(des+"/code.py","w") as f:
        f.write(code)

    #执行pyinstaller
    os.system(f"cd {des}&& pyinstaller code.py")  

    exceptions = ["code.exe", "base_library.zip"]
    for filename in os.listdir(des+"/dist/code"):
        if filename.startswith("python"):
            exceptions.append(filename)
    delete_files_except(des+"/dist/code", exceptions)
    

    #删除文件和移动文件
    shutil.copytree("dist/dist/code", "dist_temp")
    shutil.rmtree("dist")
    shutil.move("dist_temp", "dist")
    
    compresszip(des)


def delete_files_except(des, exceptions):
    for filename in os.listdir(des):
        if filename not in exceptions:
            filepath = os.path.join(des, filename)
            if os.path.isdir(filepath):
                shutil.rmtree(filepath)
            else:
                os.remove(filepath)
def compresszip(des):
    import zipfile
    
    

    # 解压base_library.zip
    with zipfile.ZipFile(des+'/base_library.zip', 'r') as zip_ref:
        zip_ref.extractall(des)
    
    # Convert all pyc files to py files
    for pyc_file in return_pyc_files(des):
        py_file = des+"/"+pyc_file
        py_file = pyc_file[:-1]

        import os
        print(f"uncompyle6 {pyc_file} >> {py_file} ")
        os.system(f"uncompyle6 {pyc_file} >> {py_file}")
        errortxt="Stacks of completed symbols:"
        if  errortxt in open(des+"/"+py_file,"r").read() or os.path.getsize(py_file) < 300:
            os.remove(des+"/"+py_file)
        else:
            import share 
            with open(py_file,"r+") as f:
                txt=share.remove_comments(f.read())
                f.seek(0)
                f.write(txt)
    os.remove(des+"//base_library.zip")
    #os.system("del {des}//*.pyc")    
    """       
    # Zip all py files into base_library.zip
    with zipfile.ZipFile(des+'/base_library.zip', 'w') as zipf:
        for py_file in return_py_files(des):
            zipf.write(py_file)"""
def return_pyc_files(des):
    py_files = []
    for filename in os.listdir(des):
        if filename.endswith(".pyc"):
            py_files.append(filename)
            print(filename)
    return py_files
def return_py_files(des):
    py_files = []
    for filename in os.listdir(des):
        if filename.endswith(".py"):
            py_files.append(filename)
            
    return py_files
            
