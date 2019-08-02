import cProfile
import pstats
import io
import secrets

from calculator_roman import Number, sum_, sub_, mul_, div_
from calculator_kate import Calculator


def collect_info(pr):
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('tottime')
    a = ps.print_stats()

    return a.total_tt


def rand_hex():
    return secrets.token_hex(150), secrets.token_hex(100)


def test_performance(calc_funcs, wrap=None):
    funcs_quantity = len(calc_funcs)

    tottime_list = [None for _ in range(funcs_quantity)]

    for op in range(funcs_quantity):
        profiler = cProfile.Profile()

        profiler.enable()
        for i in range(10000):
            base = 16
            # Здесь должны быть рандомные входные данные длиной 150 и 100
            x = rand_hex()[0]
            y = rand_hex()[1]
            if wrap:
                calc_funcs[op](Number(x, base).convert_to_binary(),
                               Number(y, base).convert_to_binary())
            else:
                calc_funcs[op](x, y, base)
        profiler.disable()

        tottime_list[op] = round(collect_info(profiler), 3)
    return tottime_list


if __name__ == "__main__":
    CALC_NAME_1 = 'calculator_roman'
    FUNCS_1 = [sum_, sub_, mul_, div_]

    CALC_NAME_2 = 'calculator_kate'
    FUNCS_2 = [Calculator().add, Calculator().subtract, Calculator().multiply, Calculator().divide]

    print(test_performance(FUNCS_1, wrap=True))
    print(test_performance(FUNCS_2))
