class TemperatureError(Exception):
    """Customized exception that inherits the Exception class.

    Args:
        Exception (type): Class for exceptions in python.
    """
    pass


class VoltageError(Exception):
    """Customized exception that inherits the Exception class.

    Args:
        Exception (type): Class for exceptions in python.
    """
    pass


def temperature_exception(temperatures: list[int]) -> None:
    """Exception of temperatures.

    Args:
        temperatures (list[int]): List of generated temperatures.

    Raises:
        TemperatureError: This error is raised when an element in the temperature list is greater than 80 degrees.
    """
    for temperature in temperatures:
        if temperature > 80:
            raise TemperatureError("Temperature greater than 80° found!")


def voltage_exception(voltages: list[int]) -> None:
    """Exception of voltages.

    Args:
        voltages (list[int]): List of generated voltages.

    Raises:
        VoltageError:This error is raised when an element in the voltage list is greater than 190 volts.
    """
    for voltage in voltages:
        if voltage == 0:
            print("Voltage equal 0V found!")
        elif voltage > 190:
            raise VoltageError("Voltage greater than 190V found!")
