from functions.get_files_info import get_files_info

print("=== TESTING: get_files_info ===")

print('TEST 1: get_files_info("calculator", ".")')
print("===============================")
print("Output:")
print(get_files_info("calculator", "."))
print("===============================")

print('TEST 2: get_files_info("calculator", "pkg")')
print("===============================")
print("Output:")
print(get_files_info("calculator", "pkg"))
print("===============================")

print('TEST 3: get_files_info("calculator", "/bin")')
print("===============================")
print("Output:")
print(get_files_info("calculator", "/bin"))
print("===============================")

print('TEST 3: get_files_info("calculator", "../")')
print("===============================")
print("Output:")
print(get_files_info("calculator", "../"))
print("===============================")
