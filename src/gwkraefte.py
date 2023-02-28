def luftWiederstand(A=28.3, v, cw=0.1):
    return round(-0.5 * A * 1.225 * v**2 * cw, 2)

def gewichtskraft(m, g=9.81):
    return round(m * g, 2)