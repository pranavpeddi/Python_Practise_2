class Base(object):
    pass

class Derived(Base):
    pass

print(issubclass(Derived,Base))
print(issubclass(Base,Derived))

