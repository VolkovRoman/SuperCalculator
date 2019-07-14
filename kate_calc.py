import re

patterns = {2: '[^0-1]', 8: '[^0-7]', 16: '[^0-9,a-f,A-F]', 10: '[^0-9]'}


class Number:
    def __init__(self, number):
        self.base, self.value = self.get_base_and_num(number)

    def get_base_and_num(self, number):
        try:
            if number[:2] == '0x':
                number = number[2:]
                num_base = 16
            elif number[:2] == '0b':
                number = number[2:]
                num_base = 2
            elif number[0] == '0' and len(number) > 1:
                number = number[1:]
                num_base = 8
            else:
                num_base = 10
            num_base = self.check_number_base(num_base, number, patterns)
            return num_base, number

        except Exception:
            return None, number

    def check_number_base(self, num_base, number, pattern):
        if re.search(pattern[num_base], number):
            num_base = None
        return num_base

    @staticmethod
    def hex_to_dec(hex_symbol):
        if not hex_symbol.isdigit():
            hex_symbol = hex_symbol.upper()
            h = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
            try:
                hex_symbol = h[hex_symbol]
            except KeyError:
                return 'Invalid hex number'
        return hex_symbol

    @staticmethod
    def dec_to_hex(dec_number):
        if 9 < dec_number < 16:
            h = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
            try:
                dec_number = h[dec_number]
            except KeyError:
                return 'Invalid decimal number'
        return str(dec_number)


class Calculator:
    def calculate(self, x, y, operation):
        x_raw = Number(x)
        y_raw = Number(y)
        base_x, x = x_raw.base, x_raw.value
        base_y, y = y_raw.base, y_raw.value
        if base_x == base_y:
            if base_x is None:
                return 'Invalid numbers.'
        else:
            return 'Numbers from two different number systems.'

        return self.choose_operation(x, y, base_x, operation)

    def choose_operation(self, x, y, base, op):
        if op == '-':
            return self.subtract(x, y, base)
        elif op == '+':
            return self.add(x, y, base)
        elif op == '*':
            return self.multiply(x, y, base)
        elif op == '/':
            if y == '0':
                return "Division by zero."
            else:
                return self.divide(x, y, base)[0]
        elif op == '%':
            if y == '0':
                return "Division by zero."
            else:
                return self.get_division_remainder(x, y, base)
        else:
            return "Operation unsupported."

    def unify_nums(self, x, y):
        len_of_x, len_of_y = len(x), len(y)
        if len_of_x > len_of_y:
            for i in range(len_of_x - len_of_y):
                y = '0' + y
        elif len_of_x < len_of_y:
            len_of_x, len_of_y = len_of_y, len_of_x
            for i in range(len_of_x - len_of_y):
                x = '0' + x
        return x.upper(), y.upper()

    def add(self, x, y, base):
        res = self.basis_for_add_or_subtract(x, y, base, op_code=1)
        if base == 16:
            return res
        return str(int(res))

    def subtract(self, x, y, base):
        res = self.basis_for_add_or_subtract(x, y, base, op_code=-1)
        if base == 16 or res[0] == '-':
            return res
        return str(int(res))

    def basis_for_add_or_subtract(self, x, y, base, op_code):
        res = ''
        x, y = self.unify_nums(x, y)

        negative_result = False
        if x < y and op_code == -1:
            x, y = y[:], x[:]
            negative_result = True

        cur_iteration_pool = 0
        for i in range(-1, -(len(x) + 1), -1):
            x_cur, y_cur = x[i], y[i]
            if base == 16:
                x_cur = Number.hex_to_dec(x[i])
                y_cur = Number.hex_to_dec(y[i])
            x_cur = int(x_cur)
            y_cur = int(y_cur)

            current_res = x_cur + y_cur * op_code + cur_iteration_pool
            cur_iteration_pool = 0

            if current_res >= base:
                cur_iteration_pool += 1
                current_res = current_res % base
            elif current_res < 0:
                current_res += base
                cur_iteration_pool -= 1

            if base == 16:
                current_res = Number.dec_to_hex(current_res)
            res += str(current_res)

        if cur_iteration_pool:
            res = str(cur_iteration_pool) + res[::-1]
        else:
            res = res[::-1]

        if negative_result:
            res = '-' + res
        return res

    def multiply(self, x, y, base):
        res = ''
        cur_iteration_pool = 0
        for i in range(-1, -(len(y) + 1), -1):
            iteration_res = ''
            for j in range(-1, -(len(x) + 1), -1):
                x_cur, y_cur = x[j], y[i]
                if base == 16:
                    x_cur = Number.hex_to_dec(x[j])
                    y_cur = Number.hex_to_dec(y[i])
                x_cur = int(x_cur)
                y_cur = int(y_cur)
                current_res = x_cur * y_cur + cur_iteration_pool
                cur_iteration_pool = 0

                if current_res >= base:
                    cur_iteration_pool = current_res // base
                    current_res = current_res % base

                additional_rate = 10 ** -(j + 1)

                if base == 16:
                    current_res = Number.dec_to_hex(current_res)
                    iteration_res = self.add(iteration_res, str(current_res) + str(additional_rate)[1:], base)
                    try:
                        if int(iteration_res) >= 10:
                            iteration_res = Number.dec_to_hex(int(iteration_res))
                    except ValueError:
                        continue
                else:
                    iteration_res = str(self.add(iteration_res, str(current_res * additional_rate), base))
            additional_rate = 10 ** -(i + 1)
            if cur_iteration_pool:
                iteration_res = str(cur_iteration_pool) + iteration_res
                cur_iteration_pool = 0
            iteration_res += str(additional_rate)[1:]
            res = str(self.add(iteration_res, res, base))
        return res

    def divide(self, x, y, base):
        # Деление через вычитание
        res = '0'
        x_cur = x[:]
        if base == 16:
            unified_x, unified_y = self.unify_nums(x_cur, y)
            while unified_x >= unified_y:
                x_cur = self.subtract(x_cur, y, base)
                res = self.add('1', res, base)
                unified_x, unified_y = self.unify_nums(x_cur, y)
        else:
            while int(x_cur) >= int(y):
                x_cur = self.subtract(x_cur, y, base)
                res = self.add('1', res, base)
        if len(res) > 1:
            res = res.lstrip('0')
        return res, x_cur

    def get_division_remainder(self, x, y, base):
        res = self.divide(x, y, base)[1]
        if len(res) > 1:
            res = res.lstrip('0')
        return res


if __name__ == '__main__':
    print("Negative operands unavailable. Start number with prefix, e.g. '0b', '0x', '0'."
          " Decimal numbers have no prefix.")
    first = str(input('First number:'))
    OP = input('Operation(+, -, /, %, *):')
    second = str(input('Second number:'))
    calculator = Calculator()
    print('Result:', calculator.calculate(first, second, OP))
