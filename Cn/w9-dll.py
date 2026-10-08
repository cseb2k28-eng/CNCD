def character_framing(data):
    return "FLAG" + data + "FLAG"

def character_stuffing(data):
    result = "FLAG"
    for ch in data:
        if ch == "F" or ch == "E":
            result += "E"
        result += ch
    return result + "FLAG"

def bit_stuffing(data):
    result = ""
    count = 0
    for bit in data:
        result += bit
        if bit == "1":
            count += 1
            if count == 5:
                result += "0"
                count = 0
        else:
            count = 0

    return "01111110" + result + "01111110"

data = input("Enter character data: ")
bits = input("Enter bit data: ")

print("Character Framing:", character_framing(data))
print("Character Stuffing:", character_stuffing(data))
print("Bit Stuffing:", bit_stuffing(bits))

# Input
# Enter character data: ABC
# Enter bit data: 11111011111

# Output
# Character Framing: FLAGABCFLAG
# Character Stuffing: FLAGABCFLAG
# Bit Stuffing: 011111100111110011111001111110