import cProfile
from Calculator import Number, sum_, sub_, mul_, div_
from kate_calc import Calculator


first = '1015165122054415011111111111111110151651220544150151535135151468345516816485435465416'
second = '5424154584575842548111111111111111101516153513515146834551681648543546541651220544150'

calc = Calculator()
cProfile.run("mul_(Number(first, 10).convert_to_binary(), Number(second, 10).convert_to_binary())")
cProfile.run("calc.multiply(first, second, 10)")
cProfile.run("div_(Number(first, 10).convert_to_binary(), Number(second, 10).convert_to_binary())")
cProfile.run("calc.divide(first, second, 10)")
