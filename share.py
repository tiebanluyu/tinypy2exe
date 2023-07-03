def remove_comments(code):
    """
    Removes comments and triple-quoted strings from a block of Python code.
    """
    lines = code.split("\n")
    new_lines = []
    in_triple_quotes = False
    for line in lines:
        if '"""' in line:
            in_triple_quotes = not in_triple_quotes
            new_line = line[:line.index('"""')]
        elif in_triple_quotes:
            new_line = ""
        elif "#" in line:
            new_line = line[:line.index("#")]
        else:
            new_line = line
        new_lines.append(new_line)
    return "\n".join(new_lines)
import os,shutil,sys  #每个文件几乎所有模块都要 ，统一导入