# 3. uzdevums
# Izveido programmu, kas nosaka vai lietotāja ievadītais skaitlis ir pāra vai nepāra.

num = int(input("Ievadi skaitli: "))

if num % 2 == 0:
    print("Pāra skaitlis")
else:
    print("Nepāra skaitlis")