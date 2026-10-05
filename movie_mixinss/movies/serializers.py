from rest_framework import serializers
from movies.models import movie

# class movieserializer(serializers.Serializer):
#     title=serializers.CharField()
#     director=serializers.CharField()
#     language=serializers.CharField()
#     year=serializers.IntegerField()
#     rating=serializers.FloatField()
#     runtime=serializers.IntegerField()


#     def create(self,validated_data):
#      m=movie.objects.create(**validated_data)
#      return m

#     def update(self,instance,validated_data):
#        instance.title=validated_data.get('title',instance.title)
#        instance.director=validated_data.get('director',instance.director)
#        instance.language=validated_data.get('language',instance.language)
#        instance.year=validated_data.get('year',instance.year)
#        instance.rating=validated_data.get('rating',instance.rating)
#        instance.runtime=validated_data.get('runtime',instance.runtime)
#        instance.save()
#        return instance


class movieserializer(serializers.ModelSerializer):
    class Meta:
        model=movie
        fields='__all__'

        # or

        # fields=['title','director','language','rating','runtime']


#extra validation use validate() function

def validate(self,data):
    if data['rating'] < 5:
        raise serializers.ValidationError(" low rating movie")
    return data