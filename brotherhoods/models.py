from django.db import models

# Create your models here.
class Brotherhood(models.Model):
    name = models.CharField(max_length=300)
    contact_email = models.CharField(max_length=100)
    foundation_date = models.DateField(blank=True, null=True)
    jump_order = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('jump_order',)

    def save(self, *args, **kwargs): # new
        """
        automatically populate jump order
        """
        next_jump_order = Brotherhood.objects.all().count() + 1

        self.jump_order = next_jump_order
        super(Brotherhood, self).save(*args, **kwargs)

    def __str__(self):
        return "{} {}".format(self.jump_order, self.name)
