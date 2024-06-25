import sys
informations=[]
x=input("Type input to write and print to show the list: ")
if x=="input":
    name=input("person's name is: ").title()
    prename=input(f"{name}'s given name is:  ").title()
    city=input(f"{name} {prename} lives in: ").title()
    hood=input(f"{name} {prename} lives in {city}, and the hood is: ").title()

    with open("info.csv", "a") as file:
    #the file will automatically closed as soon as the calling command close.
    #w refers to write/overwrite in the file.
    #a refers to append/add to the file.
    #r refers to read-only the file.
        file.write(f"{name},{prename},{city},{hood} \n")
elif x=="print":

    with open ("info.csv") as file:
        for line in file:
            name,prename,city,hood=line.rstrip().split(",")
            information={}
            information["name"]=name
            information["prename"]=prename
            information["city"]=city
            information["hood"]=hood
            informations.append(information)
            print(f"{information['name']} {information['prename']} lives in {information['hood']},{information['city']}.")
  
  
#if you haven't noticed yet, i just made a new .csv file which is used to store multiple pieces of information in the same file, it is very commonly used when you #use something like microsoft excel, apple numbers or google spreedsheets and you want to export the data to share with someone else as a csv file or conversly if you #want to import a csv file into your preferred spreedsheet software like excel or numbers or google spreedsheets you can do that as well so csv is a vey simple #text format that just seperates values with commas and different types of values ultimately with new lines as well.
else:
    print("invalid input, you should type input to add or print to show.")
    sys.exit()