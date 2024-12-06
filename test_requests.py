import requests

# Пример успешного запроса для формы Order Form
data = {
    "lead_email": "test@example.com",
    "order_date": "2023-12-06",
    "contact_number": "+7 123 456 78 90",
}
response = requests.post("http://localhost:8000/get_form/", data=data)
print("Success first response:", response.json())  # Success first response: {'template_name': 'Order Form'}

# Пример успешного запроса для формы Feedback Form
data = {"feedback_text": "Test feedback text"}
response = requests.post("http://localhost:8000/get_form/", data=data)
print("Success second response:", response.json())  # Success second response: {'template_name': 'Feedback Form'}

# Пример неуспешного запроса
data = {
    "random_text": "hello world",
    "random_date": "06.12.2023",
}
response = requests.post("http://localhost:8000/get_form/", data=data)
print("Invalid response:", response.json())  # Invalid response: {'random_text': 'text', 'random_date': 'date'}
