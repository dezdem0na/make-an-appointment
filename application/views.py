from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.utils.translation import ugettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from django.views.decorators.http import require_http_methods
from application.forms import ApplicationForm, SpecialistForm
from application.models import Application, Specialist


class ApplicationCreateView(SuccessMessageMixin, CreateView):
    model = Application
    form_class = ApplicationForm
    success_url = reverse_lazy('application')
    success_message = _("You booked an appointment to %(specialist)s on %(appointment_ftd)s.")
    form_class_extra = SpecialistForm

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data,
                                           appointment_ftd='{:%H:%M %d/%m/%Y}'
                                           .format(self.object.appointment))

    def get_context_data(self, **kwargs):
        context = super(ApplicationCreateView, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form_extra' not in context:
            context['form_extra'] = self.form_class_extra()
        return context


@require_http_methods(["POST"])
def update_specialists(request):
    if request.is_ajax():
        data = list(Specialist.objects.filter(specialty__pk=request.POST['specialist_id'])
                    .values('id', 'name_first', 'name_last'))
        return JsonResponse(data, safe=False)
