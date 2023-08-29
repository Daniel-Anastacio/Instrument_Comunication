import time

import serial
from instrument.instrument import Instrument
from instrument import (
    line,
    menu,
    temperature_exception,
    voltage_exception
)
from usecases.management_measurement import manage_measurement
from usecases.communication import communication
from usecases.watching_temperature import watching_temperature
from usecases.watching_voltage import watching_voltage
from usecases.watching_current import watching_current

if __name__ == "__main__":
    cont: int = 0
    com1 = serial.Serial("COM1", 9600, timeout=5)
    com2 = serial.Serial("COM2", 9600, timeout=5)

    notebook = Instrument("Lenovo Ideapad S145", com1)
    arduino = Instrument("Arduino UNO R3", com2)

    line("-", 60)
    menu()
    command = int(input("- Choose an option: "))
    line("-", 60)

    if command == 1:
        communication(arduino, notebook,"TMP")
        watching_temperature(arduino, notebook, 20)
        temperature_exception(notebook.tmp_list)
    elif command == 2:
        watching_voltage(arduino, notebook, 20)
        voltage_exception(notebook.vtg_list)
    elif command == 3:
        # communication(arduino, notebook,"CUR")
        manage_measurement(arduino, notebook)
        time.sleep(1.0)
    elif command == 4:
        watching_current(arduino,notebook, 30)
    else:
        print("Invalid Option!")

    com1.close()
    com2.close()
