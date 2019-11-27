from apistar import test

from app import app, cars

client = test.TestClient(app)


def test_list_cars():
    response = client.get('/')
    assert response.status_code == 200
    cars = response.json()
    assert len(cars) == 1000
    assert type(cars) == list
    car = cars[0]
    expected = {'id': 1, 'manufacturer': 'Nissan',
                'model': 'Altima', 'year': '2003',
                'vin': '3C6LD4BT0CG960524'}
    assert car == expected
