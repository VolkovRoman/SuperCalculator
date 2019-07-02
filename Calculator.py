def convert_base(num, to_base=10, from_base=10):
    # first convert to decimal number
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEF"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]


a = ('1234', 10)
b = ('98765', 10)
c = ('01010110', 2)
d = ('01010101', 2)
e = ('364', 8)
f = ('146', 8)
g = ('8a', 16)
h = ('0e', 16)

binary_a = convert_base(a[0], 2, a[1])
binary_b = convert_base(b[0], 2, b[1])
binary_c = convert_base(c[0], 2, c[1])
binary_d = convert_base(d[0], 2, d[1])
binary_e = convert_base(e[0], 2, e[1])
binary_f = convert_base(f[0], 2, f[1])
binary_g = convert_base(g[0], 2, g[1])
binary_h = convert_base(h[0], 2, h[1])


def sum_(x, y):
    max_len = max(len(x), len(y))
    x = x.zfill(max_len)
    y = y.zfill(max_len)
    shift = 0
    res = ''
    for i in range(max_len - 1, -1, -1):
        r = shift
        r += 1 if x[i] == '1' else 0
        r += 1 if y[i] == '1' else 0
        res = ('1' if r % 2 == 1 else '0') + res
        shift = 0 if r < 2 else 1

    if shift != 0:
        res = '1' + res
    return res


sum_(binary_a, binary_b)


def sub_(x, y):
    max_len = max(len(x), len(y))
    x = x.zfill(max_len)
    y = y.zfill(max_len)
    shift = 0
    res = ''
    for i in range(max_len - 1, -1, -1):
        r = shift
        r += 1 if x[i] == '1' else 0
        r += -1 if y[i] == '1' else 0
        res = ('1' if r % 2 == 1 else '0') + res
        shift = 0 if r != -1 else -1

    if shift != 0:
        res = '1' + res
    return res.zfill(max_len)


sub_(binary_a, binary_b)


def mul_(x , y):
    max_len = max(len(x), len(y))
    x = x.zfill(max_len)
    y = y.zfill(max_len)
    carry = "0"
    res = ''
    slag = []
    for i in range(max_len - 1, -1, -1):
        if y[i] == '0':
            slag.append('0')
        else:
            slag.append(x+carry)
        carry += '0'
    dictt = []
    for y in range(0, len(slag)-1, 2):
        dictt.append(sum_(slag[y], slag[y + 1]))



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


print(mul_(binary_c, binary_d))