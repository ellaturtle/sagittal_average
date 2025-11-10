import numpy as np
import random
import subprocess

# Create a sample input file and the expected output file.
input_name = "brain_sample.csv"
output_name = 'correct_average.csv'

# Create a random 20x20 matrix and save it as input file
np.random.seed(0)
data_input = np.random.randint(10, size=(20, 20))
np.savetxt(input_name, data_input, fmt='%d', delimiter=',')

# Read the input file
myfile = open(input_name, 'r')

# Create a plane list to keep a list per row
planes = []
for line in myfile.readlines():
    planes.append([int(x) for x in line.split("\n")[0].split(',')])
myfile.close()

# Create new list to save the averages per each plane
sagittal_averages = []
for i in range(20):
    total = 0
    for j in range(20):
        total = total + int(planes[i][j])
    sagittal_averages.append(str(total/20))

# Write the averages to the expected output file
myoutput = open(output_name, 'w')
myoutput.write(','.join(sagittal_averages) +  '\n')
myoutput.close()

# Run the sagittal_brain.py script and compare its output to the expected output
subprocess.run(["python", "sagittal_brain.py"])
output = np.loadtxt("brain_average.csv",  delimiter=',')
expected = np.loadtxt(fname=output_name, delimiter=',')
assert np.array_equal(output, expected)