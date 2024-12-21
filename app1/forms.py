from django import forms
from .models import Project

from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'image', 'video']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter project title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Describe your project'}),
            'video': forms.FileInput(attrs={'class': 'form-control', 'accept': 'video/*'}),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 3:
            raise forms.ValidationError("Title must be at least 3 characters long.")
        return title

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) < 10:
            raise forms.ValidationError("Description must be at least 10 characters long.")
        return description

    def clean_video(self):
        video = self.cleaned_data.get('video')
        if video:
            # Add validation for video file size and format if needed
            if video.size > 100 * 1024 * 1024:  # 100MB limit
                raise forms.ValidationError("Video file size must be less than 100MB.")
            # Add more format validations if needed
        return video