def primes_sieve(n):
    """Return a list of all prime numbers less than or equal to `n`."""
    if n <= 1:
        raise Exception("Please enter a bigger number")
    primes = [2]
    for i in range(2, n):
        is_prime = True
        for j in range(2, i):
            if (j%i) == 0:
                is_prime = False
                break
        if is_prime == True:
            primes.append(i)
    
    return primes


def factorize(n):
    """Return the list of prime factors of `n`, in ascending order."""
    pass  # TODO


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
