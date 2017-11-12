from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

RELATIONSHIP_FOLLOWING = 1
RELATIONSHIP_BLOCKED = 2
RELATIONSHIP_STATUSES = (
    (RELATIONSHIP_FOLLOWING, 'Following'),
    (RELATIONSHIP_BLOCKED, 'Blocked'),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    relationships = models.ManyToManyField('self', through='Relationship', symmetrical=False, related_name='related_to')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.name
    
    def add_relationship(self, profile, status):
        relationship, created = Relationship.objects.get_or_create(
            from_profile=self,
            to_profile=profile,
            status=status)
        return relationship

    def remove_relationship(self, profile, status):
        Relationship.objects.filter(
            from_profile=self,
            to_profile=profile,
            status=status).delete()
        return
    
    def get_relationships(self, status):
        return self.relationships.filter(
            to_profiles__status=status,
            to_profiles__from_profile=self)

    def get_related_to(self, status):
        return self.related_to.filter(
            from_profiles__status=status,
            from_profiles__to_profile=self)
    
    def get_following(self):
        return self.get_relationships(RELATIONSHIP_FOLLOWING)
    
    def get_followers(self):
        return self.get_related_to(RELATIONSHIP_FOLLOWING)
    
    def get_friends(self):
        return self.relationships.filter(
            to_profiles__status=RELATIONSHIP_FOLLOWING,
            to_profiles__from_profile=self,
            from_profiles__status=RELATIONSHIP_FOLLOWING,
            from_profiles__to_profile=self)

class Relationship(models.Model):
    from_profile = models.ForeignKey(Profile, related_name='from_profiles')
    to_profile = models.ForeignKey(Profile, related_name='to_profiles')
    status = models.IntegerField(choices=RELATIONSHIP_STATUSES)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()