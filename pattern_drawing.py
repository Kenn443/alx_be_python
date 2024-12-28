# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Ensure the input is a positive integer
if size <= 0:
    print("Please enter a positive integer.")
else:
    # Initialize a counter for rows
    row = 0

 # Use a while loop to iterate through rows
    while row < size:
        # Use a for loop to print asterisks in the current row
        for col in range(size):
         print("*", end="")  
       
        print() 
        row += 1