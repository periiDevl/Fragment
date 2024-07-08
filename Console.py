from rich import print
from rich.style import Style
import shutil
import time
import random
import sys
import os
import Reader
from io import StringIO
import subprocess 
project = ""


error_style = Style(color="red", bold=True)
def suppress_output(func):
    def wrapper(*args, **kwargs):
        # Redirect stdout to a dummy object
        original_stdout = sys.stdout
        sys.stdout = StringIO()
        # Call the function
        func(*args, **kwargs)
        # Restore original stdout
        sys.stdout = original_stdout
    return wrapper
@suppress_output
def suppressed_function(filename):
    Reader.read_and_update_objects(filename)

def matrix_effect(text, delay=0.00000000001, lines=0):
    # Get the terminal width
    columns = os.get_terminal_size().columns

    # Split the input text into lines
    text_lines = text.split('\n')

    # Find the maximum length of any line in the text to align them properly
    max_length = max(len(line) for line in text_lines)

    # Phase 1: Display random characters
    for _ in range(lines):
        line = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(columns))
        print(line)
        time.sleep(0.000000000000001)

    # Phase 2: Display the ASCII art line by line
    for line in text_lines:
        padded_line = line.ljust(max_length)
        # Print each character with a red color
        for char in padded_line:
            print(f"[rgb(200,0,0)]{char}", end='')
            time.sleep(delay)

        print()

def cyber_effect_print(text, delay=0.00001, iterations=5):
    for char in text:
        for _ in range(iterations):
            # Print a random character
            sys.stdout.write(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()[] -@-'))
            sys.stdout.flush()
            time.sleep(delay)
            # Move the cursor back
            sys.stdout.write('\b')
        # Print the correct character
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_centered(text):
    # Get the terminal width
    terminal_width = shutil.get_terminal_size().columns
    # Calculate the starting point for the centered text
    start = (terminal_width - len(text)) // 2
    # Print the text with leading spaces to center it
    print(' ' * start + text)
def get_name_from_argument(arg):
    # Split the argument by ':'
    parts = arg.split(':')
    if len(parts) == 2:  # Ensure there is exactly one ':' in the argument
        return parts[1].strip()  # Return the part after ':' with leading/trailing spaces removed
    else:
        return None  # Return None if the argument format is incorrect

# ASCII art and initial commands display
ascrii = """                                                                                       
                                                                                          
                                                                                          
       -@-                                                        -@@@@@@-                
     -@@@@@@-                         -@@@@@@@@@@@@@@@-     -@@@@@@@@@@@@@@@@@@-          
    -@@@@@@@@@-                       @@@@@-         @@  -@@@@@@@@@@@@@@ @@@@@@@          
    @@- -@@@-@@                       @@  @@@@@@@@@@@@--@@@@@ @@@@@@@@@@@@@@@@@@          
    @@  @@@@@@@@@@@-                  @@  @@           @@@- -@@@@@@-   -@@@@@@@-          
    @@  @@   @@ -@@@@-                @@  @@@@@@@@@@@@@@@  -@@-                           
    @@  @@   -@@@@@-@@-@@-            @@  -@@@@@@@@@@@@@-  @@-       -@@@@@@@@@@-         
    @@  @@      -@@@@ @@@@@-          @@  -@@@@@@@@@@@@@-  @@-       @@@@@@@@@@@@         
    @@  @@           @@@ @@@@-        @@  @@@@@@@@@@@@@@@  -@@-      @@@@@@-   @@         
    @@  @@           -@@@@@-@-@@-     @@  @@           @@@- -@@@@-   -@@@@@@   @@         
    @@  @@             -@@@@@@@@@@@-  @@  @@           -@@@@--@@@@@@@@@@@@@@   @@         
    @@  @@                   @@@@@@@- @@  @@             -@@@@@@ @@@@@@@@@@ @@@@@         
    @@  @@@@@@@@@@@@-        -@@@@@@@-@@@@@@               -@@@@@@@@@@@@@@@@@@@@-         
    @@  -@@@@@@@@@@@@-         -@@@@ @@-@ @@                   -@@@@@@@@@@@@-             
    @@  -@@@@@@@@@--@@              @@@@@@@@@-                                            
    @@  @@@@@@@@@@@ @@              -@@@@@@--@@-                                          
    @@  @@       @@ @@                 -@@@@@@@@@@-                                       
    @@  @@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@-@@@@@-                                     
    @@@--@@@@@@@@@- -@@@@@@@@@@@@@@@@@@@@@@@@-   -@@@                                     
    -@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-                                     
      -@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-                                      
                                                                                          
                                                                                          
                                                                                          """
print(ascrii)
time.sleep(0.3)
license_to_caliber = """MIT License

Copyright (c) 2022 Jonathan Peri

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""
print(license_to_caliber)

#cyber_effect_print("Fragment Engine by Jonathan peri")
print_centered("[blue]-------------------------------------------------------------------------------------------------------------------------")
print_centered("Commands :")
print_centered("[blue]-------------------------------------------------------------------------------------------------------------------------")
commands = """
-cnew : create new project
-cop : open existing project
-m : manual mode build
-a : automatic mode (both for activating and deactivating)
-p : open selected preview
-export : export the project
-ex-p : preview export
-ascrp : add scripts
-rscrp : add scripts
-mms : opens mss debug tool (not done)
-version : version
-include : includes a folder or file to the project
-mdyn : move the built dynaLL .dll file to the project folder
"""
time.sleep(0.6)
print("[rgb(0,200,0)]" +commands )
Overview_commands = """
. = New object [pos, sca, model, tint]
/ - Bind to object like /. to make it a physics object
! = Collider [pos, sca, *shape, follow, scriRef]
< = Camera
@ = Variable path [obj, gltf, fbx] [png, jpg, jpeg] {just stores the path}
* = Point light [pos, radius, strength]
/|\ = Directional light [pos, radius, strength]
/\ = Spot light [pos, radius,rot, strength]
Object creation example :
.object{
  x[1]
  y[2]
  z[3]
  sx[1]
  sy[2]
  sz[3]
}

"""

time.sleep(0.3)
print_centered("[blue]-------------------------------------------------------------------------------------------------------------------------")
print_centered("Overview lang features")
print_centered("[blue]-------------------------------------------------------------------------------------------------------------------------")
print("[rgb(200,0,200)]" +Overview_commands )

while True:
    suppressed_function(project)
    matrix_effect("listening..." + "(" + project + ")")
    user_input = input().strip()  # Get user input and strip any extra whitespace
    if os.path.exists(os.path.join(os.getcwd(), user_input) + ".fg"):
        project = os.path.join(os.getcwd(), user_input) + ".fg"
        print("[green]" + project)
    if user_input == "-cnew":
        matrix_effect("name? : ")
        proj_name = input()

        matrix_effect("directory? : ")
        proj_path = input()
        
        if proj_path == "":
            proj_path = os.getcwd()
        
        if os.path.exists(proj_path):
            print("[green]creating " + proj_name + ".fg file in : " + proj_path)
            with open("projects.projects", "w") as f:
                f.write(proj_name + ":" + proj_path)
            continue
        else:
            print("[bold red]Error:[/bold red] path doesn't exist.")
            continue

    elif user_input == "-o":
        matrix_effect("searching...")
        with open("projects.projects", "r") as f:
            content = f.read()
            print("[rgb(200,0,200)]" + content)
        matrix_effect("found")

        matrix_effect("write directory :")
        project = input()
        
        if os.path.exists(project):
            print("[green]Ready! " + project)
        else:
            print("[bold red]Error:[/bold red] path doesn't exist.")
        continue
    elif user_input == "-m":
        Reader.read_and_update_objects(project)
        Reader.Rbuild(project)
    elif user_input == "-a":
        print("[green] Opening auto build .exe")
    elif user_input == "-p":
        print("[green] Opening viewing window")      

        
        source_file = "caliber_engine/x64/Release/caliber_engine.exe"  # Replace with your actual path
        destination_file =  "caliber_engine/caliber_engine.exe"


        shutil.copy(source_file, destination_file)
        print("[green][√] Caliber engine EXE copied successfully.")

        print("[red][!] Capturing output from the exe, if any strage stuff show up or errors its a result of the engine output.")
        subprocess.run(["caliber_engine/caliber_engine.exe"], cwd="caliber_engine")
        print("[blue][√] Closed.")



    elif user_input == "-mms":
        print("[green] Opening mms window")        
    elif user_input == "-version":
        print("[green] 1.0")        
    elif user_input == "-mdyn":
        source_file = "caliber_engine/DynaLL/x64/Release/DynaLL.dll"  # Replace with your actual path
        destination_file =  "caliber_engine/DynaLL.dll"


        shutil.copy(source_file, destination_file)
        print("[green][√] DynaLL .dll copied successfully.")

        source_file = "caliber_engine/DynaLL/x64/Release/DynaLL.lib"  # Replace with your actual path
        destination_file =  "caliber_engine/DynaLL.lib"


        shutil.copy(source_file, destination_file)
        print("[green][√] DynaLL .lib copied successfully.")
        print("[green][√] Done.")

