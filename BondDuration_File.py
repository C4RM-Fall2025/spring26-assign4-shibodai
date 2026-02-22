from BondPrice_File import getBondPrice
def getBondDuration(y, face, couponRate, m, ppy=1):
    r = y / ppy
    N = m * ppy
    C = face * couponRate / ppy
    bondPrice = getBondPrice(y, face, couponRate, m, ppy)
    T = 0.0
    for t in range(1, N + 1):
        cf = C
        if t == N:
            cf += face
        T += (t / ppy) * (cf / (1 + r) ** t)
    bondDuration = T / bondPrice
    return bondDuration


