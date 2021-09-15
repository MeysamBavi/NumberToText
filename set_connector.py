from digit_set import DigitSetConverter
from formatter import Formatter


class SetConnector:
    def __init__(self, digit_set_object=DigitSetConverter(), formatter=Formatter()):
        self.digit_set_object = digit_set_object
        self._formatter = formatter

    _sets_multiplier = {
        1: 'thousand',
        2: 'million',
        3: 'billion',
        # 4: 'trillion',
        # 5: 'quadrillion',
        # 6: 'quintillion',
        # 7: 'sextillion',
        # 8: 'septillion',
        # 9: 'octillion',
        # 10: 'nonillion',
        # 11: 'decillion',
        # 12: 'undecillion',
    }

    def __len__(self):
        return max(self._sets_multiplier.keys()) * len(self.digit_set_object) + len(self.digit_set_object)

    def raw_convert(self, value):

        num_length = len(value)
        set_length = len(self.digit_set_object)
        values = [value[max(0, num_length - set_length - i):num_length - i] for i in range(0, num_length, set_length)]

        result = []
        for i in range(len(values)-1, -1, -1):
            digit_set = self.digit_set_object.raw_convert(values[i])

            result.extend(digit_set)

            multiplier = self._sets_multiplier.get(i)
            if multiplier and digit_set:
                result.append(multiplier)

        return result

    def half_raw_convert(self, value):

        num_length = len(value)
        set_length = len(self.digit_set_object)
        values = [value[max(0, num_length - set_length - i):num_length - i] for i in range(0, num_length, set_length)]

        result = []
        for i in range(len(values) - 1, -1, -1):
            digit_set = self.digit_set_object.convert(values[i])
            multiplier = self._sets_multiplier.get(i)

            if multiplier and digit_set:
                result.append(digit_set + self._formatter.space + multiplier)
            elif digit_set:
                result.append(digit_set)

        if not result:
            result.append(self.digit_set_object.zero)
        return result

    def convert(self, value):
        return self._formatter.format(self.half_raw_convert(value))

    