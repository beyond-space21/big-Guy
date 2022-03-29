file = open("example/models/gcode/captain.gcode",'r')
file_data = file.read()
# start_index = file_data.index("TYPE:SKIRT") + 11
# print(file_data[start_index])

file_write = open("example/models/gcode/new.gcode",'w')

now_read='X'
cmd=False
reg=''

offset_X=-196
offset_Y=-249

for i in file_data:
    match i:
        case 'X':
            now_read='X'
            file_write.write('X')
            cmd=True
        case 'Y':
            now_read='Y'
            file_write.write('Y')
            cmd=True
        case _:
            if cmd:
                if i != ' ' and i != '\n':
                    reg=reg+i
                else:
                    cmd=False
                    if now_read == 'X':
                        file_write.write(str(round(float(reg)+offset_X,3))+i)
                    if now_read == 'Y':
                        file_write.write(str(round(float(reg)+offset_Y,3))+i)
                    reg=''
            else:                
                file_write.write(i)