import random
import time

from instrument.instrument import Instrument
from usecases.communication import communication


def watching_voltage(instrument: Instrument, computer: Instrument, times: int):
    """Monitors the voltage of an instrument.

    Args:
        instrument(Instrument): The monitored instrument.
        computer(Instrument): The computer that will monitor the instrument.
        times(int): Number of times the monitoring will happen.
    """
    for _ in range(0, times):
        communication(instrument, computer, "VOL")
        computer.general_store(computer.vtg_list, "voltage")
        instrument.voltage = random.randint(0, 2000)
        time.sleep(1.0)

