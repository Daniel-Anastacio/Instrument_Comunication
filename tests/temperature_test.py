import serial
from instrument.instrument import Instrument
from usecases.communication import communication
from usecases.watching_temperature import watching_temperature


com1 = serial.Serial("COM1", 9600, timeout=5)
com2 = serial.Serial("COM2", 9600, timeout=5)
notebook = Instrument("Lenovo Ideapad S145", com1)
arduino = Instrument("Arduino UNO R3", com2)

def test_temperature():
    communication(arduino, notebook, "TMP")
    watching_temperature(arduino, notebook, 20)
    assert arduino.temperature in range(0, 2000)
