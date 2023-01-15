from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import *
from .models import *
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



def home(request):
	quizlist = {
	"questions": Quiz.objects.all()
	}
	return render(request, "quiz/home.html", quizlist)

class QuizListView(ListView):
    model = Quiz
    template_name = 'quiz/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'questions'
    


class QuizDetailView(DetailView):
    model = Quiz


class QuizCreateView(LoginRequiredMixin, CreateView):
    model = Quiz
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class QuizUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Quiz
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        quiz = self.get_object()
        if self.request.user == quiz.author:
            return True
        return False


class QuizDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Quiz
    success_url = '/'

    def test_func(self):
        quiz = self.get_object()
        if self.request.user == quiz.author:
            return True
        return False

def about(request):
    return render(request, "quiz/about.html", {"title": "About"})

