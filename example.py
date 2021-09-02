from digit_set import DigitSetConverter
from time import time

dsc = DigitSetConverter()

print('Enter input:')
try:
    while True:
        string = input()
        start = time().real
        result = dsc.raw_convert(string)
        end = time().real
        print(f'\t{result} in {end-start} ms')
except EOFError:
    pass

