import math

def vx(v, alpha):
    return v * math.cos(alpha)

def vy(v, alpha):
    return v * math.sin(alpha)

def Fx(m, v, alpha):
    return m * v * math.cos(alpha)

def Fy(m, v, alpha):
    return m * v * math.sin(alpha)