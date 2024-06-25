First_Name=input("what's your First name? ").capitalize()
Last_Name=input("what's your Last name? ").capitalize()
with open("names.txt", "a") as file:
    #the file will automatically closed as soon as the calling command close.
    #w refers to write/overwrite in the file.
    #a refers to append/add to the file.
    #r refers to read-only the file.
    file.write(f"{First_Name},{Last_Name} \n")

