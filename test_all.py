from L1_return_statements import return_hello_world
from L2_return_number import return_number_between_1_and_10
from L3_inputs import return_hello_name
from L4_return_addition import return_addition
from L5_return_list import return_list_of_numbers_inbetween


def test_return_hello_world():
    actual = return_hello_world()
    expected = [
        "Hello, World!",
        "hello, world!",
        "hello world",
    ]

    assert actual in expected, f"Expected one of {expected} but got {actual}"


def test_return_number():
    actual = return_number_between_1_and_10()
    expected = list(range(1, 11))

    assert actual in expected, f"Expected one of {expected} but got {actual}"


def test_return_name():
    actual = return_hello_name("John")
    expected = [
        "Hello, John!",
        "hello, John!",
        "hello John",
    ]

    assert actual in expected, f"Expected one of {expected} but got {actual}"


def test_return_addition():

    actual = return_addition(1, 2)
    expected = 3

    assert actual == expected, f"Expected {expected} but got {actual}"

def test_return_list():
    actual = return_list_of_numbers_inbetween(1, 10)
    expected = list(range(1, 10))

    assert actual == expected, f"Expected {expected} but got {actual}"


