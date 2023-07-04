from share import *
from level2 import execute_code

def level3(code:str):
    """
    有input之类的不可控函数，但没有inport的代码
    只能用pyinstaller，但大部分库可以删去，因为引用不到
    """
    logging.info("打包等级level3")
    #创建py文件，为pyinstaller做准备
    with open("dist/code.py","w") as f:
        f.write(code)

    #执行pyinstaller
    os.system(f"cd dist&& pyinstaller code.py")  

    exceptions = ["code.exe", "base_library.zip"]
    for filename in os.listdir("dist/dist/code"):
        if filename.startswith("python"):
            exceptions.append(filename)

    

    #删除文件和移动文件
    shutil.copytree("dist/dist/code", "dist_temp")
    #shutil.rmtree("dist")#按理说可以删除非空文件夹，可就是不行，用cmd命令
    os.system("rmdir /s /q dist")

    shutil.move("dist_temp", "dist")
    delete_files_except("dist", exceptions) 
    #compresszip(des)#这次删对了


def delete_files_except(des, exceptions):
    for filename in os.listdir(des):
        if filename not in exceptions:
            filepath = os.path.join(des, filename)
            if os.path.isdir(filepath):
                shutil.rmtree(filepath)
            else:
                os.remove(filepath)#上次删错了
def compresszip(des):
    import zipfile
    
    

    # 解压base_library.zip
    with zipfile.ZipFile(des+'/base_library.zip', 'r') as zip_ref:
        zip_ref.extractall(des)
    
    # 将pyc文件转换成py文件，再对代码进行压缩
    #问题是，这个pyc文件似乎有问题，反编译几乎无功而返
    for pyc_file in return_pyc_files(des):

        pyc_file = des+"/"+pyc_file
        py_file = pyc_file[:-1]


        print(f"uncompyle6 {pyc_file} >> {py_file} ")
        os.system(f"uncompyle6 {pyc_file} >> {py_file}")
        errortxt="Stacks of completed symbols:"
        if  errortxt in open(py_file,"r").read() or os.path.getsize(py_file) < 300:
            os.remove(py_file)
        else:
            try:
                exec("import "+py_file[0:-3])
            except:
                os.remove(py_file)
                continue   
            import share 
            with open(py_file,"r+") as f:
                txt=share.remove_comments(f.read())
            os.remove(py_file)    
            with open(py_file,"w") as f:
                f.write(txt)
    os.remove(des+"//base_library.zip")
    #os.system("del {des}//*.pyc")    
    """       
    # Zip all py files into base_library.zip
    with zipfile.ZipFile(des+'/base_library.zip', 'w') as zipf:
        for py_file in return_py_files(des):
            zipf.write(py_file)"""
def return_pyc_files(des):
    """
    输出指定目录下所有pyc文件
    """
    py_files = []
    for filename in os.listdir(des):
        if filename.endswith(".pyc"):
            py_files.append(filename)
            print(filename)
    return py_files
def return_py_files(des):
    """
    输出指定目录下所有py文件
    """
    py_files = []
    for filename in os.listdir(des):
        if filename.endswith(".py"):
            py_files.append(filename)
            
    return py_files
            
