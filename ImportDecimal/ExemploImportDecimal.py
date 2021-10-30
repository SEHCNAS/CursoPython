
from decimal import Decimal, getcontext

print(Decimal(1) / Decimal(7))

getcontext().prec = 4  # Define a precisão do Decimal

print(Decimal(1) / Decimal(7))

# print(Decimal.max(Decimal(1) / Decimal(7)))
