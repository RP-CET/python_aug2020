
#
#Watermelon       $  5.00
#Apples           $  14.00
#

items = ["Watermelon", "Apples", "Mangos"]
prices = [5.00, 14.00, 140.33]


for i in range(len(items)  ):
    entry = "%-35s $%10.2f" % (items[i], prices[i])
    print(entry)

print ("-"*50)

total = sum(prices)
entry = "%-35s $%10.2f" % ("Total" , total)
print(entry)

