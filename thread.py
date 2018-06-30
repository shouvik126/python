import threading
class messanger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.current_thread().getName())
x=messanger(name='shouvik pradhan')
y=messanger(name='sunanda maity')
z=messanger(name='ritwik pradhan')
x.start()
y.start()
z.start()