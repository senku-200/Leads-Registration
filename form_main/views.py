from django.shortcuts import render, redirect
from .forms import LeadForm
from django.http import HttpResponse

def LeadRegistration(request):
    if request.method == 'POST':
        lead_form = LeadForm(request.POST)
        if lead_form.is_valid():
            lead_form.save()
            return render(request,'template/success.html',{'isShowBack':True})
        else:
            print('Form is not valid')
    else:
        lead_form = LeadForm()
    
    context = {'form': lead_form,'isShowBack':False}
    return render(request, 'template/LeadForm.html', context)
