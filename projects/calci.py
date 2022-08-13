
class Calci(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a+self.b
    def subract(self):
        return self.a-self.b

    def multiply(self):
        return self.a * self.b
    
    def division(self):
        return self.a / self.b

# obj = Calci(a=10, b=20)
# print(obj.add(), obj.subract())
