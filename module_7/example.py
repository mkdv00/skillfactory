# d = {"pear": "Груша"}
# try:
#     print(d["apple"])
# except KeyError:
#     print("Нет такого ключа в словаре. Допустимые ключи:", d.keys())



# try:
#     fp = open("some_file.txt")
# except FileNotFoundError:
#     print("Данный файл не существует.")
# else:
#     print("Файл найден. Продолжаем...")


# def danger(N, i, start=0):
#     return range(start, N)[i]
#
# def caution(x, y):
#     z = 0
#     try:
#         z = danger(x, y)
#     except IndexError as e:
#         print(e)
#     return z
#
# print(caution(10, 5))
# print(caution(10, 20))

# my_list = [2, 4, 6, 8]
# a, _, b, _ = my_list
# print(a, b)

# for coords in [(1, 2), (2, 5), (7, 12), (8, 2)]:
#     x = coords[0]
#     y = coords[1]
#     print(f"Мы на клетке [{x}, {y}]")

# for coords in [(1, 2), (2, 5), (7, 12), (8, 2)]:
#     x, y = coords
#     print(f"Мы на клетке [{x}, {y}]")

# for i, name in enumerate(["Кролик", "сова", "утка", "лягушка"]):
#     print(f"Животное номер {i}: {name}")

# s = "#217 кролик 2,7 3x2"
# id, name, coords, size = s.split()
# print(coords)

# s = "лебедь, и рак, и щука"
# my_list = s.split(", и ")

# my_list = ["рак", "лебедь", "щука"]
# print(', и '.join(my_list))
