from django import forms
from django.utils.translation import ugettext_lazy as _
from django_summernote.widgets import SummernoteWidget
from django.contrib.auth.models import User
from .models import Resume, ResumeReview


class ResumeForm(forms.ModelForm):
    ATTACHMENT_LIMIT_IN_MB = 30

    class Meta:
        model = Resume
        exclude = ('desc',)

    def __init__(self, *args, **kwargs):
        super(ResumeForm, self).__init__(*args, **kwargs)

        for k, v in self.Meta.model.descfields().iteritems():
            self.fields[k] = v['field']

        self.fields['description'].widget.attrs['class'] = 'fill-width summernote'
        self.fields['resume'].widget.attrs['class'] = 'fill-width summernote'
        self.fields['attachment'].label += _(' - Max. file size %d MB') % self.ATTACHMENT_LIMIT_IN_MB

    def clean_attachment(self):
        attachment = self.cleaned_data.get('attachment', False)
        if attachment:
            try:
                if attachment._size > (self.ATTACHMENT_LIMIT_IN_MB * 1024 * 1024):  # 10 MB
                    raise forms.ValidationError(_("Too large attachment( > %d MB )") % self.ATTACHMENT_LIMIT_IN_MB)
            except AttributeError:
                pass
            return attachment

    def save(self, commit=True):
        # do something with self.cleaned_data['temp_id']
        return super(ResumeForm, self).save(commit=commit)


class ResumeReviewForm(forms.ModelForm):
    class Meta:
        model = ResumeReview

    def __init__(self, *args, **kwargs):
        super(ResumeReviewForm, self).__init__(*args, **kwargs)

        self.fields['user'].widget = forms.HiddenInput()
        self.fields['resume'].widget = forms.HiddenInput()

        self.fields['desc'] = forms.CharField(widget=SummernoteWidget())
        self.fields['desc'].widget.attrs['class'] = 'fill-width summernote'


class ResumeMailForm(forms.Form):
    sender = forms.ChoiceField(choices=User.objects.all().values_list('username', 'username'))
    mail_password = forms.CharField(widget=forms.PasswordInput(), required=False)
    resume_ids = forms.CharField(widget=forms.HiddenInput())
    subject = forms.CharField()
    top_image = forms.ImageField(required=False)
    message = forms.CharField(widget=SummernoteWidget())
    bottom_image = forms.ImageField(required=False)

    def __init__(self, *args, **kwargs):
        super(ResumeMailForm, self).__init__(*args, **kwargs)

        self.fields['subject'].widget.attrs['class'] = 'fill-width'
        self.fields['message'].widget.attrs['class'] = 'fill-width summernote'
