import asyncio
import genshin

async def get_character_data():
    # Авторизация по кукам
    client = genshin.Client(lang="ru-ru",region=genshin.Region.E)
    client.set_cookies(ltuid_v2='206355386',
                       ltoken_v2='v2_CAISATAaJDc2NjIwMTk3LTI3ZjMtNGYyZi1iZTU3LWYzZjUzOTMxY2VhMyDrqbHPBiisp5SaBDC697JiQgphY2NvdW50X29zagJTRw.61TsaQAAAAAB.MEQCIDybkVE1TniUGoS_4hpL3xu2ZxfWOd1Pj8suGQtS-vB4AiBgd-RZ9uY-zbQJu92dEYZBQg4wCQc9uZP6KBgMC7Qzkw')

    # Получаем данные профиля (UID игры, а не HoYoLAB)
    uid = 812345678
    data = await client.get_genshin_user(uid)

    for char in data.characters:
        print(f"Персонаж: {char.name}, Уровень: {char.level}")
        # Здесь будут все данные, которые прилетают в пакетах на сайте

asyncio.run(get_character_data())