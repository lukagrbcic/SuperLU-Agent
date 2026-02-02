# -*- coding: utf-8 -*-
import numpy as np

read_new_code = open('new_code.txt', 'r').readlines()
read_orig_code = open('schurCompUpdate_impl.cuh.bak', 'r').readlines()
# orig_code = [i.split() for i in read_orig_code.readlines()]
start_str = '//START'
end_str = '//END'



idx_start = None
idx_end = None
for i in range(len(read_orig_code)):
    if start_str in read_orig_code[i]:
        idx_start = i 
    if end_str in read_orig_code[i]:
        idx_end = i
        
        
write_new_code = open('schurCompUpdate_impl.cuh', 'w')
for code in read_orig_code[:idx_start+1]:
    write_new_code.write(code)

for code in read_new_code:
    write_new_code.write(code)
    
for code in read_orig_code[idx_end:]:
    write_new_code.write(code)

write_new_code.close()