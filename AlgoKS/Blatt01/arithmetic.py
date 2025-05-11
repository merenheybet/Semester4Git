def primes_sieve(n):
    """Return a list of all prime numbers less than or equal to `n`."""
    if n <= 1:
        return []
    primes = [2]
    for i in range(3, n+1, 2):
        is_prime = True
        for j in range(2, i):
            if (i % j) == 0:
                is_prime = False
                break
        if is_prime == True:
            primes.append(i)
    
    return primes


def factorize(n):
    """Return the list of prime factors of `n`, in ascending order."""
    # Could be wrong no idea tbh
    prime_numbers = primes_sieve(n)

    factors = []
    rest = n
    while rest != 1:
        for i in prime_numbers:
            if rest % i == 0:
                factors.append(i)
                rest = rest / i
    
    # steht nirgendwo, dass ich kein sort verwenden darf...
    return sorted(factors)

def gcd(a, b):
    """Compute and return the greatest common denominator of the natural numbers
    `a` and `b` using Euclid's algorithm."""

    # Calculate the Primfaktorzerlegung von a und b
    a_factors = factorize(a)
    b_factors = factorize(b)

    gcd = 1
    for i_a in a_factors:
        if i_a in b_factors:
            gcd = gcd * i_a
            # Removes first occurence of i_a - so should only remove one of the values
            b_factors.remove(i_a)
    
    return gcd



def qreduce(fraction):
    """Fully reduce the given fraction, represented as a tuple of numerator
    and denominator, and return the result as a tuple.

    Args:
        fraction: Tuple `(p, q)` representing the fraction p / q, where q > 0.
    """
    if(fraction[1] <= 0):
        raise Exception("q darf nicht kleiner gleich 0 sein")
    
    if(fraction[0] <= 0):
        abs_a = fraction[0] * -1
        divide_by = gcd(abs_a, fraction[1])
    else:
        divide_by = gcd(fraction[0], fraction[1])    
    
    return (fraction[0] // divide_by, fraction[1] // divide_by)


def qadd(r, s):
    """Add the two rational numbers `r` and `s` and return the resuls
    as a fully reduced fraction.

    Args:
        r: First summand, a rational number represented as a tuple
            of numerator and denominator
        s: Second summand, a rational number represented as a tuple
            of numerator and denominator
    """
    a_0 = r[0] * s[1]
    a_1 = s[0] * r[1]


    a = a_0 + a_1
    b = r[1] * s[1]

    return qreduce((a, b))
