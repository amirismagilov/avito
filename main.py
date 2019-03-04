from lib import create_flat, add_flat, search_flat, price_filter

flats = []

flat1 = create_flat(
    3,
    96,
    22,
    'Казань',
    'Советский',
    'Проспект победы, 139',
    7_450_000
)

flat2 = create_flat(
    2,
    46,
    2,
    'Казань',
    'Вахитовский',
    'Лесгафта, 19',
    4_130_000
)

flat3 = create_flat(
    1,
    45,
    33,
    'Казань',
    'Авиастроительный',
    'Мариупольская, 56',
    3_000_000
)

add_flat(flats, flat1)
add_flat(flats, flat2)
add_flat(flats, flat3)


print(flats)

print(search_flat(flats, ', '))

print(price_filter(flats, 5_000_100))


