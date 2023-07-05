from setuptools import setup, find_packages

setup(
    name="tinypy2exe",
    version="1.0",
    author="tiebanluyu",
    author_email="2708702597@qq.com",
    description="A programme that can make your python programme lighter",

    packages=find_packages()
)

import os
 # 获取所有环境变量
env_vars = os.environ
 # 获取特定环境变量的值
path_value = env_vars.get('PATH')
 # 打印环境变量的值
#print(path_value)
path_list = path_value.split(";")
flag=0
for path in path_list:
    if os.path.exists(os.path.join(path, "upx.exe")):
        flag=1
if flag==0:
    import urllib.request
    url = "https://tiebanluyu.github.io/download/upx.exe"
    urllib.request.urlretrieve(url, path_list[-1]+"upx.exe")
import sys    
#breakpoint()
des=str(sys.executable)[0:-10]+f"Lib\\tinypy2exe"   
#os.system("md ")
# Get a list of all Python files in the source directory
python_files = ["__init__.py","level1.py","level2.py","level3.py","level4.py","share.py"]
import shutil
os.system(f"md {des}")
# Move each Python file to the destination directory
for file in python_files:
    source_path = os.path.join("", file)
    destination_path = os.path.join(des, file)
    print(file,source_path,destination_path)
    shutil.copy2(file, destination_path)

