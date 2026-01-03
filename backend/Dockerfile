FROM python:3.11-slim

WORKDIR /app

# Install system dependencies for LibreOffice and Fonts
# fonts-noto-cjk is for Chinese support
RUN apt-get update && apt-get install -y --no-install-recommends \
  libreoffice-writer \
  default-jre \
  fonts-noto-cjk \
  && rm -rf /var/lib/apt/lists/*

RUN pip install poetry

COPY pyproject.toml ./
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi --no-root

COPY . .

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
