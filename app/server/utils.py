import secrets
import string
from server.exceptions import NegativeValueError


async def generate_alphanum_password(max_len):
    """
    Using secret module to generate random password
    :param max_len: int
    :return: str
    """
    if max_len < 0:
        raise NegativeValueError

    character_set = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(character_set) for i in range(max_len))

    return password
