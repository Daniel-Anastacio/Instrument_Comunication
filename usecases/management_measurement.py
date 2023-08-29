import time
import random
from instrument.instrument import Instrument
from usecases.communication import communication


def manage_measurement(instrument: Instrument, computer: Instrument) -> None:
    """Method responsible for making measurements, communications and data 
    management between an instrument and a computer.

    Args:
        instrument (Instrument): The Instrument object used to perform simulation measurements.
        computer (Instrument): The Instrument object used for data storage and communication.
    """

    for _ in range(0, 20):
        communication(instrument, computer, "CUR")
        computer.general_store(computer.data_dict["current"], "current normal")
        communication(instrument, computer, "TMP")
        computer.general_store(computer.data_dict["temperature"], "temperature")
        communication(instrument, computer, "VOL")
        computer.general_store(computer.data_dict["voltage"], "voltage")
        instrument.current = random.randint(0, 2000)
        instrument.voltage = random.randint(0, 220)
        instrument.temperature = random.randint(0, 85)
        time.sleep(1.0)
    for _ in range(0, 5):
        communication(instrument, computer, "TYP")
        computer.general_store(computer.data_dict["type"], "type")
        communication(instrument, computer, "STA")
        computer.general_store(computer.data_dict["status"], "status")
        instrument.temperature = random.randint(0, 0xFFFFFF)
        instrument.temperature = random.choice(["a", "b", "c", "abc"])
    print(60 * "-", f"\n{computer.data_dict}")
