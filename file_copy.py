input_file = input("Enter the input file: ") 
output_file = input("Enter the output file: ") 
with open(input_file,'r') as file_1: 
    content = file_1.read()
with open(output_file,'w') as file_out: 
    file_out.write(content)