with open('utf-8', 'r', encoding='utf-8')as file:
    content1 = file.read()

with open('windows-1251', 'r', encoding='windows-1251')as file:
    content2 = file.read()

with open('utf-8', 'w', encoding='utf-8')as file:
    file.write(content1 + 'мир!')

with open('windows-1251', 'w', encoding='windows-1251')as file:
    file.write(content2 + 'мир!')

