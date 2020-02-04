from django.db import models
from django.urls import reverse


class Tenant(models.Model):
    """
    Room's owner/tenant
    """
    first_name = models.CharField(
        'First name',
        max_length=250,
    )
    last_name = models.CharField(
        'Last name',
        max_length=250,
    )
    date_of_birth = models.DateField(
        blank=True,
        null=True,
        db_index=True,
    )
    phone = models.CharField(
        'Phone num',
        max_length=20,
        blank=True,
        null=True,
    )
    photo = models.ImageField(
        'Photo',
        upload_to='tenant',
        help_text='Photo of the tenant',
        null=True,
        blank=True
    )
    notes = models.TextField(
        blank=True,
        null=True,
    )

    def get_absolute_url(self):
        return reverse('tenant-detail', args=[str(self.id)])

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.fullname

    class Meta:
        ordering = ['first_name', 'last_name']
        indexes = [
            models.Index(fields=['first_name', 'last_name']),
        ]


class Room(models.Model):

    FREE, BUSY = ('FR', 'BU')
    ROOM_STATUSES = (
        ('FREE', 'Free'),
        ('BUSY', 'Busy')
    )

    number = models.IntegerField(
        help_text='Number of the room'
    )
    maximum_guest = models.IntegerField(
        blank=True,
        null=True,
        help_text='Maximum amount of guests for same time'
    )
    owner = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        help_text='Owner/Tenant of the room'
    )
    room_status = models.CharField(
        max_length=250,
        choices=ROOM_STATUSES,
        blank=True,
        null=True,
    )


class Journal(models.Model):
    created = models.DateTimeField(
        blank=True,
        null=True,
        db_index=True,
    )
    room = models.ForeignKey(
        'Room',
        on_delete=models.CASCADE,
    )
    guests_cnt = models.IntegerField(
        blank=True,
        null=True,
        help_text='How many guests are accepted'
    )
    is_kept = models.BooleanField(
        blank=True,
        null=True,
        help_text='Action type does concierge keep key or not'
    )
