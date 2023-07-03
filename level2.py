from share import *

def level2(code,des):    
    text = execute_code(code)
    lines = text.split("\n")
    prefixed_lines = ["echo " + line for line in lines]
    text ="@echo off\n"+"\n".join(prefixed_lines)[0:-5]#前面加echo off 删去后面echo
    with open(des + "/main.bat", "w+") as file:
        file.write(text)
    src = "lv2.exe"   
    # Copy the source file to the destination directory
    shutil.copy2(src, des+"/main.exe")


def execute_code(code):
    
    # Create a new StringIO object to capture the print output
    class StringIO():#chatgpt告诉我用第三方库，但用不了，我便自己写一个，可行
        def __init__(self):
            self.text=""
        def write(self,text):
            #确实在exec中调用了这个函数
            self.text=self.text+text
        def getvalue(self):            
            return self.text
        def close(self):            
            pass

    output = StringIO()

    # Save the current stdout
    old_stdout = sys.stdout

    # Redirect stdout to the StringIO object
    sys.stdout = output

    # Execute the code
    exec(code)

    # Get the print output from the StringIO object
    text = output.getvalue()

    # Restore the original stdout
    sys.stdout = old_stdout

    # Close the StringIO object
    output.close()

    return text
   