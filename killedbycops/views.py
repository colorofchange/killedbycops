from django.shortcuts import render
from django.http import HttpResponseRedirect

def home(request):
  return HttpResponseRedirect('http://act.colorofchange.org/sign/killedbycops_stw?source=killedbycops_home')