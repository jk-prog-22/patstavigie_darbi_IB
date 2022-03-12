# 1. uzdevums
# Izveido programmu, kurā tu ievadi mēneša nosaukumu
# (Marts, Maijs utt.), un izvadē tiek parādīts cik dienas ir šajā mēnesī.


month = str(input("Ievadi mēnesi:"))

if month == "Janvāris":
    print("Janvārī ir 31 diena")
elif month == "Februāris":
    print("Februārī ir 28 dienas")
elif month == "Marts":
    print("Martā ir 31 diena")
elif month == "Aprīlis":
    print("Aprīlī ir 30 dienas")
elif month == "Maijs":
    print("Maijā ir 31 diena")
elif month == "Jūnijs":
    print("Jūnijā ir 30 dienas")
elif month == "Jūlijs":
    print("Jūlijā ir 31 diena")
elif month == "Augusts":
    print("Augustā ir 31 diena")
elif month == "Septembris":
    print("Septembrī ir 30 dienas")
elif month == "Novembris":
    print("Novembrī ir 30 dienas")
elif month == "Decembris":
    print("Decembrī ir 31 diena")
else:
    print("Šāds mēnesis nav atrasts ", month)





