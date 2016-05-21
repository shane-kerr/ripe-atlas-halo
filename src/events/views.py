from django.views.generic import TemplateView


class DashboardView(TemplateView):

    template_name = "events/dashboard.html"

    def get_context_data(self, **kwargs):
        """
        Generating variables that end up in the view goes here.
        """

        context = TemplateView.get_context_data(self, **kwargs)

        # Modify context here

        return context
