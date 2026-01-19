ROMAN_PAIRS = [("X",10),("IX",9),("V",5),("IV",4),("I",1)]

def to_roman(num):
    result = []
    remaining = num
    for symbol, value in ROMAN_PAIRS:
        count = remaining // value
        remaining = remaining % value
        if count > 0:
            result.append(symbol*count)
        if remaining == 0:
            break
    return "".join(result)

