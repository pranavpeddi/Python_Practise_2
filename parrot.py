class Parrot:
    number=0
    name="pranav"

def Main():
    me=Parrot()
    me.number=1337
    me.name="naagu"
    print(me.name+""+str(me.number))

if __name__=='__main__':
    Main()