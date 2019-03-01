from rest_framework import serializers
from .models import Brotherhood

class BrotherhoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brotherhood
        fields = ('id', 'name', 'contact_email', 'foundation_date',
                  'jump_order', )
        read_only_fields = ('jump_order',)          
