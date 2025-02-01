import os

def Read(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__)) 
    filename = os.path.join(script_dir, "../Projects/" + filename + "_rd.txt")
    with open(filename, "r") as file:
        lines = file.readlines()

    data = []
    for line in lines:
        line = line.replace(" ", "").replace("(", "").replace(")", "").replace("\n", "").strip(",")
        x, y, z = map(float, line.split(","))
        data.append((x, y, z))
    

    return data
