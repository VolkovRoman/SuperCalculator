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

            tottime_list[op][i] = (collect_info(calc_name + TARGET_FILE, profiler))
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
    x = 1015165122054415011111111135151468345516816485546843512680111111101516561535135151468345516816485435465416512205
    PAIRS = {
        'sum':
            [(str(x), str(x), BASE),
             (str(x ** 66), str(x ** 66), BASE),
             (str(x ** 99), str(x ** 99), BASE),
             (str(x ** 132), str(x ** 132), BASE)],
        'sub':
            [(str(x), str(x), BASE),
             (str(x ** 66), str(x ** 66), BASE),
             (str(x ** 99), str(x ** 99), BASE),
             (str(x ** 132), str(x ** 132), BASE)],
        'mul':
            [('10151651220544150111111111111111101516510151651220544150111111111111111101516512205441501515351351514438'
              '4354683455168164854354654161220544150151535135151468345516816485546843512680',
              '54245424154584575842548111111111111111101516153513515146834551681648543546541651220544150154584575842854'
              '3213548111111111110151615351351514683455168164854354615846543123254056432008', BASE),
             ('10151651220544150111111111111111101516510151651220544150111111111111111101516512205441501515351351514514'
              '6846683455168164854354654161220544150151535135151468345516816485435465416156054680006850205856873546878',
              '54245424154584575842548111111111111111101516153513515146834551681648543554687601454165122054415015458457'
              '5842548111111111111111101516153513515146834551681648543546541651220544150168168645321383761000487424310',
              BASE),
             ('11015165122054415011111111111111110151651220544150151535135151468345516816485435465416015165122054415168'
              '43000111111111111111101516512205441501515351351514683455168101516512205441501111111111111111015165122054'
              '4540545515015153513515146834551681648543546541616485435465416051575024054087875878989991295559992121248',
              '54241545845758425481111111111111111015161535135151468345516816485435465416512205441505424154584575424154'
              '5421154584575842548111111111111111101516153513515146834551681648543546541651220544150584254811111111111',
              BASE),
             ('10151651220544150111111111111111101516512205441501515351351514683455168164854354654161015165122054415325'
              '48780111111111111111101516512205441501515351351514683455168164854354654161015165122054415011111111111111'
              '15310005101516512205441501515351351514683455168164854354654161015165122054415011111111111111110151651220'
              '5441554878330151535135151468345516816485435465416157845754878995434878454880121215487454545451544587542',
              '55424154584575842548111111111111111101516153513515146834551681648543546541651220544150542415458457584218'
              '75872548111111111111111101516153513515146834551654241545845758425481111111111111111015161535135151468345'
              '5022500216816485435465416512205441508164854354654165122054415042415458457584254811111111111111110151615',
              BASE)],
        'div':
            [('151654845', '54257', BASE),
             ('1015162715', '54257', BASE),
             ('10151655126', '68345', BASE),
             ('151651220587', '54241', BASE)],
    }

    TARGET_FILE = '_speed_test.txt'

    test_performance(CALC_NAME_1, FUNCS_1, CALC_NAME_1 + TARGET_FILE, PAIRS, PAIRS_KEYS, wrap=True)
    test_performance(CALC_NAME_2, FUNCS_2, CALC_NAME_2 + TARGET_FILE, PAIRS, PAIRS_KEYS)
