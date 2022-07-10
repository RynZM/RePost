#Multi Stage Dockerfile 
    #Advanced form of Docker Deployment

#Stage One
FROM python:3.8-buster as python-base

#Define Environment Variables for the container
ENV \
#Python
    PYTHONFAULTHANDLER=1 \ 
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYSETUP_PATH="/opt/pysetup" \
#pip & poetry 
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.1.13 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    VENV_PATH="/opt/pysetup/.venv" \
#System
    PATH="$POETRY_HOME/bin:$VENV_PATH/bin:/usr/src/app:$PATH"

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    #Dependencies missing from the base buster image
    curl \
    build-essential \
    ca-certificates \
    ssh

#Stage Two
FROM python-base as builder-base 

RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
WORKDIR $PYSETUP_PATH
COPY ./poetry.lock ./pyproject.toml ./

#Install runtime deps
RUN /opt/poetry/bin/poetry install --no-dev 

#Stage Three
FROM python-base as production
ENV REPOST_ENV=PRODUCTION
WORKDIR $PYSETUP_PATH
COPY --from=builder-base $POETRY_HOME $POETRY_HOME
COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH
RUN /opt/poetry/bin/poetry install --no-dev 

WORKDIR /usr/src/app
RUN chmod -R 777 /usr/src/
COPY . /usr/src/app
ENV PYTHONPATH="/usr/src/app/:$PYTHONPATH"

EXPOSE 8080
CMD ["gunicorn", "--config", "gunicorn_config.py", "wsgi:app"]
