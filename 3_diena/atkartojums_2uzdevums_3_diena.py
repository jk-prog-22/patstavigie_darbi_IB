# 2. uzdevums
# Izveido programmu, kas aprēķina suņa vecumu - suņa gados. 
# 1 cilvēka gads ir 4 suņa gadu, bet pirmie 2 ir vienādi ar 10.5 gadiem.

cilveku_gadi = int(input("Ievadi suņa vecumu cilvēka gados!"))

if cilveku_gadi <= 2:
	sunu_gadi = cilveku_gadi * 10.5
else:
	sunu_gadi = 21 + (cilveku_gadi - 2)*4

print("Suņa vecums cilvēku gados ir:", sunu_gadi)