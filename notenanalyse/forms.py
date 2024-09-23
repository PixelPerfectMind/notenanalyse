from django import forms
from .models import Subject, User_Subject, Symbol


class UserSubjectForm(forms.ModelForm):
    class Meta:
        model = User_Subject
        fields=['symbol_id', 'subject_id', 'school_year_id']
        labels={'symbol_id': 'Fach-Icon',
                'subject_id': 'Fach-Vorlage',
                'school_year_id': 'Gillt für Schuljahr'}

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields=['name', 'description']
        labels={'name': 'Bezeichnung', 'description': 'Beschreibung'}

class SymbolForm(forms.ModelForm):
    class Meta:
        model = Symbol
        fields=['content']
        labels={'content': 'Inhalt'}