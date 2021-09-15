from number_to_text import NumberToText
from time import time

ntt = NumberToText()
print(len(ntt))

try:
    while True:
        string = input('Enter input: ')
        start = time().real
        result = ntt.convert(string)
        end = time().real
        print(f'\t{result} ({(end-start)*1000} ms)')
except EOFError:
    pass

