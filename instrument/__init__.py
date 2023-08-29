from instrument.exceptions import temperature_exception, voltage_exception

# from instrument.functions import general_store, store_current, store_temperature, store_voltage
# from instrument.instrument import Instrument


def menu() -> None:
    """Generates a selection menu."""
    print("• Available options:")
    print("[1] Temperature (TMP)")
    print("[2] Voltage (VOL)")
    print("[3] All Data (ALL)")
    print("[4] Current (CUR)")


def line(style: str, qntd: int) -> None:
    print(style * qntd)
