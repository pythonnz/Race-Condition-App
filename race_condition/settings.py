import os

SECRET_KEY = os.environ.get("SECRET_KEY", "dev")
# ADMIN_PASSWORD_HASH = os.environ["ADMIN_PASSWORD_HASH"]
DEBUG = True
REGISTRATION_LIMIT = int(os.environ.get("REGISTRATION_LIMIT", 1))
