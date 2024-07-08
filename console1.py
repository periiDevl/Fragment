def create_menu(title, options, position_y=0):
  """
  This function creates a text-based menu with a title and options at a specified position.

  Args:
      title: The title of the menu (str).
      options: A list of menu options (list of str).
      position_y: The vertical position on the screen (int, default 0).

  Returns:
      A string containing the formatted menu.
  """
  menu_width = max(len(title), max(len(option) for option in options)) + 4
  menu_line = "-" * menu_width + "\n"
  menu = f"{menu_line}{title.upper():^{menu_width}}\n{menu_line}"
  for i, option in enumerate(options, start=1):
    menu += f"{i}. {option:<{menu_width - 3}}\n"
  menu += f"{menu_line}\nPlease enter your choice for {title}: "
  return menu.format(*[], position_y=position_y)  # Unpack empty args for format

def simple_print(message, clear_screen=False):
  """
  This function prints a message to the console with an optional clear screen.

  Args:
      message: The message to be printed (str).
      clear_screen: Whether to clear the screen before printing (bool, default False).
  """
  if clear_screen:
    print("\033c")  # Clear screen using ANSI escape code
  print(message)

# Define menu options
menu1_options = ["Option A", "Option B", "Back"]
menu2_options = ["Option X", "Option Y", "Back"]

# Create menus
menu1_text = create_menu("Menu 1", menu1_options)
menu2_text = create_menu("Menu 2", menu2_options, position_y=len(menu1_text.splitlines()))

# Print menus
simple_print(menu1_text + menu2_text)

# Get user input for Menu 1
choice1 = input()

# Handle Menu 1 choice
if choice1.isdigit():
  choice1_int = int(choice1)
  if 1 <= choice1_int <= len(menu1_options):
    if choice1_int != 3:  # Handle "Back" selection
      # Logic for Menu 1 selection (replace with your actions)
      simple_print(f"You selected: {menu1_options[choice1_int - 1]} from Menu 1")
      # Potentially show Menu 2 here (modify logic based on your needs)

  else:
    simple_print("Invalid choice for Menu 1. Please try again.")
else:
  simple_print("Invalid input for Menu 1. Please enter a number.")

# Loop for Menu 2 selection (if applicable)
while choice1 == "3":
  # Clear previous menus (optional, adjust based on your logic)
  simple_print("", clear_screen=True)

  # Print Menu 2
  simple_print(menu2_text)

  # Get user input for Menu 2
  choice2 = input()

  # Handle Menu 2 choice (similar logic to Menu 1)
  if choice2.isdigit():
    choice2_int = int(choice2)
    if 1 <= choice2_int <= len(menu2_options):
      if choice2_int != 3:  # Handle "Back" selection
        # Logic for Menu 2 selection (replace with your actions)
        simple_print(f"You selected: {menu2_options[choice2_int - 1]} from Menu 2")
      else:
        break  # Exit loop if "Back" is selected from Menu 2
    else:
      simple_print("Invalid choice for Menu 2. Please try again.")
  else:
    simple_print("Invalid input for Menu 2. Please enter a number.")

# Exit message (optional)
simple_print("\nExiting...")
