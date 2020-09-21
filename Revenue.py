
s="HackerRank.com presents Pythonist 2"
newstring=""


for i in s:
    if(i.islower()):
        newstring+=i.upper()
    else:
        newstring+=i.lower()

print(newstring)