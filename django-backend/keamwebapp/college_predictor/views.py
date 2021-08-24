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
            df = df.loc[df[category] >= rank-(rank*0.15)]

            # sorting based on closing rank
            df = df.sort_values(by = category)
            df = df.reset_index(drop=True)

            # dropping a few columns 
            cols_to_drop = [i for i in categories if i!=category]
            cols_to_drop.append("Course")
            cols_to_drop.append("Unnamed: 0")
            cols_to_drop.remove("site")
            df = df.drop(labels=cols_to_drop, axis=1)
            
            # converting all category names to "Closing Rank" in the output dataframe
            for a in categories:
                df.rename(columns={a : "Last Rank of Admission (2020)"}, inplace=True)
            
            df_html = df.to_html(classes=["table", "table-striped", "table-bordered","table-hover"])

            return render(request, 'college_predictor/base.html', context={'df_html':df_html, 'form':form})
        else:
            messages.warning(request, 'Please fill the form correctly')
        
    else:
        form = CandidateDataForm()

    return render(request, 'college_predictor/base.html', {'form':form})
