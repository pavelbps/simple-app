# Simple DevOps App

## 📌 Описание
Простое REST API приложение на Python (Flask), упакованное в Docker, с локальным запуском через Docker Compose и автоматизацией через Ansible.

## ⚙️ Требования

- Python 3.12+
- Docker
- Docker Compose
- Ansible
- Make (GNU Make)

## Запуск локально
```
pip install -r app/requirements.txt
python app/main.py
```

## Docker
```
docker build -t simple-app .
docker run -p 5000:5000 simple-app
```

## Docker Compose
```
docker-compose up -d
```

## API
```text
GET /
GET /health
GET /api/users
POST /api/users
DELETE /api/users/<id>
```

## Тесты
```
pytest app/tests/
```

## Bash
```
./scripts/server-info.sh 
http://localhost:5000/health
```

## Ansible

Перед запуском:
- замените YOUR_IP на ваш сервер
- замените YOUR_USER на вашего пользователя
- настройте SSH доступ
```
ssh-copy-id YOUR_USER@YOUR_IP
```

```
ansible-playbook -i ansible/inventory.ini ansible/playbook.yml
```

## 🚀 Быстрый старт (через Makefile)
```
git clone git@github.com:pavelbps/simple-app.git
cd simple-app
```
```
make install
make run
```
### Проверка:
```
curl http://localhost:5000/health
```
## 🛠️ Makefile (основной интерфейс проекта)

Посмотреть доступные команды:
```
make help
```
Основные команды:
```
make install        # установить зависимости
make test           # запустить тесты
make lint           # проверить bash (shellcheck)
make run            # запустить приложение локально

make docker-build   # собрать docker образ
make docker-run     # запустить контейнер

make compose-up     # запустить через docker-compose
make compose-logs   # посмотреть логи
make compose-down   # остановить

make server-info    # диагностика сервера

make ansible-run    # развертывание через ansible
```
## 🌐 API Endpoints
| Метод  | URL                 | Описание                     |
|--------|---------------------|------------------------------|
| GET    | /                   | Hello world                  |
| GET    | /health             | Проверка состояния           |
| GET    | /api/users          | Список пользователе й        |
| POST   | /api/users          | Создать пользователя         |
| GET    | /api/users/{id}     | Получить пользователя        |
| DELETE | /api/users/{id}     | Удалить пользователя         |

Примеры
```
curl http://localhost:5000/
```
```
curl http://localhost:5000/health
```
```
curl -X POST http://localhost:5000/api/users \
  -H "Content-Type: application/json" \
  -d '{"name":"test","email":"test@test.com"}'
```
## 🧪 Тестирование
```
make test
```
или
```
pytest app/tests/ -v
```
## 🐳 Docker
```
make docker-build
make docker-run
```
## 🧱 Docker Compose
```
make compose-up
make compose-logs
make compose-down
```
## 🖥️ Bash-скрипт диагностики
```
make server-info
```
или
```
./scripts/server-info.sh http://localhost:5000/health
```
## 🤖 Ansible (развертывание)
Отредактировать inventory:
```
[webservers]
app-server ansible_host=YOUR_IP ansible_user=YOUR_USER
```
## Запуск:
```
make ansible-run
```
## 📁 Структура проекта

```text
simple-app/
├── app/               # Основное приложение
├── scripts/           # Вспомогательные скрипты
├── ansible/           # Ansible конфигурации
├── Dockerfile         # Сборка контейнера
├── docker-compose.yml # Оркестрация сервисов
├── Makefile           # Команды автоматизации
└── README.md          # Документация проекта
```

## ⚠️ Troubleshooting
Порт занят
```
lsof -i :5000
```
## Docker не запускается
```
sudo systemctl status docker
```
## Ansible не подключается
```
ansible all -i ansible/inventory.ini -m ping
```
