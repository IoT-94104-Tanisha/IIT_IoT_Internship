def km_to_m(km):
    return km * 1000

def m_to_cm(m):
    return m * 100

def cm_to_mm(cm):
    return cm * 10

def feet_to_inches(feet):
    return feet * 12

def inches_to_cm(inches):
    return inches * 2.54

def distconverter(dist, conversiontype, conversionfun):
    result = conversionfun(dist)
    from_unit , to = conversiontype.split(' to ')
    print(distance, from_unit, "=", result, to)

distance = float(input("Enter distance value: "))

distconverter(distance, "km to m", km_to_m)
distconverter(distance, "m to cm", m_to_cm)
distconverter(distance, "cm to mm", cm_to_mm)
distconverter(distance, "feet to inches", feet_to_inches)
distconverter(distance, "inches to cm", inches_to_cm)
