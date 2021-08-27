# from os import times
from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User

# 강의9.0 - 1.command만들기.
# 강의9.2 - 복붙해와서 user에 맞게 수정.
class Command(BaseCommand):

    help = "This command creates many users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int,  # integer로 바꿔줌.
            help="How many users do you want to create?",
        )

    def handle(self, *args, **options):
        number = options.get("number", 1)
        seeder = Seed.seeder()
        seeder.add_entity(User, number, {"is_staff": False, "is_superuser": False})
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} users created !"))
        # 죠낸 신기하네 진짜....가짜로 이렇게 생성이 된다는게 ㄹㅇ.
