
class Wallet():
    __slots__= ( "_balance", "_valute")

    def __init__(self,_balance :int,_valute: str)-> None:
        if  not isinstance(_balance, (int, float)):
            raise TypeError("должен быть числом")
        if _balance < 0:
            raise ValueError("Баланс должен быть положительным")

        self._balance = _balance
        self._valute = _valute



    def get_balance(self):
        return (f"{self._balance} {self._valute}")

    def set_balance(self, _balance: int) -> int:
        self._balance = _balance
        print("Баланс изменен!")

    def move_money(self, money: int) -> None:
        print("Деньги сняты")
        self._balance = self._balance - money

