print("Dictionary Iteration")
d = dict()

d['key1'] = "val1"
d['key2'] = 345
d['key3']='hello'
for i in d:
	print(i, d[i])

l = ["Data", "Science", "Python"]
for i in l:
	print(i)


#For loop with strings
word = "Python"
for letter in word:
    print(letter)


#For loop with range

for i in range(5):
    print(i,end=',')

#Nested loops
for i in range(3):
    for j in range(2):
        print(f"({i}, {j})")
