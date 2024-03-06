message = "Помпиду"
p = 197
q = 137
c = 8467

code = "569644650331249058481576"
opened = (1483, 6499)
closed = (3811, 6499)

ord_first = 192
letters = [chr(ord("А")+i) for i in range (32)] + [chr(ord("а")+i) for i in range (32)]


#Task 1
N = p*q
d=1
while (c*d) % ((p-1)*(q-1)) != 1:
    d+=1
print("Task 1 answers:", end='\n\t')
print("d =", d, end='\n\t')
print("N =", N, end='\n\t')


message = [letters.index(m)+ord_first for m in message]
print("Message: ", *message, sep='', end='\n\t')


print("Encrypted text: ", end='')
for elem in message:
    tmp = elem ** c 
    tmp = tmp % N
    tmp = str(tmp)
    for i in range (len(tmp), 5):
        print('0', end='')
    print(tmp, end='')

print()
#Task 2
code = [code[i:i+4] for i in range(0, len(code), 4)]
ans=""
for elem in code:
    elem = int(elem)
    ans += letters[((elem**closed[0])%closed[1]) - ord_first]
print("Task 2:\n\t Answer:", ans)
