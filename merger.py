import os
# output_file = "output.txt"
def merge(file_list,output_file):
    f_out = open(output_file, 'w')
    sum = 0
    for f in file_list:
        f_in = open(f)
        num = int(f_in.read())
        sum += num
        f_in.close()
    f_out.write(sum)
    f_out.close()
