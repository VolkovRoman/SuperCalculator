from kate_calc import Number, Calculator


def test_get_base_and_num(test_pairs):
    for number, base_and_num in test_pairs.items():
        test_num = Number(number)
        assert test_num.get_base_and_num(number) == base_and_num


TEST_BASES_AND_NUMS = {
    '0b10101010': (2, '10101010'),
    '0x123456FAD': (16, '123456FAD'),
    '0123456': (8, '123456'),
    '123789': (10, '123789'),
    '0b104': (None, '104'),
    '0': (10, '0'),
    '12355D': (None, '12355D')}
test_get_base_and_num(TEST_BASES_AND_NUMS)


def test_hex_to_dec(test_symbols):
    for symbol, value in test_symbols.items():
        assert Number.hex_to_dec(symbol) == value


TEST_HEX_SYMBOLS = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 'Invalid hex number',
                    '-': 'Invalid hex number'}
test_hex_to_dec(TEST_HEX_SYMBOLS)


def test_unify_nums(test_x, test_y, assert_x_y):
    calculator = Calculator()
    assert calculator.unify_nums(test_x, test_y) == assert_x_y


TEST_X, TEST_Y = '1230000', '123'
ASSERT_X_Y = ('1230000', '0000123')
test_unify_nums(TEST_X, TEST_Y, ASSERT_X_Y)

TEST_PAIRS = [('0b10000010', '0b110010'),
              ('0x12C3123AF1', '0xA1004'),
              ('012345', '02233356667'),
              ('15893', '1258'),
              ('0x1A', '0b10'),
              ('0b12222', '0x12AF'),
              ('123D', '0189'),
              ('', '124')]
NUM_SYS_ERR = 'Numbers from two different number systems.'
INVALID_NUMS_ERR = 'Invalid numbers.'

ASSERT_ADD = ['10110100', '12C31C4AF5', '2233371234', '17151', NUM_SYS_ERR, NUM_SYS_ERR, INVALID_NUMS_ERR, NUM_SYS_ERR]
ASSERT_SUBTRACT = ['1010000', '12C3082AED', '-2233344322', '14635', NUM_SYS_ERR, NUM_SYS_ERR, INVALID_NUMS_ERR, NUM_SYS_ERR]
ASSERT_MULTIPLY = ['1100101100100', 'BCCB327D61FBC4', '30042146320263', '19993394', NUM_SYS_ERR, NUM_SYS_ERR,
                   INVALID_NUMS_ERR, NUM_SYS_ERR]
ASSERT_DIVIDE = ['10', '1DD52', '0', '12', NUM_SYS_ERR, NUM_SYS_ERR, INVALID_NUMS_ERR, NUM_SYS_ERR]
ASSERT_GET_DIVISION_REMAINDER = ['11110', '1A5A9', '12345', '797', NUM_SYS_ERR, NUM_SYS_ERR, INVALID_NUMS_ERR, NUM_SYS_ERR]

ANSWERS = [ASSERT_ADD, ASSERT_SUBTRACT, ASSERT_MULTIPLY, ASSERT_DIVIDE, ASSERT_GET_DIVISION_REMAINDER]
OP_SIGNS = ['+', '-', '*', '/', '%']


def test_calculator(test_pairs, answer, op_sign):
    for i, pair in enumerate(test_pairs):
        x, y = pair
        calculator = Calculator()
        assert calculator.calculate(x, y, op_sign) == answer[i]


for i, op in enumerate(OP_SIGNS):
    test_calculator(TEST_PAIRS, ANSWERS[i], op)
