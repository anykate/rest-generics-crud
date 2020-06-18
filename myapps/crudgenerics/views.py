import requests

from django.shortcuts import render, redirect
from rest_framework import generics, mixins

from .models import Student
from .forms import StudentInsertForm
from .serializers import StudentSerializer


class StudentListCreate(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_url_kwarg = 'student_id'


def savestudent(request):
    form = StudentInsertForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=False)
            post_data = requests.post(
                'http://localhost:8000/api/students/',
                headers={'Content-Type': 'application/json'},
                json=form.cleaned_data
            )
            return redirect('/')
    return render(request, 'core/insert.html', {'form': form})
