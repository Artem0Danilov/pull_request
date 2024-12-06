utf_8 = open("utf-8.txt", "r", encoding="utf-8")
win_1251 = open("windows-1251.txt", "r", encoding="windows-1251")

print(f"до: utf-8: {utf_8.read()}, win-1251: {win_1251.read()}")

utf_8.close()
win_1251.close()

utf_8 = open("utf-8.txt", "a", encoding="utf-8")
win_1251 = open("windows-1251.txt", "a", encoding="windows-1251")

utf_8.write(" world!")
win_1251.write(" world!")


utf_8.close()
win_1251.close()

utf_8 = open("utf-8.txt", "r", encoding="utf-8")
win_1251 = open("windows-1251.txt", "r", encoding="windows-1251")

print(f"до: utf-8: {utf_8.read()}, win-1251: {win_1251.read()}")

utf_8.close()
win_1251.close()
