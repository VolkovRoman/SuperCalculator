import unittest

ALPHABET = "0123456789ABCDEF"


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

class convert_base_test(unittest.TestCase):
    def test_convert_type(self):
        binary_a = BinaryNumber('1234', 10).convert_to_binary()
        self.addTypeEqualityFunc(str, binary_a)
    def test_convet_func(self):
        binary_b = BinaryNumber('98765', 10).convert_to_binary()
        self.assertEqual(binary_b, '11000000111001101')


class BinaryNumber:
    def __init__(self, number, base):
        self.number = number
        self.base = base

    def convert_to_binary(self):
        return convert_base(self.number, 2, self.base)




binary_c = BinaryNumber('01010110', 2).convert_to_binary()
binary_d = BinaryNumber('01010101', 2).convert_to_binary()
binary_e = BinaryNumber('364', 8).convert_to_binary()
binary_f = BinaryNumber('146', 8).convert_to_binary()
binary_g = BinaryNumber('8a', 16).convert_to_binary()
binary_h = BinaryNumber('8a', 16).convert_to_binary()


def sum_(x, y):
    max_len = max(len(x), len(y))
    x = x.zfill(max_len)
    y = y.zfill(max_len)
    shift = 0
    res = ''
    for i in range(max_len - 1, -1, -1):
        counter = shift
        counter += 1 if x[i] == '1' else 0
        counter += 1 if y[i] == '1' else 0
        res = ('1' if counter % 2 == 1 else '0') + res
        shift = 0 if counter < 2 else 1

    if shift != 0:
        res = '1' + res
    return res.lstrip('0')


sum_(binary_c, binary_d)

class Calculator_test_sum(unittest.TestCase):
    def test_result(self):
        self.assertEqual(sum_('010', '011'), '101')
        self.assertEqual(sum_('1000', '1010'), '10010')



def sub_(x, y):
    max_len = max(len(x), len(y))
    x = x.zfill(max_len)
    y = y.zfill(max_len)
    shift = 0
    res = ''
    for i in range(max_len - 1, -1, -1):
        counter = shift
        counter += 1 if x[i] == '1' else 0
        counter += -1 if y[i] == '1' else 0
        res = ('1' if counter % 2 == 1 else '0') + res
        shift = 0 if counter != -1 else -1

    if shift != 0:
        res = '1' + res
    return res.lstrip('0')


sub_(binary_e, binary_f)

class Calculator_test_sub(unittest.TestCase):
    def test_result(self):
        self.assertEqual(sub_('010', '010'), '')
        self.assertEqual(sub_('1010', '1000'), '10')


def mul_(x, y):
    max_len = max(len(x), len(y))
    x = x.zfill(max_len)
    y = y.zfill(max_len)
    carry = "0"
    res = ''
    addend = []
    buffer = '0'
    for i in range(max_len - 1, -1, -1):
        if y[i] == '0':
            addend.append('0')
        else:
            addend.append(x)
        carry += '0'
    for extra_zero in range(1, len(addend)):
        addend[extra_zero] += '0' * extra_zero
    for buf in range(len(addend)):
        buffer = sum_(buffer, addend[buf])
    res += buffer
    return res.lstrip('0')


mul_(binary_g, binary_h)


if __name__ == '__main__':
    unittest.main()
