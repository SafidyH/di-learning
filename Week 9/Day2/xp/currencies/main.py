class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f"{self.amount} {self.currency}"

    def __int__(self):
        return self.amount

    def __repr__(self):
        return f"{self.amount} {self.currency}"

    def __add__(self, other):
        if isinstance(other, Currency) and self.currency != other.currency:
            raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
        if isinstance(other, int):
            return Currency(self.currency, self.amount + other)
        if isinstance(other, Currency):
            return Currency(self.currency, self.amount + other.amount)

    def __iadd__(self, other):
        if isinstance(other, int):
            self.amount += other
        if isinstance(other, Currency) and self.currency == other.currency:
            self.amount += other.amount
        elif isinstance(other, Currency) and self.currency != other.currency:
            raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
        return self


# Testing the Currency class
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))  # Output: '5 dollars'
print(int(c1))  # Output: 5
print(repr(c1))  # Output: '5 dollars'

print(c1 + 5)  # Output: 10
print(c1 + c2)  # Output: 15

print(c1)  # Output: 5 dollars

c1 += 5
print(c1)  # Output: 10 dollars

c1 += c2
print(c1)  # Output: 20 dollars

print(c1 + c3)  # Output: TypeError: Cannot add between Currency type <dollar> and <shekel>
