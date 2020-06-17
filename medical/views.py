from django.shortcuts import render
import requests
import pandas as pd
from pathlib import Path
from sklearn.neighbors import KNeighborsClassifier
def home(request):
    return render(request,'home.html')
def test(request):
    return render(request,'test.html')
def calc(request):
    ls = [ ] 
    ls.append(int(request.GET['glucoselevel']))
    ls.append(int(request.GET['Bloodpressure']))
    ls.append(int(request.GET['Skinthickness']))
    ls.append(int(request.GET['Insulinlevel']))
    ls.append(float(request.GET['BMI']))
    ls.append(float(request.GET['Diabetespedigreefunction']))
    ls.append(int(request.GET['Age']))
    script_location = Path(__file__).absolute().parent
    file_path = script_location / 'diabetesample_input.csv'
    data = pd.read_csv(file_path)
    x = data.iloc[:,[1,2,3,4,5,6,7]]
    y = data.iloc[:,[8]]

    model = KNeighborsClassifier()

    model.fit(x,y.values.ravel())

    pred = model.predict([ls])


    if pred == [1]:
        return render(request,'havedia.html')
    else:
        return render(request,'havenodia.html')

    
