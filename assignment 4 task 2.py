# Step 1: Take user input and write to output.txt
user_input = input("Enter some text to write to the file: ")

with open('output.txt', 'w') as file:
    file.write(user_input + '\n')

# Step 2: Take additional input and append it to the file
additional_input = input("Enter more text to append to the file: ")

with open('output.txt', 'a') as file:
    file.write(additional_input + '\n')

# Step 3: Read and display the final contents of the file
print("\nFinal contents of 'output.txt':")
with open('output.txt', 'r') as file:
    for line in file:
        print(line.strip())
