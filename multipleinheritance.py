class Mario():
    def move(self):
        print('I am moving')
class Shroom():
    def eat_shroom(self):
        print('Now i am big')
class BigMario(Mario,Shroom):
    pass  #when we dont want to define anything on the function
bm=BigMario()
bm.move()
bm.eat_shroom()