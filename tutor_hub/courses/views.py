from django.shortcuts import render, HttpResponseRedirect
from django.shortcuts import redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group
from django.views.generic import TemplateView, DetailView, ListView, FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
