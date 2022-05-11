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


def extract(text: str, before: str, after: str):
    """before と afterに挟まれた単語を抽出する

    Args:
        text (str): _description_
        before (str): _description_
        after (str): _description_

    Returns:
        _type_: _description_
    """
    regex = f'{before}(\w+){after}'
    matches = re.findall(regex, text)
    return matches[0] if len(matches) > 0 else ""


if __name__ == '__main__':
    print(extract("hogefugahogemiga", "fuga", 'miga'))
