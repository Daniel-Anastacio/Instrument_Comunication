from usecases.management_measurement import manage_measurement

class MockInstrument:
    def __init__(self):
        self.data_dict = {
            "current": [],
            "temperature": [],
            "voltage": [],
            "type": [],
            "status": []
        }

    def read_message(self):
        return "Simulated instrument response"

    def write_response(self, response):
        pass

class MockComputer(MockInstrument):
    def general_store(self, data_list, specification):
        data_list.append("Simulated computer data")

def test_manage_measurement():
    instrument = MockInstrument()
    computer = MockComputer()

    manage_measurement(instrument, computer)
    check_data_storage(computer.data_dict)

def check_data_storage(data_dict):
    assert len(data_dict["current"]) == 20
    assert len(data_dict["temperature"]) == 20
    assert len(data_dict["voltage"]) == 20
    assert len(data_dict["type"]) == 5
    assert len(data_dict["status"]) == 5

test_manage_measurement()