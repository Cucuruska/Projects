""" 
Calculate digits of Pi in hexademical format using Bailey-Borwein-Plouffe formula.
"""

import math

def check_bbp(accuracy=11): # 11 enough for digits
    """ Check that formula gives correct result for first digits """
    pi = 0

    print 'index', 'part_sum'

    for k in range(0, accuracy):
        part_sum = (4.0/(8*k+1) - 2.0/(8*k+4) -1.0/(8*k+5) -1.0/(8*k+6))/pow(16,k)
        pi += part_sum
        print k, '   ',part_sum

    print '\ncalculated pi', pi
    print 'math pi      ', math.pi
    print

    return pi


def pi_bbp(n, verbose=None):
    pi = 0

    if verbose:
        print '    index', 'part_sum'

    for k in range(0,n+1):
        part0 = 4.0*pow(16, n-k, 8*k+1)/(8*k+1)
        part1 = 2.0*pow(16, n-k, 8*k+4)/(8*k+4)
        part2 = 1.0*pow(16, n-k, 8*k+5)/(8*k+5)
        part3 = 1.0*pow(16, n-k, 8*k+6)/(8*k+6)

        part_sum = part0 - part1 - part2 - part3
        pi += part_sum

        if verbose:
            print '   ', k, '   ', part_sum

        # keep value in range 0 - 1
        while pi > 1:
            pi -= 1
        while pi < 0:
            pi += 1

        hex_pi = hex(int(pi*16))

    if verbose:
        print '\n    sum ', pi
        print '    ' + str(n) + 'th digit (the integer part of 16*sum): ', hex_pi, '\n'

    return hex_pi

if __name__ == '__main__':
    print "\nCalculate digit of Pi in hexademical format using Bailey-Borwein-Plouffe formula.\n"
    print "Simple check for first digits."
    check_bbp(11)
    
    while True:
        key = raw_input("digit to calculate: ")
        if key in ['q', 'exit']:
            break
        else:
            try:
                pi_bbp(int(key), True) 
            except ValueError:
                print "    expected integer or 'q'"

