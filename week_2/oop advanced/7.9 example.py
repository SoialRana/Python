class MyClass:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def sum(self):
        return self.a + self.b + self.c

    def factorial(self):
        result = 1
        for i in range(1, self.b + 1):
            result *= i
        return result

obj = MyClass(2, 4, 6)
total = obj.sum()
print("Sum:", total)
# Call the factorial() method
fact = obj.factorial()
print("Factorial of b:", fact)