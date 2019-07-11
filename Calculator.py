import unittest


class Number:
    def __init__(self, number, base):
        self.number = number
        self.base = base

    def convert_to_binary(self):

        if isinstance(self.number, str):
            n = int(self.number, self.base)
        else:
            n = int(self.number)
        result = ''
        while n > 0:
            result = str(n % 2) + result
            n = n // 2
        return result


def normalized(x, y):
    max_len = max(len(x), len(y))
    x = x.zfill(max_len)
    y = y.zfill(max_len)
    return x, y


def preparing_result(shift, result):
    if shift != 0 and result != "0":
        result = '1' + result
        result.lstrip('0')
        return result
    else:
        return result

def sum_(x, y):
    x, y = normalized(x, y)
    shift = 0
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
    shift = 0
    result = ''
    for i in range(len(x) - 1, -1, -1):
        s = int(x[i]) - int(y[i])
        if s == -1:
            if shift == 0:
                result = result + "1"
                shift = 1
            else:
                result = result + "0"

        elif s == 0:
            if shift == 0:
                result = result + "0"
            else:
                result = result + "1"

        else:
            if shift == 0:
                result = result + "1"
            else:
                result = result + "0"
                shift = 0
    result = result[::-1]
    return preparing_result(shift, result)


def mul_(x, y):
    x, y = normalized(x, y)
    addend = []
    result = ''
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


def div_(x, y):
    x, y = normalized(x, y)
    pre_result = x
    counter = 0
    while int(pre_result) > 0:
        if len(pre_result) <= len(x):
            pre_result = sub_(pre_result, y)
            counter +=1
        else:
            break
    # Когда число становится меньше нуля, то оно продолжает занимать "1" из старших разрядов
    # Пример: 011 - 100; в двоичной будет -1, а моя программа выдаст 1111
    # В участке кода ниже указано, если мы уходим за границы положительных чисел
    # (то есть когда в нем станет больше разрядов,
    # то нужно компенсировать это, выччитая 1 из конечного результата)
    
    if len(pre_result) > (len(x)):
        counter = counter-1       
    elif len(pre_result) == (len(x)):
        counter = counter

    return Number(counter, 10).convert_to_binary()


class CalculatorTest(unittest.TestCase):

    def test_convert_type(self):
        binary_a = Number('1234', 10).convert_to_binary()
        self.addTypeEqualityFunc(str, binary_a)

    def test_convert_func(self):
        binary_b = Number('98765', 10).convert_to_binary()
        self.assertEqual(binary_b, '11000000111001101')

    def test_result_sum(self):
        binary_c = Number('01010110', 2).convert_to_binary()
        binary_d = Number('01010101', 2).convert_to_binary()
        self.assertEqual(sum_(binary_c, binary_d), '10101011')

    def test_result_sub(self):
        binary_e = Number('364', 8).convert_to_binary()
        binary_f = Number('146', 8).convert_to_binary()
        self.assertEqual(sub_('010', '010'), '000')
        self.assertEqual(sub_(binary_e, binary_f), '10001110')

    def test_result_mul(self):
        binary_g = Number('8a', 16).convert_to_binary()
        binary_h = Number('9b', 16).convert_to_binary()
        self.assertEqual(mul_('0', '0'), '0')
        self.assertEqual(mul_(binary_g, binary_h), '101001110001110')

    def test_result_div(self):
        binary_i = Number('48', 10).convert_to_binary()
        binary_j = Number('6', 10).convert_to_binary()
        self.assertEqual(div_(binary_i, binary_j), '1000')
        self.assertEqual(div_('1000000', '1000'), '1000')


if __name__ == '__main__':
    unittest.main()
