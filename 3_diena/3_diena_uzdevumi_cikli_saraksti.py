# 1. uzdevums
#Izdrukāt visas valstis vienā rindiņā. valstis = ['Latvija','Lietuva','Igaunija']

valstis = ["Latvija", "Lietuva", "Igaunija"]

for valsts1 in valstis:
    print(valsts1, end=" ")

# print(valstis[0], valstis[2], valstis[3])
print()

print("==============================================")
# 2. uzdevums
# Izdrukāt skaitļus no 50 līdz 25. (ievēro secību!)

for i in range(50, 25, -1):
    print(i, end = " ")


print("==============================================")
# 3. uzdevums
# Saskaiti visus skaitļus intervālā no 10 - 29, kas dalās ar 3.
sum = 0
for i in range(10, 29):
    if i % 3 == 0:
        sum = sum + i

print("Summa ir", sum)

print("==============================================")
# 4. uzdevums
# Izveido programmu, kas izdrukā skaitļus no 1 līdz 100, bet skaitļu vietās, kas dalās ar:
# 3 tiek izdrukāts vārds "Bum",
# 5 tiek izdrukāts vārds "Rum",
# 3 un 5 tiek izdrukāts vārds "BumRum

for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        print("BumRum,", end=" ")
    elif i % 3 == 0:
        print("Bum,", end=" ")
    elif i % 5 == 0:
        print("Rum,", end=" ")        
    else:
        print(i, ",", sep="", end=" ")


print("==============================================")
# 6. uzdevums
# Izveido programmu, kas izdrukā zemāk esošo piemēru. Jāizmanto cikls-ciklā.

for cipari in range(10):
    for i in range(cipari):
        print(cipari, end=" ")
    print()


print("==============================================")
# 7. uzdevums
# Izveido programmu, kas izdrukā zemāk esošo piemēru. Jāizmanto cikls-ciklā.
rindas = 5
for i in range(0, rindas):
    for j in range(0, i + 1):
        print("*", end=' ')
    print()

for i in range(rindas, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print()


