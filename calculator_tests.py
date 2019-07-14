import unittest
from Calculator import Number, sum_, sub_, mul_, div_
from kate_calc_fin import Calculator

# first num, second num and result
test_sum_dec = [
    ['10', '5', '15'],
    ['123456789', '987654321', '1111111110']
]
test_sum_bin = [
    ['101010', '1111111', '10101001'],
    ['1010101010101010101010101010', '010101010101010101010101010', '1101010101010101010101010100']
]
test_sum_hex = [
    ['A45', 'B51', '1596'],
    ['FBA6510', 'CD9A673210', 'CDAA219720']
]
test_sum_oct = [
    ['17', '56', '75'],
    ['13245675642365521', '1321654632135351213', '1335122527777736734']
]


class CalculatorTest(unittest.TestCase):

    def test_sum_dec(self):
        for fir, sec, res in test_sum_dec:
            func_res = sum_(Number(fir, 10).convert_to_binary(), Number(sec, 10).convert_to_binary())
            func_res = int(func_res, 2)  # Перевожу в нужную СС для сравнения с результатами других функций
            self.assertEqual(str(func_res), res)
            func_another_res = Calculator().calculate(fir, sec, '+')
            self.assertEqual(func_another_res, res)

    def test_sum_bin(self):
        for fir, sec, res in test_sum_bin:
            func_res = sum_(fir, sec)
            self.assertEqual(func_res, res)
            func_another_res = Calculator().calculate('0b'+fir, '0b'+sec, '+')
            self.assertEqual(func_another_res, res)

    def test_sum_hex(self):
        for fir, sec, res in test_sum_hex:
            func_res = sum_(Number(fir, 16).convert_to_binary(), Number(sec, 16).convert_to_binary())
            func_res = int(func_res, 2)  # Перевожу в 10 СС
            func_res = str('%X' % func_res)  # Перевожу в нужную СС для сравнения с результатами других функций
            self.assertEqual(func_res.upper(), res)
            func_another_res = Calculator().calculate('0x'+fir, '0x'+sec, '+')
            self.assertEqual(func_another_res, res)

    def test_sum_oct(self):
        for fir, sec, res in test_sum_oct:
            func_res = sum_(Number(fir, 8).convert_to_binary(), Number(sec, 8).convert_to_binary())
            func_res = int(func_res, 2)  # Перевожу в 10 СС
            func_res = str('%o' % func_res)  # Перевожу в нужную СС для сравнения с результатами других функций
            self.assertEqual(func_res, res)
            func_another_res = Calculator().calculate('0'+fir, '0'+sec, '+')
            self.assertEqual(func_another_res, res)


if __name__ == '__main__':
    unittest.main()
