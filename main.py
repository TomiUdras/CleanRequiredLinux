s = None
my_dict = {}
while (True):
  s = input().split(': ')
  if 'СТОП' in s:
    break
  my_dict[s[0]] = s[1].split(', ')

names = input().split(', ')
for name in names:
  if name.split('-')[0] in my_dict:
    values = my_dict[name.split('-')[0]]
    print(
        f"Продукт: {name.split('-')[0]}, калорийность: {int(name.split('-')[1])*(int(values[0])*4 + int(values[1])*9 + int(values[2])*4)}"
    )
