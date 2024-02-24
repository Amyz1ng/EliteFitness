# upload_images_to_s3.py

from django.core.management.base import BaseCommand
from storages.backends.s3boto3 import S3Boto3Storage

class Command(BaseCommand):
    help = 'Upload images to AWS S3'

    def handle(self, *args, **options):
        # Get the S3 storage object
        storage = S3Boto3Storage()

        # Upload a file
        with open('path/to/your/image.jpg', 'rb') as file:
            storage.save('destination/path/in/s3/image.jpg', file)
