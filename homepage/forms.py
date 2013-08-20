from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Resume


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
            print attachment._size
            if attachment._size > (self.ATTACHMENT_LIMIT_IN_MB * 1024 * 1024):  # 10 MB
                raise forms.ValidationError(_("Too large attachment( > %d MB )") % self.ATTACHMENT_LIMIT_IN_MB)
            return attachment

    def save(self, commit=True):
        # do something with self.cleaned_data['temp_id']
        return super(ResumeForm, self).save(commit=commit)
