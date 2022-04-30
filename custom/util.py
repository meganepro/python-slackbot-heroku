import re


def is_include(text: str, target: str):
    """targetの文字列がtextに含まれているかをチェックする

    Args:
        text (str): _description_
        target (str): _description_

    Returns:
        _type_: _description_
    """
    return True if len(re.findall(target, text)) > 0 else False
