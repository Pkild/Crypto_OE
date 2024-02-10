message = '11110001100111011011'
k_1 = '1001110111'
k_2 = '1010100100'


def feistel(msg, k):
    msg_l = msg[:len(msg) // 2]
    msg_r = msg[len(msg) // 2:]
    return msg_r + f"{int(msg_l, 2) ^ int(k, 2) ^ int(msg_r, 2):0>{len(k)}b}"


print(feistel(feistel(message, k_1), k_2))
