from django import forms

class TweetForm(forms.Form):
	tweet = forms.CharField(max_length=140)

class PhotoForm(TweetForm):
	pass

class BlogForm(TweetForm):
	pass