import unittest
from Calculator import Number, sum_, sub_, mul_, div_
from kate_calc import Calculator

# first num, second num and result
test_sum_dec = [
    ['10', '5', '15'],
    ['123456789', '987654321', '1111111110'],
    ['172003723', '42591211', '214594934'],
    ['10000010203040506070809', '1111111090807050603', '10001121314131313121412'],
    ['119308149119308149', '186381560186381560', '305689709305689709'],
]
test_sum_bin = [
    ['101010', '1111111', '10101001'],
    ['1010101010101010101010101010', '010101010101010101010101010', '1101010101010101010101010100'],
    ['11110000111100001111000011110000', '00001111000011110000111100001111' ,'11111111111111111111111111111111']
]
test_sum_hex = [
    ['A45', 'B51', '1596'],
    ['FBA6510', 'CD9A673210', 'CDAA219720'],
    ['1B69B4BE052FAB11B69B4BE052FAB1', '6565CCF11FCE74E', '1B69B4BE052FAB180CF81AF24FE1FF'],
    ['10000022335555BB51CC98745f6212651', '123FFFACCCA11C1A1C', '10000022335555BC75CC93412973D406D']
]
test_sum_oct = [
    ['17', '56', '75'],
    ['13245675642365521', '1321654632135351213', '1335122527777736734'],
    ['111100002203304455660077111100002203304455660077', '110000007650105040302010', '111100002203304455660077221100012053411516162107']
]
test_sub_dec = [
    ['10', '5', '5'],
    ['987987987', '123123', '987864864'],
    ['722613295722613295', '721835066', '722613295000778229'],
    ['10000010203040506070809', '109845602040110001','9999900357438465960808'],
    ['750588860750588860750588860750588860', '288613213288613213288613213288613213', '461975647461975647461975647461975647'],
]
test_sub_bin = [
    ['111100011010', '11101010', '111000110000'],
    ['10101010101010101010101010101', '111111110101011', '10101010101001101010110101010'],
    ['11110000111100001111000011110000', '00001111000011110000111100001111' ,'11100001111000011110000111100001']
]
test_sub_hex = [
    ['F', 'B', '4'],
    ['DDADCCF454', '987456', 'DDAD347FFE'],
    ['AEF38B8DFE7BE86E68E37D4F304471216CFDDC4F', '579E7AC12C890CD72C04E79F13A1CCF396C53', 'AEEE11A652691FDD9B70BD00B65337049DC46FFC']
]
test_sub_oct = [
    ['71175652', '555421', '70420231'],
    ['13243546576', '243546576', '13000000000'],
    ['11217260254341552650002247250631716266123', '47375766737716216276123', '11217260254341552600404260310713477770000']
]
test_mul_dec = [
    ['111', '11', '1221'],
    ['123456789987654321', '64', '7901234559209876544'],
    ['1020304050607080', '102', '104071013161922160'],
    ['654654654654', '456456456456', '298821343865791268746224'],
]
test_mul_bin = [
    ['11111001010110101', '101', '10011011110110001001'],
    ['100011101', '111001110', '100000001001010110'],
    ['11110000111100001111000011110000', '00001111000011110000111100001111' ,'111000101100010010100110100001101010010011000010111000010000']
]
test_mul_hex = [
    ['FADE', '10011', 'FAEEA8BE'],
    ['1CDB', 'A6', '12B602'],
    ['316AC97E2BC6C53316AC97E2BC6C53', '4F1118DD980573', 'F4341121A4F7A001B715932497C2FF273D4810A4849']
]
test_mul_oct = [
    ['1774', '4771', '11736034'],
    ['306773456123212512', '17', '5650675664341037526'],
    ['5123162461202306571316002061577633503', '2531627731065673522077633503', '15637507254561175243703051055116114766473676510564544267231755611']
]
test_div_dec = [
    ['362', '12', '30'],
    ['997', '17', '58'],
    ['23027962', '191', '120565'],
]
test_div_bin = [
    ['10110001011010110110', '1110101', '1100001000011'],
    ['10100100100', '11111111', '101'],
    ['11110000111100001111000011110000', '00001111000011110000111100001111' ,'10000']
]
test_div_hex = [
    ['AD14', '6', '1CD8'],
    ['199456', '80', '3328'],
    ['48238329B3F452', '536870912', 'DD696']
]
test_div_oct = [
    ['774', '6', '124'],
    ['456123654321', '7777777', '45612'],
    ['4053023657020642216766404717', '1471471615421774731750315', '2420']
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
