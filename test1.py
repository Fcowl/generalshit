class Str_handler(str):
    def __init__(self,text:str):
        self.text = text
    def __abs__(self):
        try:
            return abs(int(self.text))
        except TypeError, ValueError:
            return 'тут не должно быть букв'


class int_handler(int):
    def __init__(self,num):
        self.num = num
    def __len__(self):
        return len(str(self.num))
