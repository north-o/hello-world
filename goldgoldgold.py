price = eval(input("What is the price of the gold? "))
howmany = eval(input("How many does the customer want? "))

pricewithouttax = price*howmany
doingtax = pricewithouttax*0.05
pricewithtax = doingtax+pricewithouttax

print ("Price without tax is",pricewithouttax)
print ("Price with tax is price",pricewithtax)