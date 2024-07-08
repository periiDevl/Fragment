from collections import namedtuple
from rich import print
class Object:
    def __init__(self, x, y, z, scaleX, scaleY, scaleZ):
        self.x = x
        self.y = y
        self.z = z
        self.scaleX = scaleX
        self.scaleY = scaleY
        self.scaleZ = scaleZ

def read_file_char_by_char(filename):
    """
    Opens a file in read mode, prints each character, and saves them to a list.

    Args:
        filename: The name of the file to read.

    Returns:
        A list of characters read from the file.
    """
    tokens = []
    try:
        with open(filename, 'r') as file:
            char = file.read(1)  # Read one character at a time
            while char:
                print(char, end='')  # Print the character without a newline
                tokens.append(char)  # Add the character to the list
                char = file.read(1)  # Read the next character
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

    return tokens

def FindWord(word, i, tokens):
    for j in range(len(word)):
        if word[j] != tokens[i + j]:
            return False
    return True

def parse_file(filename, objects):
    # Read the file and get the tokens
    tokens = read_file_char_by_char(filename)
    print("\nCharacters saved in a list:")
    print(tokens)

    
    objectType = "null"
    objectName = ""
    objectOpened = False
    objectReadyToShip = False
    variableType = "null"
    variableOpended = False
    variableClosed = False
    variableContent = ""
    obj = Object(0, 0, 0, 0, 0, 0)

    for i in range(len(tokens) - 1):
        if tokens[i] == "#" or (tokens[i] == "." and objectType == "null"):
            print("Detected a comment object wainting for opener")
            objectType = tokens[i]
            objectReadyToShip = False
        
        if tokens[i] == "{" and not objectReadyToShip:
            print("Opener detected for :" + objectType)
            objectOpened = True
            print("Name for the object was decided to be : " + objectName)
        
        if objectType != "null" and not objectOpened and not objectReadyToShip and tokens[i] != objectType:
            objectName += tokens[i]
        
        if objectOpened and not objectReadyToShip:
            if objectType == ".":
                if tokens[i] in ["x", "y", "z"]:
                    if variableType == "null":
                        variableType = tokens[i]
                elif FindWord("sx", i, tokens) or FindWord("sy", i, tokens) or FindWord("sz", i, tokens):
                    if variableType == "null":
                        variableType = tokens[i] + tokens[i + 1]
                elif tokens[i] == "[":
                    variableOpended = True
                    variableClosed = False
                elif tokens[i] == "]" and variableOpended:
                    if variableType == "sx":
                        obj.scaleX = variableContent
                    elif variableType == "x":
                        obj.x = variableContent
                    elif variableType == "y":
                        obj.y = variableContent
                    elif variableType == "sx":
                        obj.scaleX = variableContent
                    elif variableType == "sy":
                        obj.scaleY = variableContent
                    elif variableType == "sz":
                        obj.scaleZ = variableContent
                    variableClosed = True
                    variableOpended = False
                    print("[green]Variable : " + variableType + " variable content : " + variableContent)
                    variableType = "null"
                    variableContent = ""
                if variableOpended and not variableClosed and tokens[i] != "[":
                    variableContent += tokens[i]
        
        if tokens[i] == "}" and objectOpened and objectType != "null" and objectName != "" and not objectReadyToShip:
            objectReadyToShip = True
            objects.append(obj)
            print("[blue]Object type :" + objectType + " with the name " + objectName + " was detected.")
            objectType = "null"
            objectName = ""
            objectOpened = False



