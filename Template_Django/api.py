from django.contrib.auth.models import User
from social.apps.django_app.default.models import UserSocialAuth
from tastypie import fields
from tastypie.resources import ModelResource


class UserResource(ModelResource):

    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'

class UserSocialAuthResource(ModelResource):

    class Meta:
        queryset = UserSocialAuth.objects.all()
        resource_name = 'UserSocialAuth'
