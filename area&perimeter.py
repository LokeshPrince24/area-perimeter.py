# Open the input file in read mode and output file in write mode
with open('area val.txt', 'r') as infile, open('output2.txt', 'w') as outfile:
    # Read the lengths and breadths from the input file
    l = int(infile.readline().strip())
    b = int(infile.readline().strip())

    # Calculate area and perimeter
    area = l * b
    perimeter = 2 * (l + b)

    # Write the results to the output file
    outfile.write("Area of rectangle is: " + str(area) + "\n")
    outfile.write("Perimeter of rectangle is: " + str(perimeter) + "\n")
