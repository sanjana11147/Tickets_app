from django.shortcuts import render

from rest_framework import generics

from tickets import models
from . import serializers


class ListTicket(generics.ListCreateAPIView):
	queryset = models.Ticket.objects.all()
	serializer_class = serializers.TicketSerializer


class DetailTicket(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.Ticket.objects.all()
	serializer_class = serializers.TicketSerializer
