import unittest
from Calculator import Number, sum_, sub_, mul_, div_
from kate_calc import Calculator

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
test_sub_dec = [
    ['10', '5', '5'],
    ['987987987', '123123', '987864864']
]
test_sub_bin = [
    ['111100011010', '11101010', '111000110000'],
    ['10101010101010101010101010101', '111111110101011', '10101010101001101010110101010']
]
test_sub_hex = [
    ['F', 'B', '4'],
    ['DDADCCF454', '987456', 'DDAD347FFE']
]
test_sub_oct = [
    ['71175652', '555421', '70420231'],
    ['13243546576', '243546576', '13000000000']
]
test_mul_dec = [
    ['111', '11', '1221'],
    ['123456789987654321', '64', '7901234559209876544']
]
test_mul_bin = [
    ['11111001010110101', '101', '10011011110110001001'],
    ['100011101', '111001110', '100000001001010110']
]
test_mul_hex = [
    ['FADE', '10011', 'FAEEA8BE'],
    ['1CDB', 'A6', '12B602']
]
test_mul_oct = [
    ['1774', '4771', '11736034'],
    ['306773456123212512', '17', '5650675664341037526']
]
test_div_dec = [
    ['362', '12', '30'],
    ['997', '17', '58']
]
test_div_bin = [
    ['10110001011010110110', '1110101', '1100001000011'],
    ['10100100100', '11111111', '101']
]
test_div_hex = [
    ['AD14', '6', '1CD8'],
    ['199456', '80', '3328']
]
test_div_oct = [
    ['774', '6', '124'],
    ['456123654321', '7777777', '45612']
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

    def test_sub_dec(self):
        for fir, sec, res in test_sub_dec:
            func_res = sub_(Number(fir, 10).convert_to_binary(), Number(sec, 10).convert_to_binary())
            func_res = int(func_res, 2)  # Перевожу в нужную СС для сравнения с результатами других функций
            self.assertEqual(str(func_res), res)
            func_another_res = Calculator().calculate(fir, sec, '-')
            self.assertEqual(func_another_res, res)

    def test_sub_bin(self):
        for fir, sec, res in test_sub_bin:
            func_res = sub_(fir, sec)
            self.assertEqual(func_res, res)
            func_another_res = Calculator().calculate('0b'+fir, '0b'+sec, '-')
            self.assertEqual(func_another_res, res)

    def test_sub_hex(self):
        for fir, sec, res in test_sub_hex:
            func_res = sub_(Number(fir, 16).convert_to_binary(), Number(sec, 16).convert_to_binary())
            func_res = int(func_res, 2)  # Перевожу в 10 СС
            func_res = str('%X' % func_res)  # Перевожу в нужную СС для сравнения с результатами других функций
            self.assertEqual(func_res.upper(), res)
            func_another_res = Calculator().calculate('0x'+fir, '0x'+sec, '-')
            self.assertEqual(func_another_res, res)

    def test_sub_oct(self):
        for fir, sec, res in test_sub_oct:
            func_res = sub_(Number(fir, 8).convert_to_binary(), Number(sec, 8).convert_to_binary())
            func_res = int(func_res, 2)  # Перевожу в 10 СС
            func_res = str('%o' % func_res)  # Перевожу в нужную СС для сравнения с результатами других функций
            self.assertEqual(func_res, res)
            func_another_res = Calculator().calculate('0'+fir, '0'+sec, '-')
            self.assertEqual(func_another_res, res)

    def test_mul_dec(self):
        for fir, sec, res in test_mul_dec:
            func_res = mul_(Number(fir, 10).convert_to_binary(), Number(sec, 10).convert_to_binary())
            func_res = int(func_res, 2)  # Перевожу в нужную СС для сравнения с результатами других функций
            self.assertEqual(str(func_res), res)
            func_another_res = Calculator().calculate(fir, sec, '*')
            self.assertEqual(func_another_res, res)

    def test_mul_bin(self):
        for fir, sec, res in test_mul_bin:
            func_res = mul_(fir, sec)
            self.assertEqual(func_res, res)
            func_another_res = Calculator().calculate('0b'+fir, '0b'+sec, '*')
            self.assertEqual(func_another_res, res)

    def test_mul_hex(self):
        for fir, sec, res in test_mul_hex:
            func_res = mul_(Number(fir, 16).convert_to_binary(), Number(sec, 16).convert_to_binary())
            func_res = int(func_res, 2)  # Перевожу в 10 СС
            func_res = str('%X' % func_res)  # Перевожу в нужную СС для сравнения с результатами других функций
            self.assertEqual(func_res.upper(), res)
            func_another_res = Calculator().calculate('0x'+fir, '0x'+sec, '*')
            self.assertEqual(func_another_res, res)

    def test_mul_oct(self):
        for fir, sec, res in test_mul_oct:
            func_res = mul_(Number(fir, 8).convert_to_binary(), Number(sec, 8).convert_to_binary())
            func_res = int(func_res, 2)  # Перевожу в 10 СС
            func_res = str('%o' % func_res)  # Перевожу в нужную СС для сравнения с результатами других функций
            self.assertEqual(func_res, res)
            func_another_res = Calculator().calculate('0'+fir, '0'+sec, '*')
            self.assertEqual(func_another_res, res)

    def test_div_dec(self):
        for fir, sec, res in test_div_dec:
            func_res = div_(Number(fir, 10).convert_to_binary(), Number(sec, 10).convert_to_binary())
            func_res = int(func_res, 2)  # Перевожу в нужную СС для сравнения с результатами других функций
            self.assertEqual(str(func_res), res)
            func_another_res = Calculator().calculate(fir, sec, '/')
            self.assertEqual(func_another_res, res)

    def test_div_bin(self):
        for fir, sec, res in test_div_bin:
            func_res = div_(fir, sec)
            self.assertEqual(func_res, res)
            func_another_res = Calculator().calculate('0b'+fir, '0b'+sec, '/')
            self.assertEqual(func_another_res, res)

    def test_div_hex(self):
        for fir, sec, res in test_div_hex:
            func_res = div_(Number(fir, 16).convert_to_binary(), Number(sec, 16).convert_to_binary())
            func_res = int(func_res, 2)  # Перевожу в 10 СС
            func_res = str('%X' % func_res)  # Перевожу в нужную СС для сравнения с результатами других функций
            self.assertEqual(func_res.upper(), res)
            func_another_res = Calculator().calculate('0x'+fir, '0x'+sec, '/')
            self.assertEqual(func_another_res, res)

    def test_div_oct(self):
        for fir, sec, res in test_div_oct:
            func_res = div_(Number(fir, 8).convert_to_binary(), Number(sec, 8).convert_to_binary())
            func_res = int(func_res, 2)  # Перевожу в 10 СС
            func_res = str('%o' % func_res)  # Перевожу в нужную СС для сравнения с результатами других функций
            self.assertEqual(func_res, res)
            func_another_res = Calculator().calculate('0'+fir, '0'+sec, '/')
            self.assertEqual(func_another_res, res)


if __name__ == '__main__':
    unittest.main()
