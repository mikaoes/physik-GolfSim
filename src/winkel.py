import math

def vx(v, alp):
    return round(v * math.cos(math.radians(alp)), 2)

def vy(v, alp):
    return round(v * math.sin(math.radians(alp)), 2)

def Fx(m, v, alp):
    return round(m * v * math.cos(math.radians(alp)), 2)

def Fy(m, v, alp):
    return round(m * v * math.sin(math.radians(alp)), 2)