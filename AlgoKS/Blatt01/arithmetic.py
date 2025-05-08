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
    pass  # TODO


def qreduce(fraction):
    """Fully reduce the given fraction, represented as a tuple of numerator
    and denominator, and return the result as a tuple.

    Args:
        fraction: Tuple `(p, q)` representing the fraction p / q, where q > 0.
    """
    pass  # TODO


def qadd(r, s):
    """Add the two rational numbers `r` and `s` and return the resuls
    as a fully reduced fraction.

    Args:
        r: First summand, a rational number represented as a tuple
            of numerator and denominator
        s: Second summand, a rational number represented as a tuple
            of numerator and denominator
    """
    pass  # TODO
