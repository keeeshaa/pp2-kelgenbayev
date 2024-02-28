import re

txt = input()
new_txt = ""
li =list()
for i in range(len(txt)):
    if re.match(r'[A-Z]', txt[i]):
        new_txt += " "
    new_txt += txt[i]
new_txt = re.split(r"[ ]", new_txt)
for i in new_txt:
    text = i.lower()
    li.append(text)
new_txt = "_".join(li)
print(new_txt)
