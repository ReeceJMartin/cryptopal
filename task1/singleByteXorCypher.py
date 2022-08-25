# Input String
hexChars = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"


def bruteforceKey(hexInput):

    # Convert that input string to a utf-8 equivilant string 
    conversion = bytes.fromhex(hexInput).decode("utf-8")

    # Bruteforce search by all possible keys

    for key in range(128):

        converted = ""

        # XOR every character with current Key
        for character in conversion:

            try: 

                xored = int(hex(ord(character)), 16) ^ key

                xoredString = bytes.fromhex(hex(xored)[2:]).decode("utf-8")

                converted = converted + str(xoredString)

            except:
                continue


        # Output the decrypted message with the current key
        
        print(hex(key)+":")
        print(converted+"\n")


bruteforceKey(hexInput=hexChars)