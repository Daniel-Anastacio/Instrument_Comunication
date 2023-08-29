import time
import random
from instrument.instrument import Instrument
from usecases.communication import communication
from usecases.asking import asking


def watching_temperature(instrument: Instrument, computer:Instrument, times: int):
    """A function that monitors the temperatures of external equipment, checking its current temperature and storing it in a list.

    Args:
        instrument (Instrument): The external equipment that will be analyzed by a machine.
        computer (Instrument): The machine that will analyze data from an external device.
        times (int): The number of times a temperature will be stored.
    """
    for _ in range(0, times):
        communication(instrument, computer, "VOL")
        computer.general_store(computer.tmp_list, "temperature")
        instrument.temperature = random.randint(0, 2000)
        time.sleep(1.0)
    
    answer: bool = asking("no")
    if answer:
        watching_temperature(instrument, computer, times)
    else:
        pass
