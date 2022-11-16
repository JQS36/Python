import textwrap

def wrap3(string, max_width):
    """wrapper = textwrap.TextWrapper(width=max_width)
    word_list = wrapper.wrap(text=string)
    return "\n".join(word_list)"""
    w = ""
    for i in range(0, len(string), max_width):
        w = w + string[:max_width] + "\n"
        string = string[max_width:]
    return w

string "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
max_width = 4
print(wrap3(string, max_width))