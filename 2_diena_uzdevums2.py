# 2. uzdevums
#Uzrakstiet programmu, kas prasa lietotājam ievadīt savu vārdu, ja tas ievada vārdu, Bond, tad izdrukājiet uz ekrāna "Esi sveicināts 007",
#ja cits tad "Esi sveicināts, VARDS", kur VARDS ir lietotāja ievadītais vārds.

vards = (input("Kā Jūs sauc?"))

print("Esi sveicināts, 007!") if vards == "Bond" else print("Esi sveicināts/a,", vards)