import os, logging
from repost import app
from repost.flask_config import PORT, PREFIX

def rotate_logs():
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

if os.getenv('REPOST_ENV', '') == 'PRODUCTION':
    rotate_logs()

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=PORT)