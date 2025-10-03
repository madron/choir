from storages.backends import s3
from storages.utils import setting


class S3Storage(s3.S3Storage):
    def __init__(self, **settings):
        super().__init__(**settings)
        self.public_url = setting('AWS_S3_PUBLIC_URL')

    def url(self, *args, **kwargs):
        url = super().url(*args, **kwargs)
        if self.public_url and url.startswith(self.endpoint_url):
            url = url.replace(self.endpoint_url, self.public_url, 1)
        return url
