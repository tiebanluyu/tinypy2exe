def remove_comments(code):
    """
    移除注释
    """
    lines = code.split("\n")
    new_lines = []
    in_triple_quotes = False
    for line in lines:
        if '"""' in line:
            in_triple_quotes = not in_triple_quotes
            new_line = line[: line.index('"""')]
        elif in_triple_quotes:
            new_line = ""
        elif "#" in line:
            new_line = line[: line.index("#")]
        else:
            new_line = line
        new_lines.append(new_line)
    result = "\n".join(new_lines)

    while result.find(" \n") + 1:
        result = result.replace(" \n", "\n")
    while result.find("\n\n") + 1:
        result = result.replace("\n\n", "\n")
    result = result.replace("    ", " ")
    return result


import os, shutil, sys  # 每个文件几乎所有模块都要 ，统一导入
import logging

import time
def fake_progress_bar():
    t=15
    for progress in range(0,  t+ 1, 1):
        print(f"Progress: {progress}% [{'=' * (progress // 15)}{' ' * ((t - progress) // 10)}]", end='\r')
        time.sleep(1)  # 模拟延迟

