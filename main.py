s = None
my_dict = {}

while True:
    s = input().split(': ')
    if 'СТОП' in s:
        break
    my_dict[s[0]] = [float(value) for value in s[1].split(', ')]

names = input().split(', ')
for name in names:
    if name.split('-')[0] in my_dict:
        values = my_dict[name.split('-')[0]]
        calories = int(name.split('-')[1]) * (values[0] * 4 + values[1] * 9 + values[2] * 4)
        print(f"Продукт: {name.split('-')[0]}, калорийность: {calories}")
