from rest_framework import serializers
from tickets import models

class TicketSerializer(serializers.ModelSerializer):
	class Meta:
		fields = (
			'id',
			'title',
			'description'
		)
		model = models.Ticket
