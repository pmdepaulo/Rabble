import pytest
import django
import os
from django.test import Client

from .factories import SubRabbleFactory, CommunityFactory, UserFactory, PostFactory, CommentFactory
from django.urls import reverse

@pytest.mark.django_db
def test_index_view():
    client = Client()
    user = UserFactory.create()
    client.force_login(user)
    default_community = CommunityFactory.create(name="Default", owner_user_id=user)
    sub_rabbles = SubRabbleFactory.create_batch(5, community_id=default_community)
    #print(sub_rabbles[0].rabble_name)
    response = client.get(reverse('index'))

    assert response.status_code == 200
    assert response.context is not None
    assert 'subrabbles' in response.context
    assert len(response.context['subrabbles']) == len(sub_rabbles)
    
    html = response.content.decode()
    for subrabble in sub_rabbles:
        assert subrabble.rabble_name in html
        assert subrabble.display_name in html
        assert subrabble.description in html

@pytest.mark.django_db
def test_subrabble_detail_view():
    client = Client()
    user = UserFactory.create()
    client.force_login(user)
    default_community = CommunityFactory.create(name="Default", owner_user_id=user)

    subrabble = SubRabbleFactory.create(community_id=default_community)
    posts = PostFactory.create_batch(5, subrabble_id=subrabble)
    comment1 = CommentFactory.create(post_id=posts[0])
    comment2 = CommentFactory.create(post_id=posts[1])
    comment3 = CommentFactory.create(post_id=posts[2])
    comment4 = CommentFactory.create(post_id=posts[3])
    comment5 = CommentFactory.create(post_id=posts[4])
    response = client.get(reverse('subrabble-detail', kwargs={'rabble_name': subrabble.rabble_name}))

    assert response.status_code == 200
    assert response.context is not None
    assert 'posts' in response.context
    assert len(response.context['posts']) == len(posts)
    
    html = response.content.decode()
    for post in posts:
        assert post.title in html
        assert post.body in html
        assert post.user_id.username in html
    
    contexts = response.context['posts']
    assert len(contexts) == 5
    for context in contexts:
        assert str(context.comment_count) in html
        assert context.comment_count == 1

@pytest.mark.django_db
def test_post_create_view():
    client = Client()
    user = UserFactory.create()
    client.force_login(user)
    default_community = CommunityFactory.create(name="Default", owner_user_id=user)

    subrabble = SubRabbleFactory.create(community_id=default_community)
    post = PostFactory.create(subrabble_id=subrabble)
    data = {
        'id': post.id,
        'title': post.id,
        'body': post.body,
        'user_id': post.user_id,
        'subrabble_id': post.subrabble_id,
        'created_at': post.created_at,
        'anonymous': post.anonymous
    }
    response = client.post(reverse('subrabble-detail', kwargs={'rabble_name': subrabble.rabble_name}), data=data)

    assert response.status_code == 200
    assert response.context is not None
    saved_post = PostFactory._meta.model.objects.filter(id=post.id)
    assert len(saved_post) == 1
    assert saved_post[0].title == post.title
    assert saved_post[0].body == post.body
    assert saved_post[0].user_id == post.user_id
    assert saved_post[0].subrabble_id == post.subrabble_id