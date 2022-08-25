inputString = "1c0111001f010100061a024b53535009181c"
against = "686974207468652062756c6c277320657965"

def xorHex(hexOne, hexTwo):
    result = int(inputString, base=16) ^ int(hexTwo, base=16)
    result = hex(result)[2:]
    return result

assert xorHex(inputString, against) == "746865206b696420646f6e277420706c6179"
