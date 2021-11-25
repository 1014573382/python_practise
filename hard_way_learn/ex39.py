# create a mapping of province to Abbreviation(简称)
provinces = {
    '甘肃': '甘',
    '河北': '冀',
    '河南': '豫',
    '山西': '晋',
    '安徽': '皖',
    '贵州': '黔'
}

# create a mapping of province and its capital
capitals = {
    '甘': '兰州',
    '冀': '石家庄',
    '豫': '郑州',
    '晋': '太原',
    '皖': '合肥',
    '黔': '贵阳'
}

print("The abbreviation of Gansu：", provinces['甘肃'])

print("The capital of Gansu province: ", capitals['甘'])
print("The capital of Gansu province: ", capitals[provinces['甘肃']])

for province, abbrev in list(provinces.items()):
    print(f"{province} is abbreviated {abbrev}.")

print("---------------------------------\n")

for abbrev, capital in capitals.items():
    print(f"{abbrev} has the capital {capital}.")

print("---------------------------------\n")

for province, abbrev in list(provinces.items()):
    print(f"{province} is abbreviated {abbrev}.")
    print(f"and has capital {capitals[abbrev]}")

print('-' * 40)

print("provinces.items()的结果：", provinces.items())
print("-----------------------------------\n")
print("list(provinces.items())的结果：",list(provinces.items()))

print("---------------------------------\n")
# 获取一个默认的简称
province = provinces.get('四川', '蜀')
print(f"The abbreviation of '四川' is {province}")
