def rgb_hex():
    invalid_msg = "Invalid error"
    red = int(input("Enter a red value (>0, and <255): "))
    if red < 0 or red > 255:
        print(invalid_msg)
        return
    green = int(input("Enter a green value (>0, and <255): "))
    if green < 0 or green > 255:
        print(invalid_msg)
        return
    blue = int(input("Enter a blue value (>0, and <255)5: "))
    if blue < 0 or blue > 255:
        print(invalid_msg)
        return
    val = (red << 16) + (green << 8) + blue
    print("%s" % (hex(val)[2:]).upper())


def hex_rgb():
    hex_val = input("Enter a hex value (6 digits): ")
    if len(hex_val) != 6:
        print(invalid_msg)
    return
    else:
        hex_val = int(hex_val, 16)
        two_hex_digits = 2**8
        blue = hex_val % two_hex_digits
        hex_val = hex_val >> 8
        green = hex_val % two_hex_digits
        hex_val = hex_val >> 8
        red = hex_val % two_hex_digits
        print("Red: %s Green: %s Blue: %s" % (blue, green, red))


def convert():
    while True:
        option = input("Enter 1 to conovert RGB to HEX, Enter 2 to convert HEX to RGB, Enter X to Exit: ").upper()
    if option == "1":
        print("RGB to HEX... ")
        rgb_hex()
    elif option == "2":
        print("HEX to RGB...")
        hex_rgb()
    elif option == "X":
        break
    else:
        print("Error")


convert()
