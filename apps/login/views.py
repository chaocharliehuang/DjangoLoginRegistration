from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.core.urlresolvers import reverse

import bcrypt

from .models import User

def index(request):
    if 'first_name' not in request.session:
        request.session['first_name'] = ''
    if 'last_name' not in request.session:
        request.session['last_name'] = ''
    if 'email' not in request.session:
        request.session['email'] = ''
    return render(request, 'login/index.html')

def register(request):
    if request.method == 'POST':
        # FORM VALIDATION
        errors = User.objects.basic_validator(request)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect(reverse('login:index'))

        # ADD USER TO DATABASE
        pw_hashed = bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt())
        new_user_id = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], pw=pw_hashed).id

        request.session['first_name'] = ''
        request.session['last_name'] = ''
        request.session['email'] = ''
        request.session['id'] = new_user_id

        return redirect(reverse('login:success', args=(new_user_id,)))
    else:
        return redirect(reverse('login:index'))

def success(request, id):
    context = {'first_name': User.objects.get(id=id).first_name}
    return render(request, 'login/success.html', context)