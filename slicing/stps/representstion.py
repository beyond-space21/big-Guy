import readableSTL

p1=readableSTL.load("cube.stl")
normals=p1.getdata().normals
points=p1.getdata().points

print(len(points))