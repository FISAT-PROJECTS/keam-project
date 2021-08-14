from django.shortcuts import redirect, render
from django.contrib import messages

from .forms import CandidateDataForm

import pandas as pd
import json

def formInput(request):
    if request.method == 'POST':
        form = CandidateDataForm(request.POST)

        if form.is_valid():
            category = form.cleaned_data.get('category')
            course = form.cleaned_data.get('course')
            rank = form.cleaned_data.get('rank')

            df = pd.read_csv("final_data.csv")

            categories = list(df.columns)[4:]

            df = df.loc[df['Course'] == course]
            df = df.loc[df[category] >= rank]

            # sorting based on closing rank
            df = df.sort_values(by = 'SM')
            df = df.reset_index(drop=True)

            # dropping a few columns 
            cols_to_drop = [i for i in categories if i!=category]
            cols_to_drop.append("College Code")
            cols_to_drop.append("Course")
            cols_to_drop.append("Unnamed: 0")
            df = df.drop(labels=cols_to_drop, axis=1)

            # df_json = df.to_json(orient='records')

            # data = []

            # data = json.loads(df_json)

            # context = {'d':data}
            df_html = df.to_html()

            return render(request, 'college_predictor/prediction.html', context={'df_html':df_html})
        else:
            messages.warning(request, 'Please fill the form correctly')
        
    else:
        form = CandidateDataForm()

    return render(request, 'college_predictor/home.html', {'form':form})