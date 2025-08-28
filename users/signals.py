from django.contrib.auth import get_user_model
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Student

@receiver(post_migrate)
def set_default_student_user(sender, **kwargs):
    
    if sender.name != "users":
        return

    User = get_user_model()
    default_user, _ = User.objects.get_or_create(
        username="default_user",
        defaults={"email": "default@example.com", "is_staff": False, "is_superuser": False}
    )
    Student.objects.filter(user__isnull=True).update(user=default_user)
