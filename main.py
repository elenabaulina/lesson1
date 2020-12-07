print("Задание 1")
welcome = "Вы зашли на этот сайт не случайно =)"
print(welcome)
user_name = input("Как вас зовут: ")
print("Привет", user_name)
answer = input("Какое сегодня число? ")
print("А вы знаете, что число ", answer,  " на Руси было счастливым?")
print("Поздравляю, сегодня ваш день!")
print("Задание 2")
number_seconds = int(input("Введите количество секунд, которое вы желаете преобразовать: "))
hours = number_seconds // 3600
minuits = (number_seconds - hours * 3600) // 60
seconds = number_seconds - hours * 3600 - minuits * 60
print("Это получается  " , hours , " ч. " ,  minuits , "мин. " ,seconds , "сек.")
print("Задание 3")
number = (input("Введите цифру "))
result = int(number) + int(str(number + number)) + int(str(number + number + number))
print("Сумма : ", result)
print("Задание 4")
number = list(input("Введите любое число : "))
m = max(number)
print("Максимальное число : ", m)
print("Задание 5")
gain = int(input("Введите выручку вашей фирмы за месяц, руб: "))
cost = int(input("Введите издержки вашей фирмы за месяц, руб: "))
if gain > cost:
    print("Поздравляю! Вы прибыльны!")
    profi = gain - cost
    print("Ваша рентабельность = ", profi, "руб.")
    worker = int(input("Введите количество сотрудников: "))
    worker_one = profi // worker
    print("Прибыль фирмы в рассчете на одного сотрудника, руб : ", worker_one)
else:
    print("Вы убыточны =(( ")
profi = 0
print("Задание 6")
normal = int(input("Введите количество километров в первый день: "))
final = int(input("Введите сколько нужно пробежать в итоге: "))
last_day = normal
all_day = 1
print(all_day, " Км: ", normal)
while last_day < final:
    all_day+=1
    last_day = last_day + (last_day * 0.1)
    print(all_day, " Км: ", last_day)
