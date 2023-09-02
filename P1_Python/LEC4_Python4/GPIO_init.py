
#-------------------------------------------------------------
# Write python code to generate Init function of GPIO for AVR.
#-------------------------------------------------------------

bits = int(input("Enter number of bits: "))

bits_list = []

for i in range(0,bits):
    bit = input(f"Enter bit{i} mode: ")
    if bit == 'out':
        bits_list.append(1)
    elif bit == 'in':
        bits_list.append(0)

    else:
        print("Wrong input")
        break


bits_list.reverse()
bits_list.insert(0,'0b')

bits_list = map(str, bits_list)
port_value = ''.join(bits_list)

function = f'void Init_void (void)\n{{\nDDRA = {port_value}\n}}'

with open("set_direction.c",'a') as new:
    new.write(function)
