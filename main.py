import sys
from level1 import level1
from level2 import level2
from level3 import level3
from level4 import level4
from share import remove_comments
import os
# Get the path to the file from the second command line argument


#print(list(itertools.compress(test,choose(test))))


import ast

if __name__=="__main__":
    path = sys.argv[1]


    try:
        des=sys.argv[2]
    except:
        des="dist"    
# Open the file in write mode and write the number 1 to it

    with open(path, "r") as file:
        code=file.read()
        code=remove_comments(code)
        #code=remove_annotations(code)#压缩，有问题
        print(code)
    #某些代码需要文件夹存在，无法自动创建
    os.system(f"cd {des}||md {des}")
    #os.system("")    
    if "import" in code:
        level4(code,des)
    else:
        if code=="print(\"helloworld\")":#level1
            level1(code,des)
        elif ("input"in code) or ("open"in code) :  
            level3(code,des)
        else:#level2
            level2(code,des)
    




    