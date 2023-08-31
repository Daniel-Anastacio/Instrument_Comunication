import serial
from instrument.instrument import Instrument
from usecases.communication import communication
from usecases.watching_current import watching_current


com1 = serial.Serial("COM1", 9600, timeout=5)
com2 = serial.Serial("COM2", 9600, timeout=5)
notebook = Instrument("Samsung Expert X40", com1)
arduino = Instrument("Arduino UNO R3", com2)

def test_current():
    communication(arduino, notebook, "CUR")
    watching_current(arduino, notebook, 20)
    assert arduino.current in range(0, 2000)
