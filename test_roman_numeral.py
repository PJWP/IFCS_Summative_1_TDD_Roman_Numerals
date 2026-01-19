from roman_numerals import to_roman

def test_smoke_test():
    assert True

def test_1_is_I():
    assert to_roman(1) == "I"

def test_3_is_III():
    assert to_roman(3) == "III"

def test_2_is_II():
    assert to_roman(2) == "II"

def test_5_is_V_and_6_is_VI():
    assert to_roman(5) == "V"
    assert to_roman(6) == "VI"

def test_10_is_X_and_12_is_XII():
    assert to_roman(10) == "X"
    assert to_roman(12) == "XII"

def test_4_is_IV_and_9_is_IX():
    assert to_roman(4) == "IV"
    assert to_roman(9) == "IX"


