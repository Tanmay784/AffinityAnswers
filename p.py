slurs=["nigga","nigro","chinki","ching","chong","chingchong","nigra"]
n=int(input("enter the number of lines "))
lines=[]
count=0
levels=[]
# lines=[["hello","my","nigga"],["nigga","nigro"]]
for i in range(n):
    i=input().split()
    lines.append(i)
for i in lines:
    for j in i:
        if j in slurs:
            count+=1
    levels.append(count)
    count=0
for i in range(n):
    print(f"the sentence {i} wrong level is {levels[i]}")