import pytest

# To use this marks, you need to create an ini file in the same directory with the following lines:
# [pytest]
# markers =
#     windows: Only for Windows systems.
#     mac: Only for MAC systems.
@pytest.mark.windows
def test_windows_1():
    assert True

@pytest.mark.windows
def test_windows_2():
    assert True

@pytest.mark.mac
def test_mac_1():
    assert True

@pytest.mark.mac
def test_mac_2():
    assert True
