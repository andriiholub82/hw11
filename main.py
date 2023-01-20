from collections import UserDict
from datetime import datetime


class AddressBook(UserDict):
    
    def add_record(self, rec):
        self.data[rec.name.value] = rec 

    def iterator(self, n=2):
        index = 0
        temp = []
        for k, v in self.data.items():
            temp.append(v)
            index += 1
            if index >= n:
                yield temp
                temp.clear()
                index = 0
        if temp:
            yield temp

    def get_page(self, n=2):
        gen = self.iterator(n)
        for i in range(len(self.data)):
            try:
                result = next(gen)
                print(result)
                input('Press enter for next page: ')
            except StopIteration:
                break
        


class Record:
    
    def __init__(self, name, phone=None, birthday=None) -> None:
        self.name = name
        self.phones = []
        self.birthday = ""
        if birthday:
            self.birthday = birthday
        if phone:
            self.phones.append(phone)

    def add_phone(self, phone):
        self.phones.append(phone)

    def edit_phone(self, old_phone, new_phone):
        for i in self.phones:
            if i.value == old_phone.value:
                i.value = new_phone.value

    def delite_phone(self, phone):
        for i in self.phones:
            if i.value == phone.value:
                self.phones.remove(phone)

    def days_to_birthday(self):
        if self.birthday:
            current_datetime = datetime.now()
            year = current_datetime.year
            bday = datetime.strptime(self.birthday.value, "%d.%m.%Y").date()
            cur_bday = bday.replace(year=year)
            delta = cur_bday - current_datetime.date()
            if delta.days < 0:
                cur_bday = bday.replace(year=year + 1)
                delta = cur_bday - current_datetime.date()
            return delta
        else:
            return f"{self.name} have not birthday"

    def __repr__(self) -> str:
        return f"{self.name} {', '.join([str(ph) for ph in self.phones])} {self.birthday}"



class Field:

    def __init__(self, value) -> None:
        self.value = value
        self.__value = None

    # def __str__(self) -> str:
    #     return self.value

    def __repr__(self) -> str:
        return self.value


class Name(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if 2 < len(value) < 12:
            self.__value = value
        else:
            print(f"Name should be more than 2 symbol")



class Phone(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if len(value) == 10:
            self.__value = "+38" + value
        elif len(value) == 12:
            self.__value = "+" + value
        else:
            print(f"Format not correct, use 098******* or 38098*******")


class Birthday(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        elements = value.split('.')
        flag = False
        if len(elements) == 3:
            if len(elements[0]) == 2 and len(elements[1]) == 2 and len(elements[2]) == 4:
                if elements[0].isdigit() and elements[1].isdigit() and elements[2].isdigit():
                    self.__value = value
                    flag = True
        if flag is False:
            print(f"Format not correct, use 01.01.2000")

if __name__ == '__main__':
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)

    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '+381234567890'
    

    print('All Ok)')

   
   
    
