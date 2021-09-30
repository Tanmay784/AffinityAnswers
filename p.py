# I dislike rasism and this is purely for demonstration purpose 

# a list of slurs
slurs=["nigga","nigro","niga","chinki","ching","chong","chingchong","nigra","niger"]
n=int(input("enter the number of lines "))
lines=[]
count=0
levels=[]
# taking input and putting them in a list
for i in range(n):
    i=input().split()
    lines.append(i)
# checking each and every lines for slur words
for i in lines:
    for j in i:
        if j in slurs:
            count+=1
    levels.append(count)
    count=0
for i in range(n):
    print(f"the sentence {i} wrong level is {levels[i]}")