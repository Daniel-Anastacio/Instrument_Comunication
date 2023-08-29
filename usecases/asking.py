def asking(ask: str) -> bool:
    """A function that asks the user if he/she wants to continue executing the program.

    Returns:
        bool: Indicates the procedure that the execution of the program will have (`True` indicates "continue" and `False` indicates "terminate").
    """
    if ask == "yes":
        return True
    elif ask == "no":
        return False
    else:
        return False
