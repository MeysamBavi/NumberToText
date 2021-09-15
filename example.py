from digit_set import DigitSetConverter
from set_connector import SetConnector
from time import time

dsc = DigitSetConverter()
sc = SetConnector(dsc)
print(len(sc))

print('Enter input:')
try:
    while True:
        string = input()
        start = time().real
        result = sc.convert(string)
        end = time().real
        print(f'\t{result} in {(end-start)*1000} ms')
except EOFError:
    pass

