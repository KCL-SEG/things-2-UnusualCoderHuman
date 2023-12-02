from django.shortcuts import render, redirect
from .forms import ThingForm  # Import your ThingForm

def home(request):
    if request.method == 'POST':
        # If the form has been submitted, process the data
        form = ThingForm(request.POST)
        if form.is_valid():
            # Form data is valid, save the Thing object and do something
            # e.g., redirect to a success page
            form.save()
            return redirect('success_page')
        else:
            # Form data is invalid, re-render the form with error messages
            return render(request, 'home.html', {'form': form})
    else:
        # If this is a GET request, create an empty form
        form = ThingForm()
    
    return render(request, 'home.html', {'form': form})
