message=input()
normalized_message=message.strip().lower()
words=normalized_message.split()
clean_message=" ".join(words)
clean_count=len(clean_message)
exclamation_count=clean_message.count("!")
question_count=clean_message.count("?")
cleaned_words=[]

for word in words:
    clean_word=word.strip(".,!?;:.")
    if clean_word != "":
        cleaned_words.append(clean_word)

word_count=len(cleaned_words)
longest_word=""

for clean_word in cleaned_words:
    if len(clean_word) > len(longest_word):
        longest_word=clean_word

total_letters=0
for clean_word in cleaned_words:
    total_letters+=len(clean_word)

if word_count > 0:
    average_word_len=total_letters / word_count
else:
    average_word_len=0.0

urgency_markers=["срочно", "немедленно", "сейчас", "быстро"]
secret_data_markers=["пароль", "логин", "код подтверждения", "данные карты"]
secrecy_markers=["никому не говори", "не сообщай", "между нами", "держи в секрете"]

urgency_markers_count = 0
for marker in urgency_markers:
    if marker in clean_message:
        urgency_markers_count += 1

secret_data_markers_count=0
for marker in secret_data_markers:
    if marker in clean_message:
        secret_data_markers_count += 1

secrecy_markers_count=0
for marker in secrecy_markers:
    if marker in clean_message:
        secrecy_markers_count += 1

uppercase_count=0
for word in message.split():
    clean_word = word.strip(".,!?;:.")
    if len(clean_word)>1 and clean_word.isupper():
        uppercase_count+=1
many_exclamations=exclamation_count >= 3
link = ("http://" in clean_message or "https://" in clean_message or "www." in clean_message)
send_markers = ["отправь", "пришли", "сообщи"]
send_request = False
for marker in send_markers:
    if marker in clean_message:
        send_request = True
        break
score=0
if many_exclamations:
    score += 1
if uppercase_count > 0:
    score += 1
if urgency_markers_count > 0:
    score += 2
if secret_data_markers_count > 0:
    score += 3
if secrecy_markers_count > 0:
    score += 3
if link:
    score += 1
if send_request > 0 and secret_data_markers_count > 0:
    score+=2
if score<=2:
    conclusion="НИЗКИЙ РИСК"
elif score<=5:
    conclusion="СРЕДНИЙ РИСК"
else:
    conclusion="ВЫСОКИЙ РИСК"
print("ПАСПОРТ СООБЩЕНИЯ")
print("-----------------")
print(f"Слов: {word_count}")
print(f"Восклицательных знаков: {exclamation_count}")
print(f"Вопросительных знаков: {question_count}")
print(f"Самое длинное слово: {longest_word}")
print(f"Средняя длина слова: {average_word_len}")
found_evidence = []
if urgency_markers_count > 0:
    found_evidence.append("срочность")
if secret_data_markers_count > 0:
    found_evidence.append("запрос секретных данных")
if secrecy_markers_count > 0:
    found_evidence.append("просьба молчать")
if uppercase_count > 0:
    found_evidence.append("слова капсом")
if many_exclamations:
    found_evidence.append("много восклицательных знаков")
if link:
    found_evidence.append("ссылка")
if send_request:
    found_evidence.append("просьба отправить")
if found_evidence:
    print("Найдены улики: " + ", ".join(found_evidence))
else:
    print("Найдены улики: нет")
print(f"Баллы подозрительности: {score}")
print(f"Вердикт: {conclusion}")
safe_message=clean_message
for marker in secret_data_markers:
    safe_message = safe_message.replace(marker, "[СКРЫТО]")
print("Безопасная копия:")
print(safe_message)