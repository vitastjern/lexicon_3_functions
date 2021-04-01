# You will receive a single integer number between 0 and 100 which is divided with 
# 10 without residue (0, 10, 20, 30...). Your task is to create a function that 
# visualizes a loading bar depending on that number you have received in the input.

def loading_bar(load):
    result = str(load) + "% "
    if load == 100:
        result = result + "Complete!\n\n"
    
    result += "["
    for x in range(0, load, 10):
        result += "%"
    for y in range(load, 100, 10):
        result += "."
    result += "]"

    if load < 100:
        result += "\n\nStill loading"

    return result


what_load = int(input())
print(loading_bar(what_load))
