if 1 > 2:
    print("hello")
elif 3 == 3:
    print("elif ran")
else:
    print("last")

seq = [1, 2, 3, 4, 5, 6, 7]

for item in seq:
    print(item)

mypairs = [(1, 2), (3, 4)]

for (tup1, tup2) in mypairs:
    print(tup1, tup2)


for item in range(10):
    print(item)


x = [1, 2, 3, 4]

out = [num**2 for num in x]
print(out)
