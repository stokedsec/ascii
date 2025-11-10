import PIL.Image


# List of ASCII characters in order of space filled
SYMBOLS = ["@", "%", "#", "*", "+", "=", ":", "-", ".", " "]
# List of Unicode characters in order of space filled
UNICODE = ["█", "█", "▓", "▓", "▒", "▒", "░", "░", "┉", "┉", " "]

def basicProcess(img, charSet):

    # Define vars
    pixels = img.getData()
    characters = []
    brightnessFactor = 255/len(charSet)
    formattedString = ""

    # Create raw data
    for pixel in pixels:
        brightnessVal = round(pixel / brightnessFactor)
        characters.append(charSet[brightnessVal])

    # Organize into rows and columns
    for i in range(1, len(characters) + 1):
        if i % img.width == 0:
            formattedString += "\n"
        formattedString += characters[i]

    return formattedString
