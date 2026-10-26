for i in range(1,11):
    print(i)

for i in range(2,51,2):
    print(i)

for i in range(10,0,-1):
    print(i)

n=5
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)

f=1
for i in range(1,n+1):
    f*=i
print(f)

for i in range(1, 11):
    print(n * i)

list=[-2,-1,0,1,2,3,4,5,6]
positiv=0
for i in list:
    if i>0:
        positiv+=1
print(positiv)

t="Привет"
glasni=0
for i in t:
    if i in "аеёиоуыэюя":
        glasni+=1
print(glasni)


largest = list[0]
for i in list:
    if i > largest:
        largest = i
print(largest)

for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end=" ")
    print()