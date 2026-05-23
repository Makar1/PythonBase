class Fibo:
    def __init__(self, n: int):
        self.n = n
        self.count = 0
        self.a = 0  # текущее значение
        self.b = 1  # следующее значение

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration

        result = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return result


fibo = Fibo(20)
for x in fibo:
    print(x, end=" ")


