ROMAN_PAIRS = [
    ("M",1000),("CM",900),("D",500),("CD",400),
    ("C",100),("XC",90),("L",50),("XL",40),
    ("X",10),("IX",9),("V",5),("IV",4),
    ("I",1)
               ]

def to_roman(num):
    if num != int(num):
        return "Error: Input must be an integer"
    if num <= 0 or num >= 4000:
        return "Error: Input must be between 1 and 3999"

    num = int(num)
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

