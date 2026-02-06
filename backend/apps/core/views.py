from django.views.generic import TemplateView
from courses.models import Course
from apps.linguistics.models import LinguisticArea

class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Enviamos los datos reales de la base de datos
        context['courses'] = Course.objects.all()
        context['areas'] = LinguisticArea.objects.all()
        return context
