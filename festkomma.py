# Calculates binary, hexadecimal and decimal representations of decimal floating point numbers


hexadecimals = {
        "0000": "0",
        "0001": "1",
        "0010": "2",
        "0011": "3",
        "0100": "4",
        "0101": "5",
        "0110": "6",
        "0111": "7",
        "1000": "8",
        "1001": "9",
        "1010": "A",
        "1011": "B",
        "1100": "C",
        "1101": "D",
        "1110": "E",
        "1111": "F"
        }


def binary(num: float, vorkomma: int, nachkomma: int) -> str:
    out: str = ""
    for i in range(vorkomma):
        index = vorkomma - i - 1
        if num > 2 ** index:
            num = num - 2 ** index
            out = out + "1"
        else:
            out = out + "0"
    
    for i in range(nachkomma):
        index = -i - 1
        if num > 2 ** index:
            num = num - 2 ** index
            out = out + "1"
        else:
            out = out + "0"

    print(out[:vorkomma] + "." + out[vorkomma:])

    return out


# Ich bin zu faul also wird das nur für strings mit durch 4 teilbarer länge funktionieren
def hexadecimal(string: str) -> str:
    out: str = ""
    for i in range(int(len(string) / 4)):
        out = out + hexadecimals[string[i * 4: (i + 1) * 4]]
    print("0x" + out)
    return out


def decimal(string: str) -> str:
    out: int = 0
    for i in range(len(string)):
        out += int(string[len(string) - 1 - i]) * 2 ** i 
    print(out)
    return(str(out))


def calculateAll(num: float, vorkomma: int, nachkomma: int):
    print(f"The binary, hexadecimal and decimal representations of {num} interpreted as a {vorkomma}.{nachkomma} binary number are:")
    string = binary(num, vorkomma, nachkomma)
    hexadecimal(string)
    decimal(string)


if __name__ == '__main__':
    calculateAll(3.141592, 8, 8)
