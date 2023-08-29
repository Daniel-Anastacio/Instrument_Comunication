import time
import random
from instrument.instrument import Instrument
from usecases.communication import communication

def watching_current(instrument: Instrument,computer:Instrument, times: int):
    """Monitors the electrical current of an instrument.

    Args:
        instrument(Instrument): The monitored instrument.
        computer(Instrument): The computer that will monitor the instrument.
        times(int): Number of times the monitoring will happen.
    """
    while len(computer.cur_list) < times:
        communication(instrument, computer, "CUR")
        computer.general_store(computer.cur_list, "current specified")
        instrument.current = random.randint(0, 2000)
        time.sleep(1.0)
