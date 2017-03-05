def my_for(iterable, callback):
    it = iter(iterable)
    while True:
        try:
            value = next(it)
            callback(value)
        except StopIteration:
            break


def loop(value):
    print('Next value received:', value)


my_for(range(10), loop)


class SimpleIterable:
    def __getitem__(self, index):
        if 0 <= index <= 5:
            return index * 2
        else:
            raise IndexError


iterable = SimpleIterable()
for value in iterable:
    print(value)

