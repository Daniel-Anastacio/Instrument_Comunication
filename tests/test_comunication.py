from instrument.instrument import Instrument
from usecases.communication import communication

class MockInstrument(Instrument):
    def __init__(self, name, ser):
        super().__init__(name, ser)

    def read_message(self):
        return "Response from instrument"

    def write_response(self, response):
        pass

def test_communication_with_invalid_request():
    instrument = MockInstrument(name="InstrumentName", ser=None)  
    computer = MockInstrument(name="ComputerName", ser=None)

    request = "Invalid command"
    result = communication(instrument, computer, request)

    assert result == "Invalid command not recognized"

def test_communication_with_instrument_unavailable():
    instrument = None
    computer = MockInstrument(name="ComputerName", ser=None)

    request = "Test command"
    result = communication(instrument, computer, request)

    assert result == "Instrument not available"

def test_communication_with_computer_unavailable():
    instrument = MockInstrument(name="InstrumentName", ser=None)
    computer = None

    request = "Test command"
    result = communication(instrument, computer, request)

    assert result == "Computer not available"