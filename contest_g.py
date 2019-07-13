import re

str = input()

letters = len(re.findall(r'[A-Z]', str))
numbers = 0
for i in re.findall(r'[0-9]+', str):
    numbers += int(i)
numbers = numbers - len(re.findall(r'[0-9]+', str))

print(letters + numbers)
