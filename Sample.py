'''
# with open("myfile.txt", "w") as file:
    file.write("Hello  Kaja\n")
    file.write("Hello JMC\n")

print("File written successfully!") 
'''
'''
with open("myfile.txt", "r") as file:
    content = file.read()

print(content)
'''
'''
with open("myfile.txt", "r") as file:
    for line in file:
        print(line.strip())   # strip() removes extra spaces/newlines        
'''
'''
try:
    number = int("hello")
except Exception as e:
    print(f"An error occurred: {e}")
'''

def add(a, b):
    return a + b

result = int(add(10.5, 5))   # store the returned value
print("Sum is:", result)

