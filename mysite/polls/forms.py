from django import forms
from django.forms import ModelForm
from polls.models import Question

class QuestionForm(forms.ModelForm):
	question = forms.CharField()

	class Meta:
		model = Question
		fields = ('question',)