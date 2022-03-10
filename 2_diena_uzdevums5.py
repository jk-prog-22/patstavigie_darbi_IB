# 5.uzdevums
# Izveido gāzes kalkulatoru. Lietotājs ievada pateriņu (kWh) programma izvada cik ir jāmaksā.

paterins = float(input("Ievadi savu gāzes patēriņu (kWh) :"))

tarifs_1 = paterins * 0.1045819 
tarifs_2 = paterins * 0.0548696
tarifs_3 = paterins * 0.0394548
tarifs_4 = paterins * 0.0487234



if paterins <= 2635:
    print("Jums jāmaksā (EUR): " + str(round(tarifs_1, 2)))
if paterins > 2635 <= 5269:
    print("Jums jāmaksā (EUR): " + str(round(tarifs_2, 2)))
if paterins > 5269 <= 63227.9:
    print("Jums jāmaksā (EUR): " + str(round(tarifs_3, 2)))
if paterins > 63227.9 <= 263450:
    print("Jums jāmaksā (EUR): " + str(round(tarifs_4, 2)))
