from functions.get_file_content import get_file_content

print("=== TESTING: get_files_info ===")

print('TEST 1: get_file_content("calculator", "lorem.txt")')
print("===============================")
print("Output:")
print(get_file_content("calculator", "lorem.txt"))
print("===============================")

print('TEST 2: get_file_content("calculator", "main.py")')
print("===============================")
print("Output:")
print(get_file_content("calculator", "main.py"))
print("===============================")

print('TEST 3: get_file_content("calculator", "pkg/calculator.py")')
print("===============================")
print("Output:")
print(get_file_content("calculator", "pkg/calculator.py"))
print("===============================")

print('TEST 4: get_file_content("calculator", "/bin/cat")')
print("===============================")
print("Output:")
print(get_file_content("calculator", "/bin/cat"))
print("===============================")

print('TEST 5: get_file_content("calculator", "pkg/does_not_exist.py")')
print("===============================")
print("Output:")
print(get_file_content("calculator", "pkg/does_not_exist.py"))
print("===============================")
