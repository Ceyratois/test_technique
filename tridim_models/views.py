from django.shortcuts import render
from django.views.generic import CreateView
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from tridim_models.models import UploadedModel
from tridim_models.forms import UserForm, RegisteredUserForm


class ModelCreationView(CreateView):
    """Allow 3D Model creation (upload)."""
    
    model = UploadedModel
    fields = ["name", "description"]
    
    def form_valid(self, form):
        user = self.request.user
        form.instance.creator = user.registereduser
        return super(ModelCreationView, self).form_valid(form)
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ModelCreationView, self).dispatch(*args, **kwargs)

    
class UserCreationView(View):
    """Allow a user to register (create an account on the app)."""
    
    def get(self, request, *args, **kwargs):
        uf = UserForm(prefix='user')
        ruf = RegisteredUserForm(prefix='registereduser')
        return render(
            request,
            'register.html', 
            context={"userform":uf, "registereduserform":ruf})

    def post(self, request, *args, **kwargs):
        ruf = RegisteredUserForm(request.POST, prefix="registereduser")
        uf = UserForm(request.POST, prefix="user")
        if uf.is_valid() and ruf.is_valid():
            user = uf.save()
            registereduser = ruf.save(commit=False)
            registereduser.user = user
            registereduser.save()
            login(request, user)
            messages.add_message(
                request, 
                messages.INFO, 
                "Your account was successfully created ! You can now upload a 3D model.")
            return HttpResponseRedirect("/models/new")
        else:
            return render(
                request,
                'register.html', 
                context={"userform":uf, "registereduserform":ruf})            
