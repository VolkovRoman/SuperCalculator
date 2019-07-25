from calculator_speed_test import test_performance
from calculator_roman import sum_, sub_, mul_, div_


CALC_NAME = 'calculator_roman_bin'
FUNCS = [sum_, sub_, mul_, div_]

BASE = 2
PAIRS_KEYS = ['sum', 'sub', 'mul', 'div']
x = '1010010101010100101010101001010101010010101001000100101010101010010101001001010101010100111001100101'
y = '0010110101101111010100101010010100111010100101010101001010100100010010101010101001010100100101110010'
x_div = '101001'
y_div = '110101'
PAIRS = {
    'sum':
        [(x, y, BASE),
         (x * 66, y * 66, BASE),
         (x * 99, y * 99, BASE),
         (x * 132, y * 132, BASE)],
    'sub':
        [(x, y, BASE),
         (x * 66, y * 66, BASE),
         (x * 99, y * 99, BASE),
         (x * 132, y * 132, BASE)],
    'mul':
        [(x, y, BASE),
         (x * 2, y * 2, BASE),
         (x * 3, y * 3, BASE),
         (x * 4, y * 4, BASE)],
    'div':
        [(x_div, y_div, BASE),
         (x_div * 2, y_div, BASE),
         (x_div * 3, y_div, BASE),
         (x_div * 4, y_div, BASE)]
}

TARGET_FILE = '_speed_test.txt'

test_performance(CALC_NAME, FUNCS, CALC_NAME + TARGET_FILE, PAIRS, PAIRS_KEYS, wrap=True)
