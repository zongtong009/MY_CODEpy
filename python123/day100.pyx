from libc.stdlib cimport malloc, free
DEF LIMIT = 1024 * 31
DEF PRIME = 1024 * 4
DEF SIEVE = 1024 * 32
cdef inline int imin(int a, int b) nogil:
    return a if a < b else b
cdef inline int memset(char *p, int n) nogil:
    cdef:
        short *q = <short *>p
        int i, j = 0
    for i in range((n + 1) >> 1):
        j += q[i]
        q[i] = 0x0100
    return j >> 8
cdef int naive_sieve(char *sieve, int *primes, int *offsets, 
                     int n) nogil:
    cdef int i, j
    memset(sieve, n)
    for i in range(3, n, 2):
        if sieve[i]:
            j = i * i
            while j < n:
                sieve[j] = 0
                j += i << 1
            primes[0] = i
            offsets[0] = j
            primes += 1
            offsets += 1
    primes[0] = 0
    offsets[0] = 0
    return memset(sieve, n)
cdef int segmented_sieve(char *sieve, int *primes, int *offsets, 
                         int k, int n) nogil:
    cdef int i
    while primes[0]:
        i = offsets[0] - k
        while i < n:
            sieve[i] = 0
            i += primes[0] << 1
        offsets[0] = i + k
        primes += 1
        offsets += 1
    return memset(sieve, n)
cpdef int eratosthenes(int n) nogil:
    cdef:
        char *sieve
        int *primes
        int *offsets
        int k, total
    if n > LIMIT * LIMIT:
        return -1
    sieve = <char *>malloc(SIEVE)
    primes = <int *>malloc(PRIME * sizeof(int))
    offsets = <int *>malloc(PRIME * sizeof(int))
    total = naive_sieve(sieve, primes, offsets, imin(n, LIMIT))
    memset(sieve, SIEVE)
    k = LIMIT
    n -= LIMIT
    while n > 0:
        total += segmented_sieve(sieve, primes, offsets, 
                                 k, imin(n, SIEVE))
        k += SIEVE
        n -= SIEVE
    free(sieve)
    free(primes)
    free(offsets)
    return total

for i in range(1, 10):
    print('primes below 10**%d: %d' % (i, eratosthenes(10**i)))