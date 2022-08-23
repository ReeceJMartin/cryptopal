import base64

def hexTo64(hex):
    conversion = bytes.fromhex(hex).decode("utf-8")
    conversion = base64.b64encode(bytes(conversion, "utf-8"))
    conversion = conversion.decode("ascii")
    return conversion

inputString = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

outputString = hexTo64(inputString)

print(outputString)