#11.Modulo
#1.You're trying to divide a group into four teams. All of you count off, and you get number 27.
#    Find out your team by computing 27 modulo 4. Save the value to my_team.
#2.Print out my_team. What number team are you on?
#3.Food for thought: what number team are the two people next to you (26 and 28) on? What are the numbers for all 4 teams?

my_team = 27%4
print(my_team)
team_26 = 26%4
team_28 = 28%4
team_29 = 29%4
print("my team is "+ str(my_team))
print("team for 26 is "+ str(team_26))
print("team for 28 is "+ str(team_28))
print("team for 29 is "+ str(team_29))

#Project to make customer reciepts

storeName = "Lovely Loveseats for Neat Suites on Fleet Street"
lovelyLoveseatDescription = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
lovelyLoveseatPrice = 254.00
stylishSetteeDescription = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
stylingSetteePrice = 180.50
luxuriousLampDescription = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
luxuriousLampPrice = 52.15
salesTax = .088
customerOneTotal = 0
customerOneItemization = ""
customerOneTotal += lovelyLoveseatPrice
customerOneItemization += lovelyLoveseatDescription + """
"""
customerOneTotal += luxuriousLampPrice
customerOneItemization +=  luxuriousLampDescription + """
"""
customerOneTax = customerOneTotal*salesTax
customerOneTotal += customerOneTax
print("Customer One Items")
print(customerOneItemization)
print("Customer One Total")
print(customerOneTotal)