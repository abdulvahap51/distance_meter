from math import sin, cos, sqrt, atan2, radians

def distance(lat1, lon1, lat2, lon2):
    # Dünya'nın yarıçapı (km)
    R = 6371.0

    # Radyan cinsinden koordinatlar
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    # İki nokta arasındaki fark
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    # Haversine formülü
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    # Mesafe (m)
    distance = R * c * 1000
    return distance

 
print(distance(41.0082, 28.9784, 39.9208, 32.8541))

