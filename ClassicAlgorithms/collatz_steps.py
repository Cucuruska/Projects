"""
Collatz sequence:
if n is even:
    new_n = n/2
else:
    new_n = n*3 + 1
"""

import sys


def collatze_steps(n, verbose=None):
    """ Takes the n and calculate the number of steps to get 1
        in Collatz sequence that started with n.

        restrictions:   n is integer
                        1 < n < sys.maxint
        otherwise returns None """

    if not isinstance(n, int):
        return None

    if n > sys.maxint:
        print 'The number is too big, maximum is', sys.maxint
        return None

    if n == 0:
        return None

    if verbose and n != 1:
        print 'steps\tn'

    steps = 0
    while n > 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = n*3 + 1

        steps += 1

        if verbose:
            print steps, '\t', n

    return steps

if __name__ == '__main__':
    print "Calculate the number of steps to get 1 \
           in Collatz sequence started with n."

    while True:
        init_n = raw_input("Initial number: ")
        if init_n in ['q', 'quit', 'exit']:
            break

        try:
            init_n = int(init_n)
        except ValueError:
            print "    expected integer more than 1 or 'q'"

        result = collatze_steps(init_n, True)
        print 'steps ', result
