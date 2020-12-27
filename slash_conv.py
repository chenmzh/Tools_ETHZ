import os


# Read a path
script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "output.txt"
abs_file_path = os.path.join(script_dir, rel_path)

# Enter the input
address = input("Please enter the string you want to convert and press enter:")
# Split first and then join by /
temp = address.split("\\")
output = "/".join(temp)

# Create a file and Print the output
f = open(abs_file_path, "w")
f.write(output)
f.close()
input("Press enter to exit ")
