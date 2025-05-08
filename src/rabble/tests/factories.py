from factory import LazyAttribute, Faker, SubFactory, Sequence
from factory.django import DjangoModelFactory
from rabble.models import *

class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
    
    id = Sequence(lambda n: n)
    username = Faker('name')
    first_name = Faker('first_name')
    last_name = Faker('last_name')
    bio = Faker('sentence')
    email = Faker('email')

class CommunityFactory(DjangoModelFactory):
    class Meta:
        model = Communities
    
    id = Sequence(lambda n: n)
    name = Faker('word')
    owner_user_id = SubFactory(UserFactory)

class SubRabbleFactory(DjangoModelFactory):
    class Meta:
        model = SubRabbles
    
    id = Sequence(lambda n: n)
    rabble_name = Faker('word')
    display_name = LazyAttribute(lambda x: str(x.rabble_name).title())
    description = Faker('paragraph')
    community_id = SubFactory(CommunityFactory)
    public = Faker('boolean')
    allow_anon = Faker('boolean')

class PostFactory(DjangoModelFactory):
    class Meta:
        model = Posts
    
    id = Sequence(lambda n: n)
    title = Faker('word')
    body = Faker('paragraph')
    user_id = SubFactory(UserFactory)
    subrabble_id = SubFactory(SubRabbleFactory)
    created_at = Faker('date_time')
    anonymous = Faker('boolean')

class CommentFactory(DjangoModelFactory):
    class Meta:
        model = Comments
    
    id = Sequence(lambda n: n)
    body = Faker('sentence')
    user_id = SubFactory(UserFactory)
    post_id = SubFactory(PostFactory)
    created_at = Faker('date_time')
    anonymous = Faker('boolean')