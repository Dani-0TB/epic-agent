from functions.run_python_file import run_python_file

print("=== TESTING: run_python_file ===")

print('TEST 1: run_python_file("calculator", "main.py")')
print("========================================")
print("Output:")
print(run_python_file("calculator", "main.py"))
print("========================================")

print('TEST 2: run_python_file("calculator", "main.py", ["3 + 5"])')
print("========================================")
print("Output:")
print(run_python_file("calculator", "main.py", ["3 + 5"]))
print("========================================")

print('TEST 3: run_python_file("calculator", "tests.py")')
print("========================================")
print("Output:")
print(run_python_file("calculator", "tests.py"))
print("========================================")

print('TEST 4: run_python_file("calculator", "../main.py")')
print("========================================")
print("Output:")
print(run_python_file("calculator", "../main.py"))
print("========================================")

print('TEST 5: run_python_file("calculator", "nonexistent.py")')
print("========================================")
print("Output:")
print(run_python_file("calculator", "nonexistent.py"))
print("========================================")

print('TEST 6: run_python_file("calculator", "lorem.txt")')
print("========================================")
print("Output:")
print(run_python_file("calculator", "lorem.txt"))
print("========================================")
