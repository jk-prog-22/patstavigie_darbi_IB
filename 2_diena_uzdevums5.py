# 5.uzdevums
# Izveido gāzes kalkulatoru. Lietotājs ievada pateriņu (kWh) programma izvada cik ir jāmaksā.

paterins = float(input("Ievadi savu gāzes patēriņu (kWh) :"))
paterins_round = float"{:.2f}".format(paterins)
tarifs_1 = 0.1045819 
tarifs_2 = 0.0548696
tarifs_3 = 0.0394548
tarifs_4 = 0.0487234



if paterins <= 2635:
    print("Jums jāmaksā: ", paterins * tarifs_1, paterins_round)
if paterins <= 5269:
    print("Jums jāmaksā: ", paterins * tarifs_2)
if paterins <= 63227.9:
    print("Jums jāmaksā: ", paterins * tarifs_3)
if paterins <= 263450:
    print("Jums jāmaksā: ", paterins * tarifs_4)
