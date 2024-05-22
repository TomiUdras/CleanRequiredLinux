s = None
my_dict = {}

while True:
  s = input().split(': ')
  if 'СТОП' in s:
    break
  my_dict[s[0]] = [float(value) for value in s[1].split(', ')]

names = input().split(', ')
final = []
for name in names:
  if name.split('-')[0] in my_dict:
    values = my_dict[name.split('-')[0]]
    calories = int(
        name.split('-')[1]) * (values[0] * 4 + values[1] * 9 + values[2] * 4)
    final.append([
        f"Продукт: {name.split('-')[0]}, калорийность: {calories}", values[0]
    ])

final.sort(key=lambda x: x[1])
for item in final:
  print(item[0])
