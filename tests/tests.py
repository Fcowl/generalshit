import requests
from bs4 import BeautifulSoup
import datetime

urls = {'09.03.01 Информатика и вычислительная техника':"https://www.nstu.ru/entrance/enrollment_campaign/rating_bachelor/entrance_list?comp_name=%D0%90%D0%92%D0%A2%D0%A4.1&fk_tr_basis=1",
        '09.03.02 Информационные системы и технологии':'https://www.nstu.ru/entrance/enrollment_campaign/rating_bachelor/entrance_list?comp_name=%D0%90%D0%92%D0%A2%D0%A4.2&fk_tr_basis=1',
        '02.03.03 Математическое обеспечение и администрирование информационных систем':'https://www.nstu.ru/entrance/enrollment_campaign/rating_bachelor/entrance_list?comp_name=%D0%A4%D0%9F%D0%9C%D0%98.2&fk_tr_basis=1',
        '09.03.03 Прикладная информатика':'https://www.nstu.ru/entrance/enrollment_campaign/rating_bachelor/entrance_list?comp_name=%D0%90%D0%92%D0%A2%D0%A4.3&fk_tr_basis=1',
        '27.03.04 Управление в технических системах (профиль: "Автоматика и управление")':'https://www.nstu.ru/entrance/enrollment_campaign/rating_bachelor/entrance_list?comp_name=%D0%90%D0%92%D0%A2%D0%A4.8&fk_tr_basis=1',
        '27.03.04 Управление в технических системах (профиль: "Автономные информационные и управляющие системы")':'https://www.nstu.ru/entrance/enrollment_campaign/rating_bachelor/entrance_list?comp_name=%D0%A4%D0%9B%D0%90.9&fk_tr_basis=1'}

my_number = '1262614'
start_text = 'Факультет - мое место (бюджетных мест) мой приоритет - людей с определенным приоритетом выше меня'
print(start_text)
data = [start_text]
for fakultet,url in urls.items():

    priorities_above_me = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0}

    response = requests.get(url)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")
    cards = soup.find_all("div", class_="rating__card")


    for card in soup.find_all('div',class_=""):
        card_text = card.get_text('',strip=False)
        if 'Количество бюджетных мест' in card_text:
            places = card.find('b').text

    for card in cards:
        row = card.find("div", class_="tablelike__table-row")
        profile =  row.find("div", class_="rating__table-cell__case").text.replace("\n", "").replace('\t','')
        place = row.find("div", class_="rating__table-cell__nn").text.replace("\n", "").replace('\t','')
        priority = row.find('div',class_='rating__table-cell__priority').text.replace("\n", "").replace('\t','')
        if my_number in profile:
            output = f'{fakultet} - {place} ({places}) {priority} - {priorities_above_me}'
            print(output)
            data.append(output)
            break

        try:
            priorities_above_me[priority[-1]] +=1
        except KeyError:
            priorities_above_me[priority[-1]] = 1

with open(r'nstu_data.txt', 'a',encoding='utf-8') as f:
    date = datetime.datetime.now().strftime('%d.%m.%Y %H:%M')
    f.write(f'\n{date}\n')
    #f.write('\n')
    #f.write(date)
    for line in data:
        f.write(f'{line} \n')
        #f.write('\n')
print('data saved')