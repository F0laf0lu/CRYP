from django.shortcuts import render, redirect
from django.contrib.auth import login
import pandas as pd
import numpy as np
import pickle
from .forms import AreaForm, CropForm, InputForm, SignUpForm
import math
from django.contrib.auth.decorators import login_required

# Create your views here.
def SignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def index(request):
    return render(request, 'cover.html')

def home(request):
    return render(request, 'home.html')

@login_required
def yieldinput(request):
    area = AreaForm()
    crop = CropForm()
    input = InputForm()

    context = {
        'area': area,
        'crop': crop,
        'input': input
    }
    return render(request, 'yield.html', context)

@login_required
def predict(request):
    with open('model_pickle', 'rb') as f:
        mp = pickle.load(f)

    if request.method == 'POST':
        area = AreaForm(request.POST)
        crop = CropForm(request.POST)
        input = InputForm(request.POST)
        if area.is_valid():
            country = area.cleaned_data['country']
            country_arr = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            if country == 'bfa':
                country_arr[0] = 1
            elif country == 'gmb':
                country_arr[1] = 1
            elif country == 'gha':
                country_arr[2] = 1
            elif country == 'gin':
                country_arr[3] = 1
            elif country == 'mli':
                country_arr[4] = 1
            elif country == 'mrt':
                country_arr[5] = 1
            elif country == 'ngr':
                country_arr[6] = 1
            elif country == 'sen':
                country_arr[7] = 1
            elif country == 'tgo':
                country_arr[8] = 1

        if crop.is_valid():
            crop = crop.cleaned_data['Crop']
            crop_arr = [0, 0, 0, 0, 0, 0, 0]
            if crop == 'cas':
                crop_arr[0] = 1
                crop = 'Cassava'
            elif crop == 'mze':
                crop_arr[1] = 1
                crop = 'Maize'
            elif crop == 'mil':
                crop_arr[2] = 1
                crop = 'Millet'
            elif crop == 'opm':
                crop_arr[3] = 1
                crop = 'Oil Palm fruit'
            elif crop == 'rce':
                crop_arr[4] = 1
                crop = 'Rice'
            elif crop == 'sor':
                crop_arr[5] = 1
                crop = 'Sorghum'
            elif crop == 'yam':
                crop_arr[6] = 1
                crop = 'Yam'

        if input.is_valid():
            temp = float(input.cleaned_data['Temperature'])
            precp = float(input.cleaned_data['Precipitation'])
            pesticide = np.log(float(input.cleaned_data['Pesticides']))

    data = [temp, precp, pesticide] + country_arr + crop_arr
    arr = np.array(data)
    reshaped_arr = arr.reshape(1, -1)
    predX = pd.DataFrame(reshaped_arr, columns=['Precipitation', 'Temperature', 'Pesticides', 'Country_Burkina Faso', 'Country_Gambia', 'Country_Ghana', 'Country_Guinea', 'Country_Mali', 'Country_Mauritania','Country_Niger', 'Country_Senegal', 'Country_Togo', 'Item_Cassava, fresh', 'Item_Maize (corn)', 'Item_Millet', 'Item_Oil palm fruit', 'Item_Rice', 'Item_Sorghum', 'Item_Yams'])

    prediction = mp.predict(predX)
    prediction = round(prediction[0], 4)
    prediction =round( math.exp(prediction), 2)
    context = {'prediction': prediction,
            'crop':crop}
    return render(request, 'result.html', context)
