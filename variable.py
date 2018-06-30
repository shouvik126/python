class Girl:
    gender='female'    #class variable
    def __init__(self,name):
        self.name=name  #instance variable which should be different for different variable
r=Girl('sunanda')
h=Girl('Ankita')
print(r.gender)
print(h.gender)
print(r.name)
print(h.name)