import pytest
from tests import arduino, notebook

def test_when_notebook_writes_a_unknown_command_then_arduino_should_reads_the_message_and_return_a_error():
    notebook.write_response('Message')
    with pytest.raises(ValueError):
        arduino.read_message()

def test_when_notebook_writes_a_valid_command_arduino_should_reads_the_message_and_incorporate_a_property():
    notebook.write_response("STA")
    arduino.read_message()
    assert arduino.status == int(notebook.ser.readline().decode())
    notebook.write_response("TYP")
    arduino.read_message()
    assert arduino.type+'\r\n' == str(notebook.ser.readline().decode())
    notebook.write_response("TMP")
    arduino.read_message()
    assert arduino.temperature == int(notebook.ser.readline().decode())
    notebook.write_response("VOL")
    arduino.read_message()
    assert arduino.voltage == int(notebook.ser.readline().decode())
    notebook.write_response("CUR")
    arduino.read_message()
    assert arduino.current == int(notebook.ser.readline().decode())
    print(notebook.ser.readline().decode())

def test_when_a_data_should_be_stored_specifically():
    arduino.specific_store(arduino.vtg_list, 70)
    assert len(arduino.vtg_list) == 1
    assert arduino.vtg_list == [70]

def test_when_a_general_data_should_be_stored_specifically_then_checks_data():
    notebook.write_response("TMP")
    arduino.read_message()
    arduino.general_store(arduino.tmp_list, "temperature")
    assert len(arduino.tmp_list) == 1
    assert type(arduino.tmp_list[0]) == int

