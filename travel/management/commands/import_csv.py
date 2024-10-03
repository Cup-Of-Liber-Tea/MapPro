# from django.core.management.base import BaseCommand
# from travel.models import Tourist
# import csv
# from django.core.files import File
# from django.conf import settings
# import os

# class Command(BaseCommand):
#     help = 'Import tourist data from CSV file'

#     def add_arguments(self, parser):
#         parser.add_argument('csv_file', type=str, help='Path to the CSV file')

#     def handle(self, *args, **options):
#         csv_file_path = options['csv_file']
        
#         with open(csv_file_path, 'r', encoding='utf-8') as file:
#             reader = csv.DictReader(file)
#             for row in reader:
#                 tourist = Tourist(
#                     id=row['Id'],
#                     name=row['Title'],
#                     description=row['Descriptions'],
#                     location=row['Location'],
#                     operating_hours=row['OPERATING HOURS'],
#                     entrance_fee=row['ENTRANCE FEE'],
#                     parking=row['PARKING']
#                 )
                
#                 # 이미지 처리
#                 if row['IMAGE']:
#                     image_path = os.path.join(settings.MEDIA_ROOT, row['IMAGE'])
#                     if os.path.exists(image_path):
#                         with open(image_path, 'rb') as img_file:
#                             tourist.image.save(row['IMAGE'], File(img_file), save=False)
                
#                 tourist.save()
        
#         self.stdout.write(self.style.SUCCESS('Successfully imported tourist data'))