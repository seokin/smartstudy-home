from django.forms import ModelForm
from .models import Resume


class ResumeForm(ModelForm):
    class Meta:
        model = Resume
        exclude = ('desc',)

    def __init__(self, *args, **kwargs):
        super(ResumeForm, self).__init__(*args, **kwargs)

        for k, v in self.Meta.model.descfields().iteritems():
            self.fields[k] = v['field']

    def save(self, commit=True):
        # do something with self.cleaned_data['temp_id']
        return super(ResumeForm, self).save(commit=commit)
