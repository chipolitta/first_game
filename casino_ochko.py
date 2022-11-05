import random as unicorn

dumpster = [*range(6, 10), *[10] * 4, 11] * 4
unicorn.shuffle(dumpster)
print('Игра в очкоооо нааааачинааааетсяяяя!!!\n'
      'Крутите барабан!\n'
      'Пиши да или нет - брать карту или не брать.\n'
      'Если выбираешь нет - игра over, если да - у тебя есть шанс выиграть, но это не точно - ты играешь в русскую рулетку - выиграть можно, только набрав суммарно 21 очко! '
      'У тебя только одна попытка, от удачи зависит твое будущее!\n'
      'Поехали!!!\n'
      'да или нет?\n')
belly = 0
for action in iter(input, "нет"):
    food = dumpster.pop()
    if (belly + food > 21
            and food == 11): food = 1
    print("Карта: ", food)
    belly += food
    if belly >= 21: break

if belly > 21:
    casino_result = "Ты проиграл"
    print(casino_result)
elif belly == 21:
    casino_result = "Ты выиграл"
    print(casino_result)
else:
    print(f"Ты набрал {belly} очков")

