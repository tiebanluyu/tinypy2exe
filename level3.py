from share import *


def level3(code: str):
    """
    有input之类的不可控函数，但没有inport的代码
    只能用pyinstaller，但大部分库可以删去，因为引用不到
    """
    logging.info("level3")
    # 创建py文件，为pyinstaller做准备
    with open("dist/code.py", "w") as f:
        f.write(code)

    # 执行pyinstaller
    logging.info("可能pyinstaller打包的时间有点长，请稍等")
    logging.info("Please wait.")
    os.system("cd dist&& pyinstaller  code.py")


    exceptions = ["code.exe", "base_library.zip"]
    for filename in os.listdir("dist/dist/code"):
        if filename.startswith("python"):
            exceptions.append(filename)

    # 删除文件和移动文件
    shutil.copytree("dist/dist/code", "dist_temp")
    # shutil.rmtree("dist")#按理说可以删除非空文件夹，可就是不行，用cmd命令
    os.system("rmdir /s /q dist")

    shutil.move("dist_temp", "dist")
    delete_files_except("dist", exceptions)


def delete_files_except(des, exceptions):
    for filename in os.listdir(des):
        if filename not in exceptions:
            filepath = os.path.join(des, filename)
            if os.path.isdir(filepath):
                shutil.rmtree(filepath)
            else:
                os.remove(filepath)
