class MyClass:
    def __init__(self, value):
        self.value = value
    
    def __add__(self, other):
        return (a.value + b.value)

a = MyClass(7)
b = MyClass(13)
result = a + b

print(result)  
