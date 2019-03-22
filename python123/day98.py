import numpy as np
import sys

np.set_printoptions(precision=14, linewidth=120)


def integrate(fn, a, b, steps=5, debug=False, exact=None):
    table = np.zeros((steps, steps), dtype=np.float64)
    pow_4 = 4 ** np.arange(steps, dtype=np.float64) - 1
    # trapezoidal rule
    h = (b - a)
    table[0, 0] = h * (fn(a) + fn(b)) / 2
    for j in range(1, steps):
        h /= 2
        # extended trapezoidal rule
        table[j, 0] = table[j - 1, 0] / 2
        table[j, 0] += h * np.sum(
            fn(a + i * h) for i in range(1, 2 ** j + 1, 2)
        )
        # richardson extrapolation
        for k in range(1, j + 1):
            table[j, k] = table[j, k - 1] + \
                (table[j, k - 1] - table[j - 1, k - 1]) / pow_4[k]
    # debug
    if debug:
        print(table, file=sys.stderr)
        if exact is not None:
            errors = [
                '%.2e' % i
                for i in np.abs(table.diagonal() - exact)
            ]
            print('abs. error:', errors, file=sys.stderr)
    return table[-1, -1]


integrate(lambda x: np.exp(-x * x), 0, 1,
          debug=True, exact=0.746824132812427)

          
integrate(1..__truediv__, 1, 2, debug=True, exact=np.log(2))
