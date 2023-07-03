from share import *
def level4(code,des):
    print(des)
    with open(des+"/code.py","w",encoding="utf-8") as f:
        f.write(code)
    
    os.system(f"cd {des} && pyinstaller code.py")  
    #删除文件和移动文件
    shutil.copytree("dist/dist/code", "dist_temp")
    #shutil.rmtree("dist")#按理说可以删除非空文件夹，可就是不行，用cmd命令
    os.system("rmdir /s /q dist")

    shutil.move("dist_temp", "dist")