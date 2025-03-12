# -*- coding: utf-8 -*-
"""
Created on Sun Mar  9 14:47:29 2025

@author: Charlie
"""

from django import forms 
from .models import Topic ,Entry

class TopicForm(forms.ModelForm): 
      class Meta: 
            model = Topic 
            fields = ['text'] 
            labels = {'text': ''}
            
class EntryForm(forms.ModelForm): 
      class Meta: 
         model = Entry 
         fields = ['text'] 
         labels = {'text': ' '} 
         widgets = {'text': forms.Textarea(attrs={'cols': 80})} 