import re


def _check_type(arg):
    if not isinstance(arg, str) and not isinstance(arg, int):
        raise TypeError('Argument must be integer or string')
    if isinstance(arg, str):
        result = re.search(r'^\d+$', arg)
        if result is None:
            raise TypeError('The passed string is not a decimal number.')
    return str(arg)


# class DigitSequence:
#     def __init__(self, value):
#         self._value = str(value)
#
#     def __getitem__(self, item):
#         i = int(item)
#         return self._value[-1-i]

class DigitSetConverter:
    def __len__(self):
        return 3

    _zero = '0'

    _digits = {
        _zero: 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
    }
    _specifics_sub = {
        **_digits,
        '10': 'ten',
        '11': 'eleven',
        '12': 'twelve',
        '13': 'thirteen',
        '14': 'fourteen',
        '15': 'fifteen',
        '16': 'sixteen',
        '17': 'seventeen',
        '18': 'eighteen',
        '19': 'nineteen',
    }

    _specific_digit_place = {
        1: {
            '2': 'twenty',
            '3': 'thirty',
            '4': 'forty',
            '5': 'fifty',
            '6': 'sixty',
            '7': 'seventy',
            '8': 'eighty',
            '9': 'ninety',
        }
    }

    _place_multipliers = {
        2: 'hundred',
    }

    def _get_specific_place(self, place, digit):
        dict_for_place = self._specific_digit_place.get(place)

        if dict_for_place is None:
            return None
        return dict_for_place.get(digit)

    def raw_convert(self, value):
        assert isinstance(value, str)
        value = value.lstrip(self._zero)
        assert len(value) <= len(self)

        result = []

        # if not value:
        #     result.append(self._digits[self._zero])
        #     return result

        for place in range(len(value)-1, -1, -1):

            digit = value[-1-place]

            if digit == self._zero:
                continue

            specific_sub = self._specifics_sub.get(value[-1-place:])
            if specific_sub is not None:
                result.append(specific_sub)
                break

            specific_place = self._get_specific_place(place, digit)
            if specific_place is not None:
                result.append(specific_place)
                continue

            result.append(self._digits[digit] + ' ' + self._place_multipliers[place])
        return result

    def __call__(self, *args, **kwargs):
        return self.raw_convert(args[0] if args else kwargs['value'])
