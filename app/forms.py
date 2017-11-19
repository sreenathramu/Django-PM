from django.forms import ModelForm
from django import forms
from models import Category,Tasks
from djangoTrello.models import User
from django.utils.translation import ugettext_lazy as _

class CategoryAddForm(ModelForm):
    class Meta:
        model = Category
        fields = ['category_name','description']
        labels = {
            'category_name': _('Category Name'),
            'description': _('Description')
        }
        help_texts = {
                'description': _('Maximum 250 Characters'),
        }
        widgets = {
            'category_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
        error_messages = {
            'category_name': {
                'max_length': _("This category name is too long."),
            },
            'description': {
                'max_length': _("This description is too long."),
            },
        }

    