with open("wifi.dat", encoding='utf-8') as file:
    lines = file.readlines()

total = 0
for line in lines:
    total += int(line)

print(f"total = {total}")
