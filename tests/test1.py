from pathlib import Path

p = Path(__file__).parent.parent / 'procesess'

with open(p / 'краш.txt',encoding='utf-8') as f:
    crash_list = [n.strip() for n in f.readlines()]
with open(p/'не краш.txt',encoding='utf-8') as f:
    no_crash_list = [n.strip() for n in f.readlines()]

prob_crash  = []
no_crash_set = set(no_crash_list)
for item in set(crash_list):
   if item not in no_crash_set:
       prob_crash.append(item)


print(prob_crash)