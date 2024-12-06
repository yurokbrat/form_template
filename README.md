# Form Template API
## Тестовые данные
В качестве тестовых данных используется 2 формы: 
- _Order Form_
  ```json
    {
        "name": "Order Form",
        "fields": [
            {"name": "lead_email", "type": "email"},
            {"name": "order_date", "type": "date"},
            {"name": "contact_number", "type": "phone"}
        ]
    }
    ```
- _Feedback Form_
    ```json
        {
            "name": "Feedback Form",
            "fields": [
                {"name": "feedback_text", "type": "text"}
            ]
        }
    ```
## Подготовка тестовых данных
1. Запустите Docker.
    ```bash
   docker-compose up --build

2. Скопируйте тестовые данные (test_data.json) в контейнер MongoDB:
    ```bash
   docker cp test_data.json mongodb_container:/data/test_data.json

3. Импортируйте тестовые данные:
    ```bash
   docker exec -i mongodb_container mongoimport --db form_database --collection form_templates --file /data/test_data.json --jsonArray

### Теперь API доступно по по адресу _http://localhost:8000/get_form/_.

## Пример запроса
1. ### Успешный запрос:
   - **Request** 
       ```json
        {
            "lead_email": "test@example.com",
            "order_date": "2023-12-06",
            "contact_number": "+7 123 456 78 90"
        }
        ```
    - **Response**
        ```json
        {
            "template_name": "Order Form"
        }
       ```
2. ### Неуспешный запрос:
   - **Request** 
     ```json
      {
          "unknown_field": "hello world",
          "random_date": "06.12.2023"
      }
      ```
   - **Response**
       ```json
       {
           "unknown_field": "text",
           "random_date": "date"
       }
       ```
---

## Запуск тестового скрипта для проверки запросов
Чтобы запустить скрипт для проверки запросов, запустите докер и откройте файл `test_request.py`

```bash
docker compose up -d
python test_requests.py 
```
