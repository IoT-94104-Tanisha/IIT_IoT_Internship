km_to_m = lambda km: km * 1000
m_to_cm = lambda m: m * 100
cm_to_mm = lambda cm: cm * 10
feet_to_inches = lambda ft: ft * 12
inches_to_cm = lambda inch: inch * 2.54

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