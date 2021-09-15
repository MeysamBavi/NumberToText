from formatter import Formatter


class DigitSetConverter:
    def __len__(self):
        return 3

    def __init__(self, formatter=Formatter()):
        self._formatter = formatter

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

    def raw_convert(self, value, _indicator=None):
        assert isinstance(value, str)
        value = value.lstrip(self._zero)
        assert len(value) <= len(self)

        result = []

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

            result.append(self._digits[digit] + self._formatter.space + self._place_multipliers[place])

        if _indicator is not None:
            _indicator.should_stick_last_two = not len(result) < len(value)
        return result

    def convert(self, value):
        indicator = _FormatIndicator()
        raw = self.raw_convert(value, _indicator=indicator)
        if indicator.should_stick_last_two:
            return self._formatter.stick_last_two(raw)
        return self._formatter.format(raw)

    def __getzero(self):
        return self._digits[self._zero]

    zero = property(__getzero)


class _FormatIndicator:
    def __init__(self, should_stick_last_two=True):
        self.should_stick_last_two = should_stick_last_two

