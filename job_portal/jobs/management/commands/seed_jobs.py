from django.core.management.base import BaseCommand 
from faker import Faker
from jobs.models import Job, Category 
from django.contrib.auth import get_user_model
import random

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        fake = Faker()
        
        User = get_user_model()
        employer = User.objects.filter(role='employer').first()
        if not employer:
            self.stderr.write(self.style.ERROR("No employer user with role='employer' found."))
            return
        
        categories = list(Category.objects.all())
        if not categories:
            self.stdout.write("No categories found. Creating default categories...")
            default_names = ['IT', 'Design', 'Marketing', 'Finance', 'Engineering', 'Healthcare']
            categories = [Category.objects.create(name=name) for name in default_names]
            self.stdout.write(self.style.SUCCESS("Default categories created."))

        for _ in range(20):
            Job.objects.create(
                title=fake.job(),
                company=fake.company(),
                location=fake.city(),
                description=fake.text(max_nb_chars=400),
                category=random.choice(categories),
                employer=employer
            )
        self.stdout.write(self.style.SUCCESS('Successfully created fake jobs with categories'))