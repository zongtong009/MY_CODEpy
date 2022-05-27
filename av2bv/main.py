table = 'fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'
tr = {}

for i in range(58):
    tr[table[i]] = i

s = [11, 10, 3, 8, 4, 6]
xor = 177451812
add = 8728348608


def dec(x):
    r = 0
    for k in range(6):
        r += tr[x[s[k]]] * 58 ** k
    return (r - add) ^ xor


def enc(y):
    x = int(y[2:])
    x = (x ^ xor) + add
    r = list('BV1  4 1 7  ')
    for j in range(6):
        r[s[j]] = table[x // 58 ** j % 58]
    return ''.join(r)


if __name__ == '__main__':
    # print(dec('BV17x411w7KC'))
    # print(dec('BV1Q541167Qg'))
    # print(dec('BV1mK4y1C7Bz'))
    print(enc('av633151695'))
