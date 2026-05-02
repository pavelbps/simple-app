FROM python:3.12-slim

ARG PORT="5000"
ENV PORT=${PORT}
WORKDIR /app

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

RUN useradd -m appuser
USER appuser

EXPOSE ${PORT}

HEALTHCHECK CMD curl -f http://localhost:${PORT}/health || exit 1

ENTRYPOINT ["sh", "-c"]
CMD ["gunicorn main:app --bind 0.0.0.0:${PORT}"]
