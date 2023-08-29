import serial, pytest, random
from instrument.instrument import Instrument
from usecases.communication import communication
from usecases.watching_temperature import watching_temperature
from instrument.exceptions import temperature_exception, TemperatureError, voltage_exception, VoltageError
from usecases.watching_voltage import watching_voltage

com1 = serial.Serial("COM1", 9600, timeout=5)
com2 = serial.Serial("COM2", 9600, timeout=5)
notebook = Instrument("Lenovo Ideapad S145", com1)
arduino = Instrument("Arduino UNO R3", com2)


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
