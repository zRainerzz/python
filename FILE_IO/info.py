import sys
import csv
informations=[]
x=input("Type input to write and print to show the list: ")
if x=="input":
    prename=input("given name of then new person is:  ").title()
    name=input(f"{prename}'s last name is: ").title()
    town=input(f"{prename} {name} is from: ")
    city=input(f"{name} {prename} lives in {town}, city name is: ").title()
    hood=input(f"{name} {prename} lives in {city}, and the hood is: ").title()

    with open("info.csv", "a") as file:
    #the file will automatically closed as soon as the calling command close.
    #w refers to write/overwrite in the file.
    #a refers to append/add to the file.
    #r refers to read-only the file.
        file.write(f"{name},{prename},{town},{city},{hood} \n")
elif x=="print":

    with open ("info.csv") as file:
        #reader's purpose in life is to read csv files for me and figure out where are commas or quotes, where are the potential corner cases and just deal with them for me...
        #we can use it instead, but i don't have to at the moment. here's the input as example reader=
        for line in file:
            prename,name,town,city,hood=line.rstrip().split(",")
            information={"prename":prename,"name":name,"town":town,"city":city,"hood":hood}
            informations.append(information)
            print(f"{information['name']} {information['prename']} is from {town}, he lives in {information['hood']},{information['city']}.")
  
  
#if you haven't noticed yet, i just made a new .csv file which is used to store multiple pieces of information in the same file, it is very commonly used when you #use something like microsoft excel, apple numbers or google spreedsheets and you want to export the data to share with someone else as a csv file or conversly if you #want to import a csv file into your preferred spreedsheet software like excel or numbers or google spreedsheets you can do that as well so csv is a vey simple #text format that just seperates values with commas and different types of values ultimately with new lines as well.
else:
    print("invalid input, you should type input to add or print to show.")
    sys.exit()