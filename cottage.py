from pickletools import read_int4

import menu
import price

user = input("Доброго дня,Як ми до вас можемо звертатеся? :")
all_price = 0
text = ""

print("Доброго дня " + user)
print("Чи бажаєте " + menu.SYRNIKY)

porcii = int(input("Скільки порцій? :"))

all_price += porcii * price.SYRNIKY

text += (menu.SYRNIKY) + "-" + str(price.SYRNIKY) + '\n' + (menu.SYR_WITH_STROBERIES) + str(price.SYR_WITH_STROBERIES)

print("І ще можу порадити сир з полуницею")
porcii = int(input("Скільки порцій? :"))

all_price += porcii * price.SYR_WITH_STROBERIES

print(menu.SALE)

all_price = all_price - (all_price * 0.15 )

print("---------------------------------------------------------------------------------------")
print(text)
print("Загальна вартість " + str(all_price) + " грн")
print("Дата 06,12,2024")



