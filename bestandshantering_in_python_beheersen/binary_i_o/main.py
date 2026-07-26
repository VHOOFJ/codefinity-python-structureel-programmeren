# Write Python code to open a file named "data.bin" in binary write mode and write the bytes b'PythonRocks!' to it.
# Write your code here
with open("data.bin", "wb") as file:
    file.write(b'PythonRocks!')
# Then, open the same file in binary read mode, read the contents, and store them in a variable named "read_bytes".
# Write your code here
with open("data.bin", "rb") as file:
    read_bytes = file.read()