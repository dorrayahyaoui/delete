from django.db import models

# Create your models here.
class Subdomain(models.Model):
    sub_domain = models.CharField(db_index=True,max_length=200,
        unique=True,
        blank=False,
        error_messages={
            "unique": "This Subdomain already exists.",
        }
    )
    #profile = models.ForeignKey(Client,on_delete=models.CASCADE,default=1,related_name='subdomain')
    log=models.TextField(max_length=10000,default='nothing')
    status=models.CharField(max_length=200,default='nothing')
    port=models.IntegerField(default=8100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('sub_domain',)
        verbose_name = 'subdomain'
        verbose_name_plural = 'subdomains'
    def __str__(self):
        return self.sub_domain
