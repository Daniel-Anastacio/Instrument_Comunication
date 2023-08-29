import random

import serial


class Instrument:
    """Simulated instrument class that reads and writes messages to a serial port.

    This class simulates an instrument that communicates through a serial port.
    It generates random values for status, type, voltage, temperature, and current.
    It can read messages from the serial port and respond accordingly.

    Attributes:
        status (int): A random status value.
        type (str): A random type value.
        voltage (int): A random voltage value.
        temperature (int): A random temperature value.
        current (int): A random current value.
        tmp_list(list[int]): A list that stores temperature values.

    Args:
        name (str): The instrument's name.
        ser (serial.Serial): An instance of the `serial.Serial` class representing the serial port.
    """

    def __init__(self, name: str, ser: serial.Serial) -> None:
        """Initialize the Instrument with random attribute values and a serial port.

        Args:
            name (str): The instrument's name.
            ser (serial.Serial): An instance of the `serial.Serial` class representing the serial port.
        """
        self.name = name
        self.ser = ser

        self.status = random.randint(0, 0xFFFFFFFF)
        self.type = random.choice(["a", "b", "c", "abc"])
        self.voltage = random.randint(0, 220)
        self.temperature = random.randint(0, 85)
        self.current = random.randint(0, 2000)

        self.tmp_list: list[int] = []
        self.vtg_list: list[int] = []
        self.cur_list: list[int] = []
        self.data_dict: {str: list[int]} = {"status": [], "type": [], "voltage": [], "temperature": [], "current": []}

    def read_message(self) -> None:
        """Read a message from the serial port and respond accordingly.

        This method reads a message from the serial port and processes it based on
        the command. It can respond with the status, type, voltage, temperature, or
        current based on the command received.

        Raises:
            ValueError: If an unknown command is received.
        """
        command = self.ser.readline().decode()[:3]
        if command == "STA":
            self.write_response(str(self.status))
        elif command == "TYP":
            self.write_response(str(self.type))
        elif command == "VOL":
            self.write_response(str(self.voltage))
        elif command == "TMP":
            self.write_response(str(self.temperature))
        elif command == "CUR":
            self.write_response(str(self.current))
        else:
            raise ValueError(f"Unknown command: {command}")

    def write_response(self, response: str) -> None:
        """Write a response to the serial port.

        This method writes a response to the serial port. The response is sent as bytes
        using the UTF-8 encoding.

        Args:
            response (str): The response to be sent.

        Example:
            >>> instrument = Instrument(ser)
            >>> instrument.write_response("Response message")
        """
        self.ser.write(bytearray(response + "\r\n", "UTF-8"))

    def specific_store(self, list: list, element: any) -> None:
        """Minimum unit of information that can be of string or integer type.

        Args:
            list (list): This list will receive the element as a unit.
            element (any): Minimum unit of information that can be of string or integer type.
        """
        list.append(element)
        print(f"Received : {list} ")

    def general_store(self, list: list, specification: str) -> None:
        """General function that specifies the specific storage type.

        Args:
            list (list): This list will receive the element as a unit.
            specification (str): Specification of the type of storage that will be used.
        """
        try:
            absolute_element = int(self.ser.readline().decode())
        except:
            absolute_element = self.ser.readline().decode()
        if specification == "current specified":
            print(absolute_element)
            if absolute_element < 25:
                print("Threshold alert!")
            elif absolute_element >= 25 and absolute_element <= 800:
                self.specific_store(list, absolute_element)
            
        elif specification == "current normal":
            self.specific_store(list, self.current)
            self.current = random.randint(0, 2000)
        elif specification == "temperature":
            self.specific_store(list, self.temperature)
            self.temperature = random.randint(0, 85)
        elif specification == "voltage":
            self.specific_store(list, self.voltage)
            self.voltage = random.randint(0, 220)
        elif specification == "status":
            self.specific_store(list, self.status)
            self.status = random.randint(0, 0xFFFFFF)
        elif specification == "type":
            self.specific_store(list, self.type)
            self.type = random.choice(["a", "b", "c", "abc"])
