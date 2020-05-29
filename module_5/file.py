with open("my_file.txt", encoding="utf-8") as file:
    text = file.read()

words = 0
words_with_comma = 0

for word in text.split(" "):
    if "," in word:
        words_with_comma += 1
    words += 1

print("Общее количество слов: " + str(words) + ". Количество слов с запятой: " +
      str(words_with_comma) + ". Процент слов с запятой в тексте: " +
      str(words * words_with_comma / 100))
