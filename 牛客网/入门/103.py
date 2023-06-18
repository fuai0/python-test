import re
str = input()
num = re.match('[0-9,-]{10,20}',str)

print(num.group())