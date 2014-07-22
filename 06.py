import os


def getNumbers(string):

    number = ""
    
    for i in range(len(string), 0, -1):

        if string[i-1].isdigit():
            number += string[i-1]
    
    return number

def isNormal(data):

    if len(data) == 16 + len(getNumbers(data)):

        if data[0:16] == "Next nothing is ":

            #int(data[16::])

            return True

    return False
    
done = False

nothing = "90052"

foundFiles = []

while not done:

    with open ("data/06/channel/" + nothing + ".txt", "r") as myfile:

        foundFiles.append(int(nothing))
        
        data = myfile.read().replace('\n', '')

        if isNormal(data):
            nothing = data[16::]

            #print("nothing is \"" + nothing + "\"")

        else:
            #print("\n" * 5 + "data is \"" + data + "\"")
            
            break

print("starting...")
foundFiles.remove(46145)
print(str(foundFiles))

for i in range(0, 99999):

    if not i in foundFiles:

        if os.path.isfile("data/06/channel/" + str(i) + ".txt"):

            print("file " + str(i) + ".txt exists and is not part of the \"linked list \"!")
        
    
print("done...")
