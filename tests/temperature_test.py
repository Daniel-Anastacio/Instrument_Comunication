from tests import arduino, notebook
from usecases.communication import communication
from usecases.watching_temperature import watching_temperature


def test_temperature():
    communication(arduino, notebook, "TMP")
    watching_temperature(arduino, notebook, 20)
    assert arduino.temperature in range(0, 2000)
