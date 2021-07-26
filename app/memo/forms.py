from django import forms
from .models import Child, Prog, Parent

class ProgForm(forms.ModelForm):

	def __init__(self, *args, **kargs):
		super(ProgForm, self).__init__(*args, **kargs)

	class Meta:
		model = Prog
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

		
