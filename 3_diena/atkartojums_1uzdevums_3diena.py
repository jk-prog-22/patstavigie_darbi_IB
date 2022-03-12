# 1. uzdevums
# Izveido programmu, kurā tu ievadi mēneša nosaukumu
# (Marts, Maijs utt.), un izvadē tiek parādīts cik dienas ir šajā mēnesī.


month = str(input("Ievadi mēnesi:"))

if month.casefold() == "Janvāris".casefold():
    print("Janvārī ir 31 diena")
elif month.casefold() == "Februāris".casefold():
    print("Februārī ir 28 dienas")
elif month.casefold() == "Marts".casefold():
    print("Martā ir 31 diena")
elif month.casefold() == "Aprīlis".casefold():
    print("Aprīlī ir 30 dienas")
elif month.casefold() == "Maijs".casefold():
    print("Maijā ir 31 diena")
elif month.casefold() == "Jūnijs".casefold():
    print("Jūnijā ir 30 dienas")
elif month.casefold() == "Jūlijs".casefold():
    print("Jūlijā ir 31 diena")
elif month .casefold()== "Augusts".casefold():
    print("Augustā ir 31 diena")
elif month .casefold()== "Septembris".casefold():
    print("Septembrī ir 30 dienas")
elif month .casefold()== "Novembris".casefold():
    print("Novembrī ir 30 dienas")
elif month.casefold() == "Decembris".casefold():
    print("Decembrī ir 31 diena")
else:
    print("Šāds mēnesis nav atrasts ", month)





