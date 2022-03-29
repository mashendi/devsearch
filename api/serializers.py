from rest_framework.serializers import ModelSerializer, SerializerMethodField
from projects.models import Project, Tag, Review
from users.models import Profile


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

    owner = SerializerMethodField()

    def get_owner(self, obj):
        owner = obj.owner
        serializer = ProfileSerializer(owner, many=False)
        owner_name = serializer.data.get('name')
        return owner_name


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

    owner = ProfileSerializer(many=False)
    tags = TagSerializer(many=True)
    reviews = SerializerMethodField()

    def get_reviews(self, obj):
        reviews = obj.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return serializer.data
