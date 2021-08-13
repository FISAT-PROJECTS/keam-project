from django.shortcuts import redirect, render

from .forms import CandidateDataForm

# Create your views here.
def formInput(request):
    if request.method == 'POST':
        form = CandidateDataForm(request.POST)

        if form.is_valid():
            category = form.cleaned_data.get('category')
            course = form.cleaned_data.get('course')

            return redirect('prediction') # wont work now as prediction is not defined
        
    else:
        form = CandidateDataForm()

    return render(request, 'college_predictor/home.html', {'form':form})