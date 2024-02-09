alphabet = "а, б, в, г, д, е, ё, ж, з, и, й, к, л, м, н, о, п, р, с, т, у, ф, х, ц, ч, ш, щ, ъ, ы, ь, э, ю, я".split(
    ", ")
alphabet = dict((alphabet[i], i) for i in range(len(alphabet)))  # creating alphabet as a dict of pairs letter: position


def get_key(i):  # getting letter in alphabet by it's number
    for k, v in alphabet.items():
        if v == i:
            return k
    return None


key1 = 'задел'  # print key for 1 question
message1 = 'самосборка'  # print message for 1 question

cypher = ''
for i in range(len(message1)):
    cypher += get_key((alphabet[message1[i]] + alphabet[key1[i % len(key1)]]) % len(alphabet))
print(cypher)

key2 = 'задел'  # print key for 2 question
message2 = 'щаруцшуцпл'  # print message for 2 question
decipher = ''

for i in range(len(message2)):
    decipher += get_key((alphabet[message2[i]] + len(alphabet) - alphabet[key2[i % len(key2)]]) % len(alphabet))
print(decipher)
