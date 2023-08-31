import serial
from instrument.instrument import Instrument

com1 = serial.Serial("COM1", 9600, timeout=5)
com2 = serial.Serial("COM2", 9600, timeout=5)
notebook = Instrument("Lenovo Ideapad S145", com1)
arduino = Instrument("Arduino UNO R3", com2)
