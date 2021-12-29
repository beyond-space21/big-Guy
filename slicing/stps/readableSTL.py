#credits:https://stackoverflow.com/questions/7566825/python-parsing-binary-stl-file/70474815#70474815

# example:
# import readableSTL
# p1=readableSTL.load("cube.stl")
# p1.saveas("text.txt")
# print(p1.getdata().normals)
# print(p1.getdata().points)

import struct
normals = []
points = []
triangles = []
bytecount = []

def unpack (f, sig, l):
    s = f.read (l)
    return struct.unpack(sig, s)

def read_triangle(f):
    n = unpack(f,"<3f", 12)
    p1 = unpack(f,"<3f", 12)
    p2 = unpack(f,"<3f", 12)
    p3 = unpack(f,"<3f", 12)
    b = unpack(f,"<h", 2)

    normals.append(n)
    l = len(points)
    points.append(p1)
    points.append(p2)
    points.append(p3)
    triangles.append((l, l+1, l+2))
    bytecount.append(b[0])


def read_length(f):
    length = struct.unpack("@i", f.read(4))
    return length[0]

def read_header(f):
    f.seek(f.tell()+80)

def write_as_ascii(outfilename):
    f = open(outfilename, "w")
    f.write (outfilename+"\n\n")
    f.write ("triangles:"+str(len(triangles))+"\n\n")
    f.write ("|Facet normal|\n|vector 1|\n|vector 2|\n|vector3|\n")
    for n  in range(len(triangles)):
        f.write ("\n\n{} {} {}\n".format(normals[n][0],normals[n][1],normals[n][2]))
        f.write ("{} {} {}\n".format(points[triangles[n][0]][0],points[triangles[n][0]][1],points[triangles[n][0]][2]))
        f.write ("{} {} {}\n".format(points[triangles[n][1]][0],points[triangles[n][1]][1],points[triangles[n][1]][2]))
        f.write ("{} {} {}".format(points[triangles[n][2]][0],points[triangles[n][2]][1],points[triangles[n][2]][2]))
    f.close()

def process_file(readfrom):
    try:
        f = open ( readfrom, "rb")

        read_header(f)
        l = read_length(f)
        try:
            while True:
                read_triangle(f)
        except Exception as e:
            print ("Exception",e)
    except Exception as e:
        print (e)

class load:
    def __init__(self,readfrom):
        self.normals=normals
        self.points=points
        process_file(readfrom)
    def saveas(self,writeto):
        write_as_ascii(writeto)
    def getdata(self):
        self.normals=normals
        self.points=points
        return self       