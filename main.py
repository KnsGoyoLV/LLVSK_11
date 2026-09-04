import platform
import sys


print("Python version testing script")
print(f"Python: {platform.python_version()}")
print(f"Implementation: {platform.python_implementation()}")
print(f"Platform: {platform.platform()}")

name = input("What is your name? ").strip()
if name:
	print(f"Hello, {name}!")
else:
	print("Hello, stranger!")
