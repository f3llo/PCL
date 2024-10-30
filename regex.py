import re

test = input(">")

t = r'\[|\]'

print(re.findall(t,test))
