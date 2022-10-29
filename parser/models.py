from django.db import models


class TelegramLogin(models.Model):
    logo = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=191)
    login = models.CharField(max_length=191)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    parent_id = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    alias = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class News(models.Model):
    category = models.ForeignKey('parser.Category', on_delete=models.CASCADE)
    main_photo = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=255)
    short_text = models.TextField()
    content = models.TextField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    main_news = models.DateTimeField(blank=True, null=True)
    slug = models.CharField(max_length=255)
    date_of_event = models.DateTimeField(blank=True, null=True)
    organizer = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField()
    view_count = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title
