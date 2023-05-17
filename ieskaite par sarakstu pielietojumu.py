import random 
eriks = 20 + 3 + 2006

kozeris = []
for i in range (eriks):
    kozeris.append(random.randrange(-250, 250))

print(kozeris(; ))

pozitivie = 0
negativie = 0

for i in range(eriks):
    if kozeris[i] >= 0:
        pozitivie += 1
    elif kozeris[i] < 0:
        negativie += 1
    i += 1

print("Negativo skaitlu skaits = ", negativie, "Pozitivo skaitlu skaits = ", pozitivie,)

paraskaitļi = 0
neparaskaitļi = 0

for i in range(eriks):
    if kozeris[i]%2 == 0:
        paraskaitļi += 1
    else:
        neparaskaitļi += 1
    i +=1

print("Para skaitlu skaits = ", paraskaitļi, "Nepara skaitlu skaits = ", neparaskaitļi)


videjaisaritmetiskais = 0

for i in range(eriks):
    videjaisaritmetiskais += kozeris[i]
    i += 1

print("Vidējais aritmētiskais =",videjaisaritmetiskais/eriks)

divcipars = 0
for i in range(eriks):
     if kozeris[i] >= -99 and kozeris[i] < -9:
         divcipars += 1
     elif kozeris[i] >= 10 and kozeris[i] < 100:
         divcipars += 1
     i +=1

print("izvaditie skaitli divcipari ", divcipars)
 



