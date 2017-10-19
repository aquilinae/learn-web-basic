'''
# таск 1 ввести число и вывести отрицательное оно или положительное

def zero_attitude(number):
    if number > 0:
        message = "Your number is higher than 0"
    elif number < 0:
        message = "Your number is lesser than 0"
    else:
        message = "Your number is zero"
    return message

number = input("Enter a number or 'exit': ")
while not number.isalpha():
    print(zero_attitude(int(number)))
    number = input("Enter a number: ")
'''
'''
if number > 0:
    print("Your number is higher than 0")
elif number < 0:
    print("Your number is lesser than 0")
else:
    print("Your number is zero")
'''

'''
# таск 2 ввести строку и вывести для каждого символа по три его символа

nstring = ''
string = input("Enter short string: ")
for char in string:
    print(char * 3)
print(nstring)
'''

'''
# таск 3 функция, которая выводит возводит число в квадрат

def squares(number):
    print("Square: {}\nDouble square: {}\nTriple square: {}".format(pow(number, 2), pow(number, 4), pow(number, 8)))

number = int(input("Enter a number to square: "))
squares(number)
'''

# создать класс любой объект в комнате
class Keyboard:


    def __init__(self, manufacturer, model, formfactor, wire_type, key_type, ):
        self.manufacturer = manufacturer
        self.model = model
        self.formfactor = formfactor
        self.wire_type = wire_type
        self.key_type = key_type

    def describe(self):
        print("Keyboard {} {}".format(self.manufacturer.title(), self.model.upper()), "have options:\nFormfactor: {}\nWire: {}\nKeys type: {}".format(self.formfactor.title(), self.wire_type.title(), self.key_type.title()))

genius_keyboard = Keyboard('genius', 'gmt-100', '100%', 'wire', 'membran')
genius_keyboard.describe()
