from functions.write_file import write_file

print("=== TESTING: write_file ===")

print('TEST 1: write_file("calculator", "lorem.txt", "wait, this isn\'t lorem ipsum")')
print("===============================")
print("Output:")
print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
print("===============================")

print('TEST 2: write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")')
print("===============================")
print("Output:")
print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
print("===============================")

print('TEST 3: write_file("calculator", "/tmp/temp.txt", "this should not be allowed")')
print("===============================")
print("Output:")
print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
print("===============================")
