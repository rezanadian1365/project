# PayPul
# with use of ABC and abstractmethod
from abs import ABC, abstractmethod


class PayPal(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass
