

def Read(filename):
    
    with open(filename, "r") as file:
        lines = file.readlines()

    data = []
    for line in lines:
        line = line.replace(" ", "").replace("(", "").replace(")", "").replace("\n", "").strip(",")
        x, y, z = map(float, line.split(","))
        data.append((x, y, z))
    
    
    return data