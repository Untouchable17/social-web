from django.template.defaultfilters import slugify
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.dispatch import receiver
from django.utils import timezone
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, db_index=True, verbose_name="Заголовок")
    slug = models.SlugField(unique=True)
    body = models.TextField(blank=True, db_index=True, verbose_name="Контент блога")
    photo = models.ImageField(upload_to='uploads/blog_pictures', blank=True, verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    replace_at = models.DateTimeField(auto_now=True, verbose_name="Дата редактирования")
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-created_at']


class Comment(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)

    def get_success_url(self):
        return reverse('post-list', kwargs={'pk': self.pk})


class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name='Пользователь', related_name='profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=120, blank=True, null=True)
    picture = models.ImageField(blank=True, default='default.jpg', upload_to='uploads/profile_pictures')
    followers = models.ManyToManyField(User, blank=True, related_name='followers')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# class Notification(models.Model):
#     notification_type = models.IntegerField()
#     to_user = models.ForeignKey(User, related_name='notification_to', null=True, on_delete=models.CASCADE)
#     from_user = models.ForeignKey(User, related_name='notification_from', null=True, on_delete=models.CASCADE)
#     post = models.ForeignKey('Post', related_name='+', blank=True, null=True, on_delete=models.CASCADE)
#     comment = models.ForeignKey('Comment', related_name='+', blank=True, null=True, on_delete=models.CASCADE)
#     date = models.DateTimeField(default=timezone.now)
#     user_seen = models.BooleanField(default=False)


class ThreadModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')


class MessageSend(models.Model):
    thread = models.ForeignKey('ThreadModel', on_delete=models.CASCADE, blank=True, null=True, related_name='+')
    sender_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    receiver_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    body = models.CharField(max_length=800)
    image = models.ImageField(upload_to='uploads/messages_pictures', blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)











