import random

import pytest
from instrument.exceptions import TemperatureError, VoltageError, temperature_exception, voltage_exception
from tests import arduino, notebook
from usecases.communication import communication
from usecases.watching_temperature import watching_temperature
from usecases.watching_voltage import watching_voltage


def test_temperature_exception():
    communication(arduino, notebook, "TMP")
    watching_temperature(arduino, notebook, 20)
    arduino.tmp_list.append(random.randint(80, 2000))
    with pytest.raises(TemperatureError):
        temperature_exception(arduino.tmp_list)


def test_voltage_exception():
    communication(arduino, notebook, "VOL")
    watching_voltage(arduino, notebook, 20)
    arduino.vtg_list.append(random.randint(190, 2000))
    with pytest.raises(VoltageError):
        voltage_exception(arduino.vtg_list)
