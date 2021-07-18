from django import forms
from .models import Langage, Child, Parent

class LangageForm(forms.ModelForm):

	def __init__(self, *args, **kargs):
		super(LangageForm, self).__init__(*args, **kargs)

	class Meta:
		model = Langage
		fields = ['name']


class ChildForm(forms.ModelForm):

	def __init__(self, *args, **kargs):
		super(ChildForm, self).__init__(*args, **kargs)

	class Meta:
		model = Child
		fields = '__all__'


class ParentForm(forms.ModelForm):

	def __init__(self, *args, **kargs):
		super(ParentForm, self).__init__(*args, **kargs)

	class Meta:
		model = Parent
		fields = '__all__'
