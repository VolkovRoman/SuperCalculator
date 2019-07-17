import cProfile
import pstats
import io

from Calculator import Number, sum_, sub_, mul_, div_
from kate_calc import Calculator


CALC_NAME_1 = 'Calculator'
FUNCS_1 = [sum_, sub_, mul_, div_]

CALC_NAME_2 = 'kate_calc'
FUNCS_2 = [Calculator().add, Calculator().subtract, Calculator().multiply, Calculator().divide]

BASE = 10
NUMBER_PAIRS = [('151651220544150151535135151468', '542415458457584254811111111111', BASE),
                ('151651220544150151535135151468', '5425758425481111111111684', BASE),
                ('1015165122054415011111111111111110151651220544150151535135151468345516816485435465416',
                 '5424154584575842548111111111111111101516153513515146834551681648543546541651220544150', BASE),
                ('10151651220544150111111111111111101516510151651220544150111111111111111101516512205441501515351351514'
                 '683455168164854354654161220544150151535135151468345516816485435465416',
                 '54245424154584575842548111111111111111101516153513515146834551681648543546541651220544150154584575842'
                 '548111111111111111101516153513515146834551681648543546541651220544150', BASE),
                ('11015165122054415011111111111111110151651220544150151535135151468345516816485435465416015165122054415'
                 '01111111111111111015165122054415015153513515146834551681015165122054415011111111111111110151651220544'
                 '15015153513515146834551681648543546541616485435465416',
                 '54241545845758425481111111111111111015161535135151468345516816485435465416512205441505424154584575424'
                 '15458457584254811111111111111110151615351351514683455168164854354654165122054415058425481111111111111'
                 '11101516153513515146834551681648543546541651220544150', BASE),
                ('10151651220544150111111111111111101516512205441501515351351514683455168164854354654161015165122054415'
                 '01111111111111111015165122054415015153513515146834551681648543546541610151651220544150111111111111111'
                 '10151651220544150151535135151468345516816485435465416101516512205441501111111111111111015165122054415'
                 '0151535135151468345516816485435465416',
                 '55424154584575842548111111111111111101516153513515146834551681648543546541651220544150542415458457584'
                 '25481111111111111111015161535135151468345516542415458457584254811111111111111110151615351351514683455'
                 '16816485435465416512205441508164854354654165122054415042415458457584254811111111111111110151615351351'
                 '5146834551681648543546541651220544150', BASE)]

TARGET_FILE = '_speed_test.txt'


def collect_info(file, pr):
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('tottime')
    ps.print_stats()

    with open(file, 'a+') as f:
        f.write(s.getvalue())


def test_performance(calc_name, calc_funcs, file, pairs, wrap=None):
    for operation in range(len(calc_funcs)):
        with open(file, 'a+') as report_file:
            report_file.writelines('--------- {} {} function ---------\n\n'.format
                                   (calc_name, calc_funcs[operation].__name__))
        for pair in range(len(pairs)):
            profiler = cProfile.Profile()
            with open(file, 'a+') as report_file:
                report_file.writelines('------ {} -- Length of operands: {}, {} ------\n\n'.format
                                       (calc_funcs[operation].__name__, len(pairs[pair][0]), len(pairs[pair][1])))

            profiler.enable()
            if wrap:
                calc_funcs[operation](Number(pairs[pair][0], pairs[pair][2]).convert_to_binary(),
                                      Number(pairs[pair][1], pairs[pair][2]).convert_to_binary())
            else:
                calc_funcs[operation](pairs[pair][0], pairs[pair][1], pairs[pair][2])
            profiler.disable()
            collect_info(calc_name+TARGET_FILE, profiler)


if __name__ == "__main__":
    test_performance(CALC_NAME_1, FUNCS_1, CALC_NAME_1 + TARGET_FILE, NUMBER_PAIRS, wrap=True)
    test_performance(CALC_NAME_2, FUNCS_2, CALC_NAME_2 + TARGET_FILE, NUMBER_PAIRS)
