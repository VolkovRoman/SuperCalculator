def convert_base(num, to_base=10, from_base=10):
    # first convert to decimal number
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]


a = ('1234', 10)
b = ('98765', 10)
c = ('01010110', 2)
d = ('01010101', 2)
e = ('364', 8)
f = ('146', 8)
g = ('8a', 16)
h = ('0e', 16)

binary_a = convert_base(a[0], 2, a[1])
binary_b = convert_base(b[0], 2, b[1])
binary_c = convert_base(c[0], 2, c[1])
binary_d = convert_base(d[0], 2, d[1])
binary_e = convert_base(e[0], 2, e[1])
binary_f = convert_base(f[0], 2, f[1])
binary_g = convert_base(g[0], 2, g[1])
binary_h = convert_base(h[0], 2, h[1])


def sum_(x, y):
    max_len = max(len(x), len(y))
    x = x.zfill(max_len)
    y = y.zfill(max_len)
    shift = 0
    res = ''
    for i in range(max_len - 1, -1, -1):
        r = shift
        r += 1 if x[i] == '1' else 0
        r += 1 if y[i] == '1' else 0
        res = ('1' if r % 2 == 1 else '0') + res
        shift = 0 if r < 2 else 1

    if shift != 0:
        res = '1' + res
    return res.zfill(max_len)


sum_(binary_a, binary_b)

