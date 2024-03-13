import numpy as np
from PIL import Image


d = 197
p = 71
q = 137
mod = 256


ord_first = 192
symbols = [chr(ord("А")+i) for i in range (32)] + [chr(ord("а")+i) for i in range (32)]
symbols = dict((i+ord_first, symbols[i]) for i in range(len(symbols)))
symbols[32] = " "
symbols[10] = "\n"

array_remainders = np.array(Image.open('array_remainders.png'))
array_int_parts = np.array(Image.open('array_int_parts.png'))
array_numbers = array_int_parts * mod + array_remainders

for array in array_numbers:
    for symbol in array:
        print(symbols[(int(symbol)**d)%(p*q)], end="")

#Find the author of the output text. for me it was "пушкин"
