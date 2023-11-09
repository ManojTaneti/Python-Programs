a = 0
b = 1
k = int(input("enter no.of values required :"))
print(b)
for i in range(1, k):
    c = a + b
    print(c)
    a, b = b, c
