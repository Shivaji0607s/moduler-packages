import importlib


def explore_module():

    print("""
       Explore Module Attributes
    """)

    name = input("""
Enter Module name to explore:
Example: math, datetime, time, random, uuid, os, importlib
""")

    try:
        module = importlib.import_module(name)

        print(f"\nAvailable Attributes in {name} Module are:")
        print(dir(module))

    except ModuleNotFoundError:
        print(f"\nModule '{name}' not found.")
        print("Please enter a valid Python module name.")