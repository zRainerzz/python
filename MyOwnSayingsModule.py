def main():
    salutation("World ")
    farewell("World ")


def salutation(name):
    print(f"Hello {name}. ")

def farewell(name):
    print(f"Goodbye, {name}. ")



if __name__ =="__name__":
    main()

#__name__ is a special variable automatically set by python to be quote unquote main when you run a file from the command line as by running python of MyOwnSayingsModule.py, so watch what happens now with this additional conditional in MyOwnSayingsModule.py if i run MyOwnSayingsModule.py it still works as before, because name will be automatically set to __main__ when i run this file MyOwnSayingsModule.py but notice this; name is not set to "main" it's gonna be set to something else technically the name of the module when i instead import the file like i do in MyOwnSayingsModule2.py so it will ignore the call to main function at that time because it's wrapped in that conditional in this case when i'm importing a file and not running in the command line main will not called by definition of that name's value  