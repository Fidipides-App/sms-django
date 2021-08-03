def format_phone_number(phone: str) -> str:
    """Returns the phone number with the international preffix"""

    number = str("+351") + str(phone)
    return number
