import re
url=input("URL: ").strip()

username=re.sub(r"^(https?://)?(www\.|)twitter\.com","",url    )
#username=url.removeprefix("https://twitter.com/","")
#prefix is a string that comes at the start of another, so if i remove prefix i wont need another argument for this function.

#username=url.replace("https://twitter.com/","")
#you pass 2 arguments in replace, what do you want to replace and what do you want to replace it with
print(f"Username: {username}")