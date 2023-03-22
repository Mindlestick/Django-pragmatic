from django import forms
from django.forms import ModelForm

from articleapp.models import Article
from projectapp.models import Project


class ArticleCreationFrom(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable text-start',
                                                           'style': 'height: auto;'}))
    #게시글 작성시 project를 선택하지 않아도 되게 하는 옵션
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)

    class Meta:
        model = Article
        fields = ['title','image','project','content']