from level1 import level1
from level2 import level2
from level3 import level3
from level4 import level4
from share import *
#导入
logging.basicConfig(level=10)





if __name__=="__main__":

    path:str = sys.argv[1]#第一个参数是目标文件的地址
    try:
        des=sys.argv[2]#第二个参数是打包后的文件的地址，默认为dist
    except:#为了可维护性，打包时统一用dist，完成后再将其移动到目标位置
        des="dist"    

    with open(path, "r",encoding="utf-8") as file:
        code=file.read()
        code=remove_comments(code)
    #删除文件夹，再次创建   
    logging.warning("由于将dist作为输出文件夹，所以需要将其清空")
    if input("确认清空，如不，输入q，结束程序")=="q":
        raise Exception
    os.system("rmdir /s /q dist")       
    logging.warning("再次创建dist文件夹")
    os.system("md dist")
 

    if "import" in code:
        level4(code)
    else:
        if code=="print(\"helloworld\")":
            level1(code)
        elif ("input"in code) or ("open"in code) :  
            level3(code)
        else:#level2
            level2(code)
    logging.info("完成软件生成")   
    if des!="dist":
        shutil.move("dist",des)     
        logging.info("文件移动完成") 
    logging.info("无论上面怎么回事，看到这一行，代表成功")       
    logging.info("目标文件为dist目录下的main.exe或code.exe")  
    




    