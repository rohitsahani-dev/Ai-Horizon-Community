import pandas as pd

data = {
    "Name": ['Rohit Sahani','Ayush sha','Pratik chaudari'],
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data,index = ['Day-1','Day-2','Day-3'])

print(myvar)



