import pytest
import django
import os
from django.test import Client
from rest_framework.test import APIClient
from rest_framework import status

from .factories import SubRabbleFactory, CommunityFactory, UserFactory, PostFactory, CommentFactory
from django.urls import reverse
from rabble.models import *

@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
def test_subrabble_get(api_client):
    user = UserFactory.create()
    default_community = CommunityFactory.create(name="Default", owner_user_id=user)
    sub_rabble = SubRabbleFactory.create(community_id=default_community)

    response = api_client.get(reverse('api-subrabble-by-id', kwargs={'rabble_name': sub_rabble.rabble_name}))
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['id'] == sub_rabble.id
    assert response.json()['rabble_name'] == sub_rabble.rabble_name
    assert response.json()['display_name'] == sub_rabble.display_name
    assert response.json()['description'] == sub_rabble.description
    assert response.json()['community_id'] == sub_rabble.community_id.id
    assert response.json()['public'] == sub_rabble.public
    assert response.json()['allow_anon'] == sub_rabble.allow_anon

@pytest.mark.django_db
def test_post_post(api_client):
    user = UserFactory.create()
    api_client.force_login(user)
    default_community = CommunityFactory.create(name="Default", owner_user_id=user)
    sub_rabble = SubRabbleFactory.create(community_id=default_community)
    data = {
        'id': 0,
        'title': 'post test title',
        'body': 'this is a test post request',
        'author': user.username,
        'subrabble': sub_rabble.rabble_name,
        'anonymous': False
    }

    response = api_client.post(reverse('api-posts-by-subrabble', kwargs={'rabble_name': sub_rabble.rabble_name}), data)
    assert response.status_code == 201

    new_post = Posts.objects.get(id=response.data['id'])
    assert new_post.id == data['id']
    assert new_post.title == data['title']
    assert new_post.body == data['body']
    assert new_post.user_id.username == data['author']
    assert new_post.subrabble_id.rabble_name == data['subrabble']
    assert new_post.anonymous == data['anonymous']

@pytest.mark.django_db
def test_post_patch(api_client):
    user = UserFactory.create()
    api_client.force_login(user)
    default_community = CommunityFactory.create(name="Default", owner_user_id=user)
    sub_rabble = SubRabbleFactory.create(community_id=default_community)
    post = PostFactory.create(subrabble_id=sub_rabble)
    data = {
        'title': "Updated Title!"
    }

    response = api_client.patch(reverse('api-post-in-subrabble', args=[sub_rabble.rabble_name, post.id]), data)
    assert response.status_code == 200

    post.refresh_from_db()
    assert post.title == data['title']