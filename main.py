#1.
x = []
x = list(x)
for x in range(2,21,2):
    print(x)

#2.

ls = [1,2,3,4,5]
res = sum(ls)
print(f"jami tolia {res}is")

#3.

ls = [1,2,3,4,5,6,7,8,9,10,11]
for ls in range(1,12,3):
    print(ls)

#4.

ls = [1,2,3,4,3,4,2,1,5]
ls = list(set(ls))
ls.sort()
print(ls)

#1.

x = "woah kenny,thats a wocky slush"
res = x[::-1]
print(res)

#2.

ls = [20,10,10,20,10,40,30,40,50]
res = list(set(ls))
res.sort()
print(res)

#3.


dic = {
    "a": 65,
    "b": 66,
    "c": 67,
    "d": 68
}

res = {value: key for key,value in dic.items()}

print(res)

#4.


my_list = [10,20,60,30,20,40,30,60,70,80]

res = set()

duplicates = []

for item in my_list:
    if item in res:
        duplicates.append(item)
    else:
        res.add(item)

print("dublicates are:", duplicates)

#5.

n = 5
for i in range(1,n+1):
    for j in range(n-i+1):
        print(i,end=" ")
    print()


