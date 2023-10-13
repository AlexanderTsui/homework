with open('test.txt', 'r') as file:
    original_content = file.read()

modified_content = "python" + original_content

modified_content += "python"

with open('test.txt', 'w') as file:
    file.write(modified_content)

