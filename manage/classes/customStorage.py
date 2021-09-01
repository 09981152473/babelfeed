import os
from storages.backends.s3boto3 import S3Boto3Storage
from tempfile import SpooledTemporaryFile
from botocore.retries import bucket
import boto3
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html


class CustomStorage(S3Boto3Storage):
    bucket_name = "babelcastmedia"

    def _save_content(self, obj, content, parameters):
        """
        We create a clone of the content file as when this is passed to boto3 it wrongly closes
        the file upon upload where as the storage backend expects it to still be open
        """

        # Seek our content back to the start
        content.seek(0, os.SEEK_SET)

        # Create a temporary file that will write to disk after a specified size
        content_autoclose = SpooledTemporaryFile()

        # Write our original content into our copy that will be closed by boto3
        content_autoclose.write(content.read())

        # Upload the object which will auto close the content_autoclose instance
        super(CustomStorage, self)._save_content(obj, content_autoclose, parameters)
        
        # Cleanup if this is fixed upstream our duplicate should always close        
        if not content_autoclose.closed:
            content_autoclose.close()

    def delete_show(self, show_id):
        # so we need to delete everything in the folder
        response = self.listdir(show_id)[1]

        for object in response:
            self.delete(show_id + "/" + object)
     
    def delete_episode(self, eps):
        path = eps.get_absolute_url()

        if len(path) > 1:
            self.delete(path)
