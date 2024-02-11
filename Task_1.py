alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alphabet_numbers = dict((alphabet[i], i) for i in range(len(alphabet)))  # creating alphabet as a dict of pairs letter: position

key1 = 'задел'  # print key for 1 question
message1 = 'самосборка'  # print message for 1 question

for i in range(len(message1)):
    print(alphabet[(alphabet_numbers[message1[i]] + alphabet_numbers[key1[i % len(key1)]]) % len(alphabet)], end='')

key2 = 'задел'  # print key for 2 question
message2 = 'щаруцшуцпл'  # print message for 2 question

print()

for i in range(len(message2)):
    print(alphabet[(alphabet_numbers[message2[i]] + len(alphabet) - alphabet_numbers[key2[i % len(key2)]]) % len(alphabet)], end='')
