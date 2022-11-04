import pytest
from AnotherSample import sum

# Delete __init__.py file from the pytest folder to avoid
# the error: "ModuleNotFoundError: No module named 'AnotherSample'"
@pytest.mark.parametrize(
    'input1,input2,output',
    [
        (2, 3, 5),
        (0, -5, -5),
        (3, 3, 6)
    ]
)
def test_sum(input1, input2, output):
    assert sum(input1, input2) == output, f'it should be {output}!'

# def test_sum_1():
#     result = sum(2, 3)
#     assert result == 5, 'It should be 5!.'
#
# def test_sum_2 ():
#     result = sum(0, -5)
#     assert result == -5, 'It should be -5!.'
#
# def test_sum_3():
#     result = sum(3, 3)
#     assert result == 6, 'It should be 6!.'