# Weather App

## Описание
Простое веб-приложение, которое отдаёт случайную температуру.  
Упаковано в Docker.  
Мониторинг — через healthcheck в Docker Compose.

## Запуск
docker compose up -d --build

Локалхосты для проверки

Приложение (температура)

http://localhost:8000/


Метрики приложения

http://localhost:8000/metrics


Health-check

http://localhost:8000/health


Prometheus

http://localhost:9090/


Blackbox Exporter UI 

http://localhost:9115/


Grafana

http://localhost:3000/


Логин:

admin / admin
