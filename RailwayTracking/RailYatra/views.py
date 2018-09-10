from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.views.generic import View
from django.views import generic
# Create your views here.



class IndexView(View):
    template_name="Railyatra/index.html"
    def get(self,request):
        
        return render(request,self.template_name,{})







# class SignupView(View):
#     template_name='RailYatra/signup.html'

#     def get (self,request):
        
#         form=UserCreationForm()
#         return render(request,self.template_name,{'form':form})


#     def post (self,request):
#          form=UserCreationForm(request.POST)
#          if form.is_valid:
#              form.save()
#              username=form.cleaned_data.get('username')
#              password=form.cleaned_data.get('password')
#              user=authenticate(username=username,password=password)
#              login(request,user)
#              return redirect('RailYatra:index')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            return redirect('RailYatra:signin')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})



