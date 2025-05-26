import math

def berechne_wahrscheinlichkeit(mu, K):

    p = sum((mu**k / math.factorial(k)) for k in range(K + 1)) * math.exp(-mu)
    return p * 100

print(berechne_wahrscheinlichkeit(10,10))
print(berechne_wahrscheinlichkeit(10,15))
print(berechne_wahrscheinlichkeit(20,20))
print(berechne_wahrscheinlichkeit(20,30))


def berechne_neg_wahrscheinlichkeit(mu, K):
    p = sum(((mu**n / math.factorial(n)) * (1 - (K/n))) for n in range(K+1, 3*K)) * math.exp(-mu)
    return p * 100

print(berechne_neg_wahrscheinlichkeit(10,10))
print(berechne_neg_wahrscheinlichkeit(10,15))
print(berechne_neg_wahrscheinlichkeit(20,20))
print(berechne_neg_wahrscheinlichkeit(20,30))
