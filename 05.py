# Save a dictionary into a pickle file.
import pickle

data = pickle.load(open("data/05/banner.p", "rb"))

print(str(data))

for a in range(0, len(data)):
    
    for b in range(0, len(data[a])):

        print(data[a][b][0] * data[a][b][1], end = "")

    print("\n")



