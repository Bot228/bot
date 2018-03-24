from typing import Union, Tuple



def get_username(text: str) -> Union[str, None]:
    try:
        return text.split()[1]
    except IndexError:
        return None


def get_cats_args(message_text):
    args = message_text.split()
    return int(args[1])


def get_text_args(message_text : str) -> str:
    return message_text[len("/advert"):].strip()


def get_set_name_args(message_text) -> Tuple:
    args = message_text.split()
    if len(args) < 4:
        return None, None
    username = args[1]
    new_name = str(args[2] + ' ' + args[3])
    return username, new_name

def get_delete_args(message_text):
    args = message_text.split()
    return args[1], args[2]

