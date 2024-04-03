import pytest
from car import Car

""" Exercise 0a: Write a fixture that returns a car instance. """
@pytest.fixture
def my_car():
    return Car(50)


def test_car_accelerate(my_car):
    """ Exercise 0b: Using the just created fixture test the accelerate method. Hint: accelerate, then check. """
    # TODO


def test_car_brake(my_car):
    """ Exercise 0c: Using the just created fixture test the brake method. Hint: break, then check. """
    # TODO

#--------------------------------------------------------------------------------------------------------------------

speed_data = {45, 50, 75, 45}

@pytest.mark.parametrize("speed_brake", speed_data)
def test_car_brake(speed_brake):
    car = Car(50)
    car.brake()
    assert car.speed == speed_brake


""" Exercise 1a: Write a parameterized test for accelerate. You can use the speed_data dataset. """

# TODO


@pytest.mark.parametrize("speed, expected_speed", [(50, 55), (40, 45), (30, 35), (100, 90)])
def test_car_accelerate(speed, expected_speed):
    car = Car(speed)
    car.accelerate()
    assert car.speed == expected_speed


""" Exercise 1b: Write a parameterized test for brake that receives different speeds and checks the
speed update after brake method is called. Hint: Look up! """
# TODO

#--------------------------------------------------------------------------------------------------------------------

""" Exercise 2a: Mark this test to be skipped. """
# TODO
def test_average_speed():
    car = Car(50)
    car.step()
    assert car.average_speed() == 50


""" Exercise 2b: Write a test and mark it as skippable if Python version is less than 3.7 """
# TODO


""" Exercise 2c: Write a test you expect to fail for any of the car methods and mark it accordingly (provide a reason 
too). """
# TODO
