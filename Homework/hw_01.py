import string

drone_list = ["DJI Mavic 2 Pro", "DJI Mavic 2 Zoom", "DJI Mavic 2 Enterprise Advanced", "AUTEL Evo II Pro", "DJI Mini 2", "Autel Evo Nano", "Autel Evo Lite Plus", "Parrot Anafi", "Dji Inspire 2", "DJI Mavic 3", "DJI Mavic Air2s", "Ryze Tello", "Eachine Trashcan"]

drone_weight_list = [903, 900, 920, 980, 249, 249, 600, 540, 1500, 1000, 570, 130, 110]

#в drone по очереди попадает каждый дрон из списка drone_list
#TODO1
#выведите все дроны производителя, название которого введет пользователь через input, и подсчитайте их количество. 
#учтите, что:
#1) DJI и Dji - это один и тот же производитель! такие случаи тоже должны обрабатываться
#2) при выводе исправьте название производителя, если допущена ошибка. правильный вариант названия: DJI, Autel
user_input = input("Введите название приозводителя\n").lower()
count = 0
stop = True
while (stop):
    if isinstance(user_input, str):
        for drone in drone_list:
            if user_input in drone.lower():
                if "dji" in drone.lower():
                    drone = drone.replace(drone[0:3], drone[0:3].upper())
                elif "autel" in drone.lower():
                    first_letter = drone[0].upper()
                    drone = drone.replace(drone[0:5], drone[0:5].lower())
                    drone = drone.replace(drone[0], first_letter)
                print(drone)
                count += 1
        stop = False
    else:
        print("Введите название в корректном формате")
print("Всего дронов от этого производителя", count, "\n")


#TODO2
#подсчитайте количество моделей дронов каждого производителя из списка drone_list. производители: DJI, Autel, Parrot, Ryze, Eachine
count_dji = 0
count_autel = 0
count_parrot = 0
count_ryze = 0
count_eachine = 0

for drone in drone_list:
    if "dji" in drone.lower():
        count_dji += 1
    elif "autel" in drone.lower():
        count_autel += 1
    elif "parrot" in drone.lower():
        count_parrot += 1
    elif "ryze" in drone.lower():
        count_ryze += 1
    elif "eachine" in drone.lower():
        count_eachine += 1
print("DJI:",count_dji, "\nAutel:", count_autel, "\nParrot:", count_parrot, "\nRyze:", count_ryze, "\nEachine:", count_eachine, "\n")
#TODO3
#выведите все дроны из списка, которые нужно регистрировать (масса больше 150 г), и подсчитайте их количество. 
#сделайте то же самое для всех дронов, которые не нужно регистрировать
#для этого вам нужно параллельно обрабатывать два списка: drone_list и drone_weight_list:
#как работает zip, мы разберем на лекции про списки. пока что просто пользуйтесь
need_to_registrate = []
no_need_to_registrate = []
for drone, weight in zip(drone_list,  drone_weight_list):
    if weight > 150:
        need_to_registrate.append(drone + " " + str(weight))
    else:
        no_need_to_registrate.append(drone + " " + str(weight))
print("Нуждаются в регистрации:")
for drone in need_to_registrate:
    print(drone)
print(len(need_to_registrate))
print("\n")
print("Не нуждаются в регистрации:")
for drone in no_need_to_registrate:
    print(drone)
print(len(no_need_to_registrate))
print("\n")

#TODO4
#для каждого дрона из списка выведите, нужно ли согласовывать полет при следующих условиях:
#высота 100 м, полет над населенным пунктом, вне закрытых зон, в прямой видимости
#помните, что для дронов тяжелее 150 г согласовывать полет над населенным пунктом - обязательно!
height = 100
fly_over_locality = True
out_of_closed_area = True
vlos = True
for drone, weight in zip(drone_list, drone_weight_list):
    if height > 150 or (fly_over_locality and weight > 150) or not out_of_closed_area or not vlos:
        print(drone,":")
        print("Нужно согласовывать полёт, т. к. ")
        conditions = ""
        if height > 150:
            conditions += "/высота более 150 м/"
        if not out_of_closed_area:
            conditions += "/полёт в закрытой зоне/"
        if not vlos:
            conditions += "/полёт не в прямой видимости/"
        if (fly_over_locality and weight > 150):
            conditions += "/дрон тяжелее 150 г и пролетает над населённым пунктом/"
        print(conditions)
    else:
        print(drone,":")
        print("Согласовывать полёт не нужно")

#TODO5*
#модифицируйте решение задания TODO1:
#теперь для введенного пользователем производителя вы должны вывести строку, содержащую перечисление моделей и БЕЗ названия производителя.
#например, пользователь ввел "Autel". ваша программа должна вывести вот такой результат: "Evo II Pro, Evo Nano, Evo Lite Plus". для этого вам понадобится несколько функций работы со строками. решить эту задачу можно несколькими разными способами
#производители те же: DJI, Autel, Parrot, Ryze, Eachine

user_input = input("Введите название приозводителя\n").lower()
count = 0
stop = True
while (stop):
    if isinstance(user_input, str):
        for drone in drone_list:
            if user_input in drone.lower():
                if "dji" in drone.lower():
                    drone = drone.replace(drone[0:4], "")
                elif "autel" in drone.lower():
                    drone = drone.replace(drone[0:6], "")
                elif "parrot" in drone.lower():
                    drone = drone.replace(drone[0:7], "")
                elif "ryze" in drone.lower():
                    drone = drone.replace(drone[0:5], "")
                elif "eachine" in drone.lower():
                    drone = drone.replace(drone[0:8], "")
                print(drone)
                count += 1
        stop = False
    else:
        print("Введите название в корректном формате")
print("Всего дронов от этого производителя", count)