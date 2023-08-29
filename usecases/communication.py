from instrument.instrument import Instrument


def communication(instrument: Instrument, computer: Instrument, request: str):
    """
    The method that is responsible for carrying out the communication between an instrument and a computer.

    Args:
        instrument (Instrument): The Instrument object used to send commands and read messages.
        computer (Instrument): The Instrument object used to write responses.
        request (str): The command responsible for the request that will be sent to the instrument.
    """
        
    computer.write_response(request)
    instrument.read_message()
