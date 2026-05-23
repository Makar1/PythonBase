class NegativeValueException(Exception):
    pass
class NotComparisonException(Exception):
    pass

class Currency():
    def __init__(self,name:str)->None:
        self.name = name


class Money():
    """Money - класс для денег, ведёт себя как кортеж (currency, value)

        Можно распаковать как кортеж:
            currency, value = money"""
    def __init__(self,currency: str, value: int)-> None:
        self.value = value
        self.currency = currency

    def __add__(self, other: "Money") -> "Money":
        if self.currency != other.currency:
            raise NotComparisonException
        return Money(self.value + other.value, self.currency)

    def __sub__(self, other: "Money")-> "Money":
        if self.currency != other.currency:
            raise NotComparisonException
        return Money(self.value - other.value, self.currency)

    def __eq__(self, other: "Money") -> bool:
        return self.value == other.value and self.currency == other.currency




class Wallet():
    """Wallet - класс для кошелька, ведёт себя как словарь {currency: Money}

    Можно использовать как словарь:
        wallet['rub']      # получить Money объект
        'usd' in wallet    # проверить наличие
        len(wallet)        # количество валют
        del wallet['eur']  # удалить валюту"""


    def __init__(self, *money: Money) -> None:
        self._balance = {}
        for x in money:
            self._balance[x.currency] = x

    @property
    def currencies(self):
        return self._balance


    def __getitem__(self,currency) -> Money:
        if currency in self._balance:
            return self._balance[currency]
        else:
            return Money(currency,0)


    def __delitem__(self,currency) ->None:
        if currency in self._balance:
            self._balance.pop(currency)


    def __contains__(self,currency) -> bool:
        return currency in self._balance

    def __len__(self) -> int:
        return len(self._balance)


    def add(self, money: Money)-> "Wallet":
        if money.currency in self._balance:
            self._balance[money.currency] = self._balance[money.currency] + money
        else:
            self._balance[money.currency] = money
        return self


    def sub(self,money: Money) -> "Wallet":
        if money.currency in self._balance:
            res = self._balance[money.currency] - money
            if res.value < 0:
                raise NegativeValueException
            self._balance[money.currency] =res
        return self

rub = Currency("rub")
usd = Currency("usd")


wallet = Wallet(Money("rub", 100), Money("usd", 50))
usd = wallet._balance["usd"]
print(usd.currency)
print(type(usd))
print(type(wallet))
print(wallet.currencies)
