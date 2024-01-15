from django import forms


class CommentForm(forms.Form):
    comment_text = forms.CharField(label="Commentary", widget=forms.Textarea)
    rating = forms.IntegerField(label="Rating", widget=forms.NumberInput(attrs={"min": 0, "max": 10, "required": True, "type": "number"}))