import os
import uuid
from datetime import datetime


def uploaded_filepath(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    today = datetime.now().strftime('%Y-%m-%d')
    return os.path.join(instance.__class__.__name__, today, filename)
