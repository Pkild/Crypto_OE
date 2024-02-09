message = '1111000001'
key = "00110"
encryption = lambda a, b: a ^ b
message = list(message)
key = list(key)
print(message, key)
encrypted_message = encryption(message, key)