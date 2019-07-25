import cProfile
import pstats
import io
import matplotlib.pyplot as plt
import os

from calculator_roman import Number, sum_, sub_, mul_, div_
from calculator_kate import Calculator


def collect_info(file, pr):
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('tottime')
    a = ps.print_stats()

    with open(file, 'a+') as f:
        f.write(s.getvalue())

    return a.total_tt


def test_performance(calc_name, calc_funcs, file, pairs, pairs_keys, wrap=None):
    dir_name = calc_name + '_performance'
    try:
        os.mkdir(dir_name)
    except FileExistsError:
        pass
    finally:
        os.chdir(dir_name)

    with open(file, 'w') as f:
        f.write('')

    funcs_quantity = len(calc_funcs)
    pairs_quantity = len(pairs[pairs_keys[0]])

    nums_length_list = [[None for _ in range(pairs_quantity)] for _ in range(funcs_quantity)]
    tottime_list = [[None for _ in range(pairs_quantity)] for _ in range(funcs_quantity)]

    for op in range(funcs_quantity):
        with open(file, 'a+') as report_file:
            report_file.writelines('--------- {} {} function ---------\n\n'.format
                                   (calc_name, calc_funcs[op].__name__))

        cur_pairs_set = pairs[pairs_keys[op]]
        for i, pair in enumerate(cur_pairs_set):
            first_length = len(pair[0])
            second_length = len(pair[1])
            profiler = cProfile.Profile()
            with open(file, 'a+') as report_file:
                report_file.writelines('------ {} -- Length of operands: {}, {} ------\n\n'
                                       .format(calc_funcs[op].__name__, first_length, second_length))

            profiler.enable()
            if wrap:
                calc_funcs[op](Number(pair[0], pair[2]).convert_to_binary(),
                               Number(pair[1], pair[2]).convert_to_binary())
            else:
                calc_funcs[op](pair[0], pair[1], pair[2])
            profiler.disable()

            tottime_list[op][i] = (collect_info(file, profiler))
            nums_length_list[op][i] = first_length + second_length

    plot_output(calc_name, calc_funcs, nums_length_list, tottime_list)
    os.chdir('../')
    return nums_length_list, tottime_list


def plot_output(calc_name, calc_funcs, n, time):
    for op in range(len(n)):
        n_cur = n[op]
        time_cur = time[op]
        plt.figure()
        plt.plot(n_cur, time_cur)
        plt.xlabel('Sum of operands digits')
        plt.ylabel('Total time, s')
        plt.plot(n_cur, time_cur, linestyle='-', marker='+')
        plt.title(calc_funcs[op].__name__)
        plt.grid(True)
        plt.savefig(calc_name + '_' + calc_funcs[op].__name__ + '.png')


if __name__ == "__main__":
    CALC_NAME_1 = 'calculator_roman'
    FUNCS_1 = [sum_, sub_, mul_, div_]

    CALC_NAME_2 = 'calculator_kate'
    FUNCS_2 = [Calculator().add, Calculator().subtract, Calculator().multiply, Calculator().divide]

    BASE = 10
    PAIRS_KEYS = ['sum', 'sub', 'mul', 'div']
    x = '1015165122054415011111113515146834551681648554684351268011111110151656153513515146834551681648543541'
    y = '5424542415458457584254811111111111111110151615351351514683455168164854354654115161065122054415015458'
    PAIRS = {
        'sum':
            [(x, y, BASE),
             (x * 66, y * 66, BASE),
             (x * 99, y * 99, BASE),
             (x * 132, y * 132, BASE)],
        'sub':
            [(x, y, BASE),
             (x * 66, y * 66, BASE),
             (x * 99, y * 99, BASE),
             (x * 132, y * 132, BASE)],
        'mul':
            [(x, y, BASE),
             (x * 2, y * 2, BASE),
             (x * 3, y * 3, BASE),
             (x * 4, y * 4, BASE)],
        'div':
            [('151654845', '54257', BASE),
             ('1015162715', '54257', BASE),
             ('10151655126', '68345', BASE),
             ('151651220587', '54241', BASE)],
    }

    TARGET_FILE = '_speed_test.txt'

    test_performance(CALC_NAME_1, FUNCS_1, CALC_NAME_1 + TARGET_FILE, PAIRS, PAIRS_KEYS, wrap=True)
    test_performance(CALC_NAME_2, FUNCS_2, CALC_NAME_2 + TARGET_FILE, PAIRS, PAIRS_KEYS)
