import csv
import pyperclip
from datetime import date
breasts = input("How many Breasts?")
tenders = input("How many Tenders?")

if(int(breasts) > 0):
    print(breasts + " Breasts")
if(int(tenders) > 0):
    print(tenders + " Tenders")
with open("Order.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    line = 0
    for row in csv_reader:
        name = str(row[0])
        amount = int(row[1])
        if(amount > 0):
            print(str(amount) + " " + name)
            

order = input("Are you happy with this order? Y/N ")
if(order == "Y"):
    title = date.today().strftime("%b-%d-%Y")
    output = open(title+".txt","w")
    if(int(breasts) > 0):
        output.write(breasts + " Breasts\n")
    if(int(tenders) > 0):
        output.write(tenders + " Tenders\n")
    with open("Order.csv") as csv_file:
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            name = str(row[0])
            amount = int(row[1])
            if(amount > 0):
                output.write(str(amount) + " " + name + "\n")
    output.close()
    cpy = input("Do you want to send order to Sarah? Y/N ")
    if(cpy == "Y"):
        file = open(title+".txt", "r")
        data = file.read()
        pyperclip.copy(data)
        file.close()

