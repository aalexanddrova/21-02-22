listgood = [ ]
listmid = [ ]
listbad = [ ]
N = int(input("cik ir skolenu? "))
for x in range(N):
  x = int(input("ievadi visu prieksmetu videjo atzimi: "))
  if x > 8:
    listgood.append(x)
  if 3 < x < 9:
    listmid.append(x)
  if x < 4:
    listbad.append(x)
print("teicamnieku ir: ")
print(len(listgood))
print("viduveji macas: ")
print(len(listmid))
print("nesekmigo skolenu ir: ")
print(len(listbad))