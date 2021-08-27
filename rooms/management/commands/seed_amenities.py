from os import times
from django.core.management.base import BaseCommand
from rooms.models import Amenity

# 강의9.0 - 1.command만들기.
class Command(BaseCommand):

    help = "This command creates amenities"

    # print("hello")
    # def add_arguments(self, parser):
    #     parser.add_argument(
    #         "--times", help="How many times do you want me to tell you that I love you?"
    #     )

    def handle(self, *args, **options):
        # print(args, options)
        amenities = [
            "Air conditioning",
            "Alarm Clock",
            "Balcony",
            "Bathroom",
            "Bathtub",
            "Bed Linen",
            "Boating",
            "Cable TV",
            "Carbon monoxide detectors",
            "Chairs",
            "Children Area",
            "Coffee Maker in Room",
            "Cooking hob",
            "Cookware & Kitchen Utensils",
            "Dishwasher",
            "Double bed",
            "En suite bathroom",
            "Free Parking",
            "Free Wireless Internet",
            "Freezer",
            "Fridge / Freezer",
            "Golf",
            "Hair Dryer",
            "Heating",
            "Hot tub",
            "Indoor Pool",
            "Ironing Board",
            "Microwave",
            "Outdoor Pool",
            "Outdoor Tennis",
            "Oven",
            "Queen size bed",
            "Restaurant",
            "Shopping Mall",
            "Shower",
            "Smoke detectors",
            "Sofa",
            "Stereo",
            "Swimming pool",
            "Toilet",
            "Towels",
            "TV",
        ]
        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amenities created!"))
        # 강의9.1 -완료. (뭐가 뭔지 모르겠다. 그냥 따라쳤다.)

        # times = options.get("times")
        # # print("i love you")
        # for i in range(0, int(times)):
        #     # print("i love you")  # 뭐지.. 신기하네..뭔지는 모르겠다..
        #     self.stdout.write(self.style.SUCCESS("I love you"))
