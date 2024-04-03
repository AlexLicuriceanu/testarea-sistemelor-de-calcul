import pytest
from car import Car

""" Exercise 0a: Write a fixture that returns a car instance. """
@pytest.fixture
def my_car():
    return Car(50)


def test_car_accelerate0(my_car):
    """ Exercise 0b: Using the just created fixture test the accelerate method. Hint: accelerate, then check. """
    my_car.accelerate()
    assert my_car.speed == 55

def test_car_brake0(my_car):
    """ Exercise 0c: Using the just created fixture test the brake method. Hint: break, then check. """
    my_car.brake()
    assert my_car.speed == 45

#--------------------------------------------------------------------------------------------------------------------

speed_data = {45, 50, 75, 45}

@pytest.mark.parametrize("speed_brake", speed_data)
def test_car_brake1(speed_brake):
    car = Car(50)
    car.brake()
    assert car.speed == speed_brake


""" Exercise 1a: Write a parameterized test for accelerate. You can use the speed_data dataset. """
@pytest.mark.parametrize("speed_accelerate", speed_data)
def test_car_accelerate1(speed_accelerate):
    car = Car(50)
    car.accelerate()
    assert car.speed == speed_accelerate

@pytest.mark.parametrize("speed, expected_speed", [(50, 55), (40, 45), (30, 35), (100, 90)])
def test_car_accelerate2(speed, expected_speed):
    car = Car(speed)
    car.accelerate()
    assert car.speed == expected_speed


""" Exercise 1b: Write a parameterized test for brake that receives different speeds and checks the
speed update after brake method is called. Hint: Look up! """
@pytest.mark.parametrize("speed, expected_speed", [(50, 45), (40, 35), (30, 25), (100, 95)])
def test_car_brake2(speed, expected_speed):
    car = Car(speed)
    car.brake()
    assert car.speed == expected_speed

#--------------------------------------------------------------------------------------------------------------------

""" Exercise 2a: Mark this test to be skipped. """
@pytest.mark.skip(reason="For fun")
def test_average_speed():
    car = Car(50)
    car.step()
    assert car.average_speed() == 50


""" Exercise 2b: Write a test and mark it as skippable if Python version is less than 3.7 """
@pytest.mark.skipif("sys.version_info < (3, 7)", reason="Requires Python 3.7 or higher")
def test_to_skip_python_version():
    car = Car(10)
    car.accelerate()
    assert car.speed == 15


""" Exercise 2c: Write a test you expect to fail for any of the car methods and mark it accordingly (provide a reason 
too). """
@pytest.mark.xfail(reason="This test is expected to fail")
def test_to_fail():
    car = Car(10)
    car.accelerate()
    assert car.speed == 20
