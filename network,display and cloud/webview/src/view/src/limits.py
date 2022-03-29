file = open("example/models/gcode/captain.gcode",'r')
file_data = file.read()
start_point = file_data.index("TYPE:SKIRT")
file.seek(start_point)
file_data = file.readlines()
# file_data = ['G1 X458.481 Y495.748 Z264.98509','G1 X458.236 Y495.652 Z265.0387','G1 X457.578 Y494.991 Z265.2287']
# start_index = file_data.index("TYPE:SKIRT") + 11
# print(file_data[start_index])

now_read='X'
# cmd=False
reg=''

X=[0,0]
Y=[0,0]
Z=[0,0]

def analyse(buck,data):
    match buck:
        case 'X':
            global X
            if X[0]==0:
                X[0]=data
            if data<X[0]:
                X[0]=data
            elif data>X[1]:
                X[1]=data
                
        case 'Y':
            global Y
            if Y[0]==0:
                Y[0]=data
            if data<Y[0]:
                Y[0]=data
            elif data>Y[1]:
                Y[1]=data

                
        case 'Z':
            global Z
            if Z[0]==0:
                Z[0]=data
            if data<Z[0]:
                Z[0]=data
            elif data>Z[1]:
                Z[1]=data

def scan(line):
    cmd = False
    reg=''
    for i in line:
        match i:
            case 'X':
                now_read='X'
                cmd=True
            case 'Y':
                now_read='Y'
                cmd=True
            case 'Z':
                now_read='Z'
                cmd=True
            case _:
                if cmd:
                    if i != ' ' and i != '\n':
                        reg=reg+i
                    else:
                        cmd=False
                        analyse(now_read,round(float(reg),3))
                        reg=''

length = len(file_data)
for i in range(1,length):
    if file_data[i][0:2] == 'G0':
        scan(file_data[i]+' ')
    

print(X)
print(Y)
print(Z)