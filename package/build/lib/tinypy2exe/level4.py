from .share import *


def level4(code: str) -> None:
    """
    没有任何可压缩的地方，pyinstaller打包
    只用代码压缩
    """
    logging.info("level4")
    with open("dist/code.py", "w", encoding="utf-8") as f:  # 我也不知道，反正加入utf-8才能正常运行
        f.write(code)
    
    thread = threading.Thread(target=fake_progress_bar)
    thread.start()
    os.system("cd dist && pyinstaller --log-level=WARN code.py")

    # 删除文件和移动文件
    shutil.copytree("dist/dist/code", "dist_temp")
    # shutil.rmtree("dist")#按理说可以删除非空文件夹，可就是不行，用cmd命令
    os.system("rmdir /s /q dist")

    #shutil.move("dist_temp", "dist")
    #总是十有一二在此报错，换cmd
    os.system("ren dist_temp dist")
    """
    for root, dirs, files in os.walk("dist"):
        for folder in dirs:
            if "info" in folder:
                folder_path = os.path.join(root, folder)
                logging.info(f"Deleting folder: {folder_path}")
                os.rmdir(folder_path)"""
