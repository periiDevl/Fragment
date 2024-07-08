from collections import namedtuple
from rich import print
import os
class Object:
    def __init__(self, x, y, z,rotx, roty, rotz, scaleX, scaleY, scaleZ, path, draw, static):
        self.x = x
        self.y = y
        self.z = z
        self.scaleX = scaleX
        self.scaleY = scaleY
        self.scaleZ = scaleZ
        self.rotx = rotx
        self.roty = roty
        self.rotz = rotz
        self.path = path
        self.draw = draw
        self.static = static

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
def build_word(i, tokens, lenn):
    variableType = tokens[i]
    for j in range(1, lenn):
        if i + j < len(tokens):
            variableType += tokens[i + j]
    return variableType
def find_word(word, i, tokens):
    for j in range(len(word)):
        if word[j] != tokens[i + j]:
            return False
    return True
def read_and_update_objects(filename):
    global objects
    tokens = read_file_char_by_char(filename)
    print("\nCharacters saved in a list:")
    print(tokens)
    variables = []
    objects = []
    objectType = "null"
    objectName = ""
    objectOpened = False
    objectReadyToShip = False
    variableType = "null"
    variableOpened = False
    variableClosed = False
    variableContent = ""
    
    for i in range(len(tokens) - 1):
        if tokens[i] in ["@", "."] and objectType == "null":
            print("Detected a comment object waiting for opener")
            objectType = tokens[i]
            objectReadyToShip = False
        elif find_word("/.", i, tokens) and objectType == "null":
            for j in range(2):
                print("Detected a comment object waiting for opener")
                objectType = tokens[i] + tokens[i + j]
                objectReadyToShip = False
        
                
        if tokens[i] == "{" and not objectReadyToShip:
            print(f"Opener detected for: {objectType}")
            objectOpened = True
            print(f"Name for the object was decided to be: {objectName}")
            obj = Object(0, 0, 0, 0, 0, 0,0,0,0,"",1,1)  # Create a new instance of Object here
        
        if objectType != "null" and not objectOpened and not objectReadyToShip and tokens[i].isalnum() :
            objectName += tokens[i]
        
        if objectOpened and not objectReadyToShip:
            if objectType == "@":
                variableContent += tokens[i]
            elif objectType == "." or objectType == "/.":
                if tokens[i] == "x" or tokens[i] == "y" or tokens[i] == "z":
                    if variableType == "null":
                        variableType = tokens[i]
                elif find_word("sx", i, tokens) or find_word("sy", i, tokens) or find_word("sz", i, tokens):
                    if variableType == "null":
                        for j in range(2):
                            variableType = tokens[i] + tokens[i + j]
                elif find_word("rotx", i, tokens) or find_word("roty", i, tokens) or find_word("rotz", i, tokens) or find_word("path", i, tokens) or find_word("draw", i, tokens):
                    if variableType == "null":
                        variableType = build_word(i, tokens, 4)
                elif tokens[i] == "[":
                    variableOpened = True
                    variableClosed = False
                elif tokens[i] == "]" and variableOpened:
                    print("[red]" + str(variableContent))
                    if variableType == "sx":
                        obj.scaleX = variableContent
                    elif variableType == "x":
                        obj.x = variableContent
                        print("[red]" + obj.x)
                    elif variableType == "y":
                        obj.y = variableContent
                    elif variableType == "z":
                        obj.z = variableContent
                    elif variableType == "sy":
                        obj.scaleY = variableContent
                    elif variableType == "sz":
                        obj.scaleZ = variableContent
                    elif variableType == "rotx":
                        obj.rotx = variableContent
                    elif variableType == "roty":
                        obj.roty = variableContent
                    elif variableType == "rotz":
                        obj.rotz = variableContent
                    elif variableType == "path":
                        obj.path = variableContent[1:-1]
                    elif variableType == "draw":
                        obj.draw = variableContent
                    
                    if objectType == "/.":
                        obj.static = 0
                    variableClosed = True
                    variableOpened = False
                    print(f"[green]Variable: {variableType} variable content: {variableContent}")
                    variableType = "null"
                    variableContent = ""
                
                if variableOpened and not variableClosed and tokens[i] != "[":
                    variableContent += tokens[i]

                    if variableContent == "true":
                        variableContent = 1
                    if variableContent == "false":
                        variableContent = 0
                    for vari in range(len(variables) - 1):
                        if not vari % 2:
                            if variableContent == variables[vari]:
                                variableContent = variables[vari + 1]
        if tokens[i] == "}" and objectOpened and objectType != "null" and objectName and not objectReadyToShip:
            if objectType == "@":
                variables.append(objectName)
                variables.append(variableContent[1:-1])
                variableContent = ""
            objectReadyToShip = True
            if objectType == "." or objectType == "/.":
                objects.append(obj)
            print(obj.x)
            print(f"[blue]Object type: {objectType} with the name {objectName} was detected.")
            objectType = "null"
            objectName = ""
            objectOpened = False

    return objects
def Rbuild(filename):
    objs = read_and_update_objects(filename)


    f = open("caliber_engine\world.caliber", "w")
    for obj in objs:
        f.write(str(obj.x)+","+ str(obj.y)+","+str(obj.z)+","+str(obj.rotx)+","+str(obj.roty)+","+str(obj.rotz)+","+str(obj.scaleX)+","+str(obj.scaleY)+","+str(obj.scaleZ)+","+obj.path+","+str(obj.draw)+","+str(obj.static)+ "\n")
    f.close()

