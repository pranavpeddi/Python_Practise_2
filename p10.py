class India():
    def capital(self):
        print("New Delhi is the capital of India")

    def language(self):
        print("Hindi is most widely spoken language")

    def type(self):
        print("India is developing country")


class Usa():

    def capital(self):
        print("Washington dc is the capital of USA")

    def language(self):
        print("English is the primary langunage")

    def type(self):
        print("USA is a developed country")

on_ind=India()
on_usa=Usa()

for country in(on_ind,on_usa):
    country.capital()
    country.language()
    country.type()