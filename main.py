NOP = int(input("number of tickets : "))
NOP_1 = NOP
BA = {}
amount = 0
while NOP > 0:
    Age = int(input("buyer's age : "))
    BA[NOP] = Age
    NOP = NOP - 1
BA_items = BA.items()
for NB, age in BA_items:
    if 18 <= age <= 25:
        amount = amount + 990
    elif 25 < age:
        amount = amount + 0
    elif age < 25:
        amount = amount + 1390
if NOP_1 >= 3:
    amount = amount - amount * 0.1
amount = str(amount)
print ('amount to be paint' + (amount))

