
class Formatter:
    def __init__(self, default_joiner=',', last_joiner='and', space=' '):
        self.default_joiner = default_joiner
        self.last_joiner = last_joiner
        self.space = space

    def format(self, iterable):

        if not iterable:
            return ''

        list_ = list(iterable)
        last_item = list_.pop()
        result = (self.default_joiner + self.space).join(list_)
        return (self.space + self.last_joiner + self.space).join([result, last_item]) if result else last_item

    def stick_last_two(self, iterable):
        if len(iterable) < 2:
            return self.format(iterable)

        list_ = list(iterable)

        last_two = self.space.join(reversed((list_.pop(), list_.pop())))
        list_.append(last_two)

        return self.format(list_)
