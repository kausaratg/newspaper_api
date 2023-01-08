from rest_framework import serializers

class ArticleSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    main_text =  serializers.CharField()
    published_time =serializers.DateField()
    is_active = serializers.BooleanField()
    created_time = serializers.DateTimeField(read_only=True)
    updated_time = serializers.DateTimeField(read_only = True)

    def create(self):
        pass

    def update(self):
        pass

   