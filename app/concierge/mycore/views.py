from http import HTTPStatus

from django.core import serializers
from django.core.serializers import SerializerDoesNotExist
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView

from mycore import models


def api_serializer(request, object_type, object_id):
    try:
        model = getattr(models, object_type.capitalize())
        return HttpResponse(
            serializers.serialize(
                request.GET['format'],
                [model.objects.get(id=object_id)]
            )
        )
    except (AttributeError, SerializerDoesNotExist, models.Tenant.DoesNotExist,
            models.Room.DoesNotExist, models.Journal.DoesNotExist):
        return HttpResponse(status=HTTPStatus.NOT_FOUND)


class HomePageView(TemplateView):
    template_name = "index.html"


class TenantListView(ListView):

    model = models.Tenant
    template_name = 'tenant_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Tenant list'] = models.Tenant.objects.all()
        return context


class RoomListView(ListView):

    model = models.Room
    template_name = 'room_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Room list'] = models.Room.objects.all()
        return context


class JournalListView(ListView):

    model = models.Journal
    template_name = 'journal_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Journal list'] = models.Journal.objects.all()
        return context


class TenantDetailView(DetailView):

    model = models.Tenant
    template_name = 'tenant_detail.html'
