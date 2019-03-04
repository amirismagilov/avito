def create_flat(number_of_rooms, square, floor, city, district, address, price):
    return {
        'number_of_rooms': number_of_rooms,
        'square': square,
        'floor': floor,
        'city': city,
        'district': district,
        'address': address,
        'price': price,
    }

def add_flat(container, flat):
    container.append(flat)

def search_flat(container, search):
    result = []
    search_lowercassed = search.strip().lower()
    for flat in container:
        if search_lowercassed in flat['district'].lower():
            result.append(flat)
    return result

def price_filter(container, max_price): #max - int
    result = []
    for flat in container:
        if max_price >= int(flat['price']):
            result.append(flat)
    return result
