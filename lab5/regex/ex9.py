import re

txt = input()
new_txt = ""

for i in range(len(txt)):
    if re.match(r'[A-Z]', txt[i]):
        new_txt += " "
    new_txt += txt[i]

print(new_txt)
