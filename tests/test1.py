import re

data = "-67*0--9-0*68-"

num = r'(?:0|[6789][06789]*)'
pattern = rf'{num}(?:[-*]{num})*'

matches = re.finditer(pattern, data)

print(*matches)

