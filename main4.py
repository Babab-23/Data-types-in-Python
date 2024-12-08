#Program to demonstrate string operations

# Input: Gt the user's name
name= input("Enter your name: ")
# Example 1: Concatenation message="Congratulations, " + name + "! You have completed the lesson on data types in Python."
#  Example 2: String case conversion
upper_case_message= message.upper() # Convert to uppercase
lower_case_message= message.lower() # Convert to lowercase
# Example 3 : String slicing short_message=message[:25]
 # Extract the first 25 characters
# Example 4: String formatting formatted_message= f"Well done,{name}! Keep learning Python."
# Example 5: Replace operation replaced_message=message.replace("Data types","string operation")

# Output : Display all the examples
print("\n--- Examples of String Operations---\n")
print("Original Message: ",message)
print("Uppercase  Message: ",upper_case_message)
print("Lowercase  Message: ",lower_case_message)
print("Shortened Message: ",short_message + "...")
print("Formatted Message: ", formatted_message)
print("Replaced Message: ", replaced_message)

