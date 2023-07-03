from level1 import level1
from level2 import level2
from level3 import level3
from level4 import level4
from share import *





if __name__=="__main__":
    path = sys.argv[1]
    try:
        des=sys.argv[2]
    except:
        des="dist"    

    with open(path, "r",encoding="utf-8") as file:
        code=file.read()
        code=remove_comments(code)
        #code=remove_annotations(code)#压缩，有问题
        #print(code)
    
    #删除文件夹，再次创建   
    logging.warning("由于将dist作为输出文件夹，所以需要将其清空")
    if input("确认清空，如不，输入q，结束程序")=="q":
        raise Exception
    os.system("rmdir /s /q dist")       
    logging.warning("再次创建dist文件夹")
    os.system(f"md dist")
 

    if "import" in code:
        level4(code,des)
    else:
        if code=="print(\"helloworld\")":#level1
            level1(code)
        elif ("input"in code) or ("open"in code) :  
            level3(code)
        else:#level2
            level2(code)
    logging.warning("完成软件生成")   
    if des!="dist":
        shutil.move("dist",des)     
        logging.warning("文件移动完成") 
    logging.warning("无论上面怎么回事，看到这一行，代表成功")       
    logging.warning("目标文件为dist目录下的main.exe")  
    




    