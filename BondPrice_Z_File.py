def getBondPrice_Z(face, couponRate, times, yc):
    C = face * couponRate
    bondPrice = 0.0
    for t, y in zip(times, yc):
        cf = C
        if t == times[-1]:
            cf += face
        bondPrice += cf / (1 + y) ** t
    return bondPrice

