from django.contrib import admin
from .models import User, User_Followers, Communities, Community_Members, \
SubRabbles, SubRabble_Members, SubRabble_Admin, Posts, Comments, Likes, Conversations, \
Conversation_Members, Conversation_Messages

# Register your models here.
admin.site.register(User)
admin.site.register(User_Followers)
admin.site.register(Communities)
admin.site.register(Community_Members)
admin.site.register(SubRabbles)
admin.site.register(SubRabble_Members)
admin.site.register(SubRabble_Admin)
admin.site.register(Posts)
admin.site.register(Comments)
admin.site.register(Likes)
admin.site.register(Conversations)
admin.site.register(Conversation_Members)
admin.site.register(Conversation_Messages)