class Parent():
    def last_name(self):
        print('Pradhan')
class Child(Parent):             #inheriting the Parent class
    def first_name(self):
        print('Shouvik')
    def last_name(self):     #overriding of parent function
        print('Maity')
obj=Child()
obj.first_name()
obj.last_name()