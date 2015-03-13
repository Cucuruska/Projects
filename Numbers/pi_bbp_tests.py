"""
Testbench for pi_bbp.
Control Pi value is in 'hex_pi.txt'.
"""

import re

from pi_bbp import *
from nose.tools import *
from math import pi


class PiTests():
    def __init__(self):
        """ Load file 'hex_pi.txt' and parse it into a dictionary """

        self.pi = {}
        control_file = 'hex_pi.txt'
        f = open(control_file)

        if not f:
            print "Can't open file" + control_file

        for line in f:
            m = re.match('([0-9a-fA-F ]+)\s*\:\s*([\d,]+)', line)
            if m:
                nums = re.sub(' ', '', m.group(1))    # remove spaces
                positions = re.sub(',', '', m.group(2))    # remove commas
                self.pi[positions] = nums

    def test_some_numbers(self):
        """ Calculate all digits of Pi presented in the control file
            and compare values """

        for pos in sorted(self.pi):
            print 'check positions ' + str(int(pos) - 50) + ' - ' + pos
            for k, value in enumerate(self.pi[pos]):
                real_pos = int(pos) - 50 + k
                res = pi_bbp(real_pos)
                assert_equal(res, '0x' + value)

if __name__ == '__main__':
    test_instance = PiTests()
    test_instance.test_some_numbers()
