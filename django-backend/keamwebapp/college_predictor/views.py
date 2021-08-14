from django.shortcuts import redirect, render
from django.contrib import messages

from .forms import CandidateDataForm

import pandas as pd

def formInput(request):
    if request.method == 'POST':
        form = CandidateDataForm(request.POST)

        if form.is_valid():
            category = form.cleaned_data.get('category')
            course = form.cleaned_data.get('course')
            rank = form.cleaned_data.get('rank')

            df = pd.read_csv('data/final_data.csv')

            df = df.loc[df['Course'] == course]
            df = df.loc[df[category] >= rank]

            # sorting based on closing rank
            df = df.sort_values(by = 'SM')
            df = df.reset_index(drop=True)

            # dropping a few columns 
            cols_to_drop = [i for i in category if i!=category]
            cols_to_drop.append("College Code")
            df = df.drop(labels=cols_to_drop, axis=1)

            df_dict = df.to_dict()

            return render(request, 'college_predictor/prediction.html', {'df_dict':df_dict})
        else:
            messages.warning(request, 'Please fill the form correctly')
        
    else:
        form = CandidateDataForm()

    return render(request, 'college_predictor/home.html', {'form':form})