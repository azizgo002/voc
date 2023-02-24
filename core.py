class Core:
    def __init__(self) -> None:
        pass

    def insert(self, eng, uzb):
        with open('voc.txt', 'a') as f:
            f.write(f'{eng}|{uzb}\n')

    def __get_all_db(self):
        with open('voc.txt') as f:
            data = f.read().split('\n')[:-1]
            data = tuple(map(lambda line: tuple(line.split('|')), data))
        return data

    def select_all(self):
        return self.__get_all_db() 

    def get_search_word(self, search_word):
        for line in self.__get_all_db():
            if search_word in line:
                return f'{line[0]} {line[1]}'
            
        return False