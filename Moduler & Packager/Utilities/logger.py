from datetime import datetime
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_FILE = os.path.join(BASE_DIR, "output_log.txt")

_builtin_input = input

MENU_MAP = {
    "1": "DATETIME OPERATIONS",
    "2": "MATHEMATICAL OPERATIONS",
    "3": "RANDOM DATA GENERATION",
    "4": "UUID GENERATION",
    "5": "FILE OPERATIONS",
    "6": "MODULE EXPLORER (dir())",
}


class CleanLogger(object):

  def __init__(self, filename=LOG_FILE):
    self.terminal = sys.stdout
    self.log = open(filename, "a", encoding="utf-8")

  def write(self, message):
    self.terminal.write(message)

    ignore_patterns = [
        "==================",
        "..................",
        "Choose an option",
        "DateTime and Time Operation",
        "Mathematical Operation",
        "Random Data Generation",
        "Generate Unique Identifiers",
        "File Operation (Custom Module)",
        "Explore Module Attribute",
        "Press Enter RE-ENTER",
    ]

    clean_msg = message.strip()
    if clean_msg and not any(p in clean_msg for p in ignore_patterns):
      timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
      self.log.write(f"{timestamp} OUTPUT: {clean_msg}\n")
      self.log.flush()

  def flush(self):
    self.terminal.flush()
    self.log.flush()


def setup_logger():
  """Activates output logging and records the program start banner."""
  sys.stdout = CleanLogger(LOG_FILE)

  timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
  with open(LOG_FILE, "a", encoding="utf-8") as f:
    f.write("\n" + "=" * 80 + "\n")
    f.write(
        f"{timestamp} --- NEW SESSION STARTED (Multi-Utility Toolkit) ---\n"
    )
    f.write("=" * 80 + "\n\n")


def custom_input(prompt=""):
  user_entry = _builtin_input(prompt)
  timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
  clean_prompt = prompt.strip().rstrip(".").strip()

  with open(LOG_FILE, "a", encoding="utf-8") as f:
    # Log the user's input entry
    f.write(
        f"{timestamp} USER INPUT [{clean_prompt}]: {user_entry.strip()}\n"
    )

    # If the user selected a top-level option from the main menu, insert a module divider
    if clean_prompt == "Enter your Choice Here" and user_entry in MENU_MAP:
      section_title = MENU_MAP[user_entry]
      f.write("\n" + "-" * 50 + "\n")
      f.write(f"{timestamp} >>> ENTERED MODULE: {section_title}\n")
      f.write("-" * 50 + "\n\n")

  return user_entry


import builtins

builtins.input = custom_input