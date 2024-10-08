from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
# from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Article 

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title','summary','body','photo',)
    template_name = 'article_edit.html'

    
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

class ArticleCreateView(CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'summary', 'body', 'photo','author')

    # def form_valid(self, form):
    #     form.instance.author = self.request.user 
    #     return super().form_valid(form)
    

# Create your views here.
