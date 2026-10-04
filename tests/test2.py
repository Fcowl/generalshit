text:str = input()
text_split: list[str] = text.replace(",",'').replace('.','').split()
word_am:int = len(text_split)

expl_counter:int = text.count('!')
quest_count:int = text.count('?')

biggest_word:str = max(text_split, key=len)
total_length = len(''.join(text_split))
avg_length = sum()

print(word_am)
print(expl_counter)
print(quest_count)
print(biggest_word)
print(total_length)
