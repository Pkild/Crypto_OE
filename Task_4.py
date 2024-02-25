#part 1 input
reg = [1, 0, 1, 0, 0, 0]
moved = [5, 4, 3]

#part 2 input
key = [11,4,10,3,5,0,2,1,9,8,7,6]
n = 5


ans = []

reg_copy = reg.copy()

i = 0
while (i == 0) or (reg_copy != reg):
    i += 1
    tmp = 0
    for elem in moved:
        tmp = (tmp + reg_copy[len(reg)-elem]) % 2
    ans.append(reg_copy[-1]) 
    reg_copy = [tmp] + reg_copy[:len(reg_copy)-1]
print("Task 1 answers:")
print('\t', i, end='\n\t', sep='')
print(*ans[::-1], sep=',', end='\n\n')


N = len(key)

S = [i for i in range(N)]
j = 0
for i in range (N):
    j = (j + S[i] + key[i % len(key)]) % N
    S[i], S[j] = S[j], S[i]

i, j = 0, 0

ans = []

print("Task 2 answers:\n\t", end='')
print(*S, sep=',', end='\n\t')

for k in range (n):
    i = (i + 1) % N
    j = (j + S[i]) % N
    S[i], S[j] = S[j], S[i]
    ans.append(S[(S[i] + S[j]) % N])

print(*ans[::-1], sep=',')