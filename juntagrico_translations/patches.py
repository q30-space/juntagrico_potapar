from juntagrico.admins.forms.job_copy_form import JobMassCopyForm
from juntagrico.admins.job_admin import JobCopy
from juntagrico.entity.jobs import RecuringJob, OneTimeJob


def get_fieldsets(self, request, obj=None):
    if self.is_mass_copy_view(request):
        # mask fieldset and let modeltranslation handle the patching
        self.__fieldsets = self.fieldsets
        self.fieldsets = self.copy_fieldsets
        copy_fieldsets = super(JobCopy, self).get_fieldsets(request, obj)
        self.fieldsets = self.__fieldsets
        del self.__fieldsets
        return copy_fieldsets
    return super(JobCopy, self).get_fieldsets(request, obj)

JobCopy.get_fieldsets = get_fieldsets


def save(self, commit=True):
    inst = self.instance

    # collect additional description in every language
    additional_description = {
        k: v for k, v in self.cleaned_data.items() if k.startswith('additional_description_')
    }

    for dt in self.get_datetimes(self.cleaned_data):
        new_job = RecuringJob(
            type=inst.type,
            slots=inst.slots,
            infinite_slots=inst.infinite_slots,
            time=dt,
            multiplier=inst.multiplier,
            **additional_description,
            duration_override=inst.duration_override,
            pinned=inst.pinned,
        )
        if commit:
            new_job.save()
        self.new_jobs.append(new_job)
    return self.new_jobs[0] if self.new_jobs else None

JobMassCopyForm.save = save



orig_convert_to_oj = RecuringJob.convert

def convert_to_oj(self):
    translatables = {
        translatable: value
        for translatable, value in self.__dict__.items()
        if translatable.startswith(f'additional_description_')
    }
    type = self.type

    ot_job = orig_convert_to_oj(self)
    for translatable, value in translatables.items():
        lang = translatable.rpartition('_')[2]
        description = [getattr(type, f'description_{lang}')]
        if value:
            description.append(value)
        setattr(ot_job, f'description_{lang}', '\n'.join(description))
        setattr(ot_job, f'displayed_name_{lang}', getattr(type, f'displayed_name_{lang}') or type.name)
    ot_job.save()
    return ot_job


RecuringJob.convert = convert_to_oj



orig_convert_to_rj = OneTimeJob.convert

def convert_to_rj(self, to_job_type=None):
    translatables = {
        translatable: value
        for translatable, value in self.__dict__.items()
        if translatable.startswith('description_') or translatable.startswith('displayed_name_')
    }

    recurring_job = orig_convert_to_rj(self, to_job_type)

    if to_job_type is None:
        for translatable, value in translatables.items():
            setattr(recurring_job.type, translatable, value)
        recurring_job.type.save()
    return recurring_job

OneTimeJob.convert = convert_to_rj
