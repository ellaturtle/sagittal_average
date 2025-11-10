import numpy as np
import random
import subprocess

# Create a sample input file and the expected output file.
input_name = "brain_sample.csv"
output_name = 'correct_average.csv' # Expected output file

# Create a random 20x20 matrix and save it as input file
np.random.seed(0) # Every time the test is run, the same random numbers will be generated
data_input = np.random.randint(10, size=(20, 20))
np.savetxt(input_name, data_input, fmt='%d', delimiter=',') # Save as integers in csv format

# Read the input file
myfile = open(input_name, 'r') # Opens the file for reading

# Create a plane list to keep a list per row
planes = []
for line in myfile.readlines(): # Read each line
    planes.append([int(x) for x in line.split("\n")[0].split(',')]) # Split the line into values and convert to integers
myfile.close()
# Now the planes list is a 2D list with 20 rows and 20 columns whereas before it was a list of strings, e.g. ['1,2,3,...'] -> [[1,2,3,...], ...]

# Create new list to save the averages per each plane
sagittal_averages = []
for i in range(20):
    total = 0 # Initialize total for each row
    for j in range(20):
        total = total + int(planes[i][j]) # Sum all the values in the row
    sagittal_averages.append(str(total/20)) # Calculate the average and append it to the list as a string

# Write the averages to the expected output file
myoutput = open(output_name, 'w') # Open the file for writing
myoutput.write(','.join(sagittal_averages) +  '\n') # Write the averages as a comma-separated string
myoutput.close()

# Run the sagittal_brain.py script and compare its output to the expected output
subprocess.run(["python", "sagittal_brain.py"])
output = np.loadtxt("brain_average.csv",  delimiter=',')
expected = np.loadtxt(fname=output_name, delimiter=',')
assert np.array_equal(output, expected)