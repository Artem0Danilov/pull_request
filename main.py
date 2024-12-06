import os


# Функция для добавления строки в файл с определением кодировки
def append_to_file(filename, text):
    # Определяем кодировку файла
    with open(filename, 'rb') as f:
        raw_data = f.read()

    # Пробуем декодировать с разных кодировок
    for encoding in ['utf-8', 'windows-1251']:
        try:
            decoded_data = raw_data.decode(encoding)
            # Если декодирование прошло успешно, записываем текст
            with open(filename, 'a', encoding=encoding) as f:
                f.write(text)
            print(f'Добавлено в {filename} с кодировкой {encoding}')
            return
        except UnicodeDecodeError:
            continue


# Список файлов
files = ['utf-8.txt', 'utf-32.txt', 'windows-1251.txt']

# Текст для добавления
text_to_append = 'мир!'

# Обработка каждого файла
for file in files:
    append_to_file(file, text_to_append)