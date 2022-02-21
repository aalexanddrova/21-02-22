list=[ ]
N = int(input("cik bija cilveku: "))
for i in range(N):
  mass=int(input("kada in vinu masa: "))
  list.append(mass)
listsum=sum(list)
print(listsum)
listavg=sum(list)/len(list)
print(listavg)
if listsum > 300:
  print("vini nedrikst braukt visi kopa")
else:
  print("vini drikst braukt visi kopa")