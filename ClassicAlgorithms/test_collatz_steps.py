from collatz_steps import *
from nose.tools import *

class Collatz_steps_tests():
    def __init__(self):
        pass

    def collatz_steps_uncorrect_input(self):
        for inp in [
            0 , -1, 0.97, None, 'text', ['l', 'i', 's', 't'],
            '', [], {}, (), {'key': 'value'}
            ]:
            assert_equal(collatze_steps(0), None)

    def collatz_steps_some_numbers(self):
        assert_equal(collatze_steps(1), 0)
        assert_equal(collatze_steps(2), 1)
        assert_equal(collatze_steps(3), 7)
        assert_equal(collatze_steps(11), 14)
        assert_equal(collatze_steps(220), 114)
        assert_equal(collatze_steps(11000), 42)

    def collatz_steps_too_big_input(self):
        assert_equal(collatze_steps(123456789000), None)

   
