from digit_set import DigitSetConverter
from number_to_text import NumberToText
from time import time

dsc = DigitSetConverter()
ntt = NumberToText(dsc)
print(len(ntt))

print('Enter input:')
try:
    while True:
        string = input()
        start = time().real
        result = ntt.raw_convert(string)
        end = time().real
        print(f'\t{result} in {(end-start)*1000} ms')
except EOFError:
    pass

