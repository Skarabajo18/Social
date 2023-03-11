from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import RegexValidator
from django.utils.text import gettext_lazy as _




USER_TYPE = (('GRATIS', 'GRATIS'),
             ('PREMIUM', 'PREMIUM'),
             )








class UserAccount(AbstractUser):
    
    type = models.CharField(max_length=7,
                            choices=USER_TYPE,
                            default=USER_TYPE[1][0])



class UserProfile(models.Model):

	User = models.OneToOneField(UserAccount,
                                on_delete=models.CASCADE)
    
	
	def __str__(self):
		return f'Perfil de {self.User.username}'


	def following(self):
		user_ids = UserRelationship.objects.filter(from_user=self.User).values_list('to_user_id', flat=True)
		
		return UserAccount.objects.filter(id__in=user_ids)


	def followers(self):
		user_ids = UserRelationship.objects.filter(to_user=self.User).values_list('from_user_id', flat=True)
		
		return UserAccount.objects.filter(id__in=user_ids)



class UserRelationship(models.Model):
    from_user = models.ForeignKey(UserAccount,
                                  related_name='relationships',
                                  on_delete=models.CASCADE)
    to_user = models.ForeignKey(UserAccount,
                                related_name='related_to',
                                on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Interes : {str(self.from_user).upper()} - {str(self.to_user).upper()}'

    class Meta:
        indexes = [
            models.Index(fields=['from_user', 'to_user',]),
        ]

