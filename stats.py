def get_book_text(raamat):
    with open(raamat, "r") as f:
        content = f.read()
        #print(content)
    return content

def count_words(raamat):
    text = get_book_text(raamat)
    sõnad = text.split()
    return f"Found {len(sõnad)} total words"

def count_letters(raamat):
    text = get_book_text(raamat).casefold()
    #kõik_tähed = list(text)
    tähed = set(text)
    loetud_tähed = {}
    for täht in tähed:
        loetud_tähed[täht] = text.count(täht)
        text = text.replace(täht, "")
        sotred_tähed = dict(sorted(loetud_tähed.items(), key=lambda item: item[1], reverse=True))
    return sotred_tähed # type: ignore