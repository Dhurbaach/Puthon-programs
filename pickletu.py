import requests
import pickle
url='https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
data=requests.get(url).text
# print(data)
l1=data.split("\n")
l2= [item.split(",") for item in l1 if len(item)!=0]

with open("myiris.pkl","wb") as f:
    pickle.dump(l2,f)

# To read this pickle file use this code
# with open("myiris.pkl","rb") as f:
      # pickle.load(f)


