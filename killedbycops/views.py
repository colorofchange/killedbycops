from django.shortcuts import render
from django.http import HttpResponseRedirect

def petition(request):
    return HttpResponseRedirect('http://act.colorofchange.org/sign/killedbycops_stw?source=killedbycops_home')

def redirect_home(request):
    return HttpResponseRedirect('http://www.killedbycops.org/')