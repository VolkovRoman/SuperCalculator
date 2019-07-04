import unittest

ALPHABET = "0123456789ABCDEF"
global shift
shift = 0

class Number:
    def __init__(self, number, base):
        self.number = number
        self.base = base

    def convert_to_binary(self):
        def convert_base(num, to_base=10, from_base=10):
            # first convert to decimal number
            if isinstance(num, str):
                n = int(num, from_base)
            else:
                n = int(num)
            # now convert decimal to 'to_base' base

            if n < to_base:
                return ALPHABET[n]
            else:
                return convert_base(n // to_base, to_base) + ALPHABET[n % to_base]

        return convert_base(self.number, 2, self.base)

    def __repr__(self):
        return "('{number}', {base})".format(number=self.number, base=self.base)


def normalized(x, y):
    max_len = max(len(x), len(y))
    x = x.zfill(max_len)
    y = y.zfill(max_len)
    return x, y


def preparing_result(shift, result):
    if shift != 0:
        result = '1' + result
        result.lstrip('0')
    return result


def sum_(x, y):
    x, y = normalized(x, y)
    global shift
    result = ''
    for i in range(len(x) - 1, -1, -1):
        counter = shift
        if x[i] == '1'and y[i] == '1':
            counter += 2
        elif x[i] == '1'or y[i] == '1':
            counter += 1
        else:
            counter += 0

        result = ('1' if counter % 2 == 1 else '0') + result
        shift = 0 if counter < 2 else 1

    return preparing_result(shift, result)


def sub_(x, y):
    x, y = normalized(x, y)
    global shift
    result = ''
    for i in range(len(x) - 1, -1, -1):
        counter = shift
        if x[i] == '1'and y[i] == '0':
            counter += 1
        elif x[i] == '0'and y[i] == '1':
            counter -= 1
        else:
            counter += 0
        result = ('1' if counter % 2 == 1 else '0') + result
        shift = 0 if counter != -1 else -1

    return preparing_result(shift, result)


def mul_(x, y):
    x, y = normalized(x, y)
    addend = []
    result = '0'
    for i in range(len(x) - 1, -1, -1):
        if y[i] == '0':
            addend.append('0')
        else:
            addend.append(x)
    for extra_zero in range(1, len(addend)):
        addend[extra_zero] += '0' * extra_zero

    for buf in range(len(addend)):
        result = sum_(result, addend[buf])

    result.lstrip('0')

    return result


class CalculatorTest(unittest.TestCase):
    def test_result_sum(self):
        binary_c = Number('01010110', 2).convert_to_binary()
        binary_d = Number('01010101', 2).convert_to_binary()
        self.assertEqual(sum_(binary_c, binary_d), '10101011')

    def test_result_sub(self):
        binary_e = Number('364', 8).convert_to_binary()
        binary_f = Number('146', 8).convert_to_binary()
        self.assertEqual(sub_('010', '010'), '000')
        self.assertEqual(sub_(binary_e, binary_f), '10001110')

    def test_convert_type(self):
        binary_a = Number('1234', 10).convert_to_binary()
        self.addTypeEqualityFunc(str, binary_a)

    def test_convert_func(self):
        binary_b = Number('98765', 10).convert_to_binary()
        self.assertEqual(binary_b, '11000000111001101')

    def test_result_mul(self):
        binary_g = Number('8a', 16).convert_to_binary()
        binary_h = Number('9b', 16).convert_to_binary()
        self.assertEqual(mul_('0', '0'), '0')
        self.assertEqual(mul_(binary_g, binary_h), '101001110001110')


if __name__ == '__main__':
    unittest.main()
