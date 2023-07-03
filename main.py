import sys
from level1 import level1
from level2 import level2
from level3 import level3
from level4 import level4
from share import remove_comments
import os
import logging




if __name__=="__main__":
    path = sys.argv[1]
    try:
        des=sys.argv[2]
    except:
        des="dist"    
#获取参数，目前第二个参数暂不支持

    with open(path, "r",encoding="utf-8") as file:
        code=file.read()
        code=remove_comments(code)
        #code=remove_annotations(code)#压缩，有问题
        print(code)
    
    #删除文件夹，再次创建   
    logging.warning(f"由于将{des}作为输出文件夹，所以需要将其清空")
    os.system(f"cd {des}&&rmdir /s  dist")       
    logging.warning(f"再次创建{des}文件夹")
    os.system(f"md {des}")
 

    if "import" in code:
        level4(code,des)
    else:
        if code=="print(\"helloworld\")":#level1
            level1(code,des)
        elif ("input"in code) or ("open"in code) :  
            level3(code,des)
        else:#level2
            level2(code,des)
    logging.warning("无论上面怎么回事，看到这一行，代表成功")       
    logging.warning("目标文件为dist目录下的main.exe")  
    




    