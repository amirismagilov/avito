from app.lib import create_flat


def test_create_flat():
    data = [2, 20, 3, 'Казань', 'Вахитовский', 'Волкова 5', 2_000_000]
    expected = [{
        'number_of_rooms': 2,
        'square': 20,
        'floor': 3,
        'city': 'Казань',
        'district': 'Вахитовский',
        'address': 'Волкова 5',
        'price': 2_000_000,
    }]
    actual = create_flat(data)
    assert expected == actual
