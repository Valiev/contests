class Foo:
    def __init__(self):
        self.locks = {
            1: True,
            2: True,
            3: True
        }


    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.locks[1] = False


    def second(self, printSecond: 'Callable[[], None]') -> None:
        while self.locks[1]:
            continue
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.locks[2] = False


    def third(self, printThird: 'Callable[[], None]') -> None:
        while self.locks[2]:
            continue
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        self.locks[3] = False
