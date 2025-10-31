import requests
import json

BASE_URL = "http://127.0.0.1:8000/api/books/"

# 1️⃣ GET all books
response = requests.get(BASE_URL)
print("All Books:", response.json())

# 2️⃣ POST a new book
new_book = {
    "title": "Django REST Book",
    "author": "Mysha",
    "published_date": "2025-10-31",
    "price": 400.00
}
response = requests.post(BASE_URL, data=json.dumps(new_book), headers={"Content-Type": "application/json"})
book_id = response.json().get("id")  # save ID to test update/delete
print("Created Book:", response.json())

# 3️⃣ GET single book
response = requests.get(f"{BASE_URL}{book_id}/")
print("Single Book:", response.json())

# 4️⃣ PATCH (partial update)
update_data = {"price": 450.00}
response = requests.patch(f"{BASE_URL}{book_id}/", data=json.dumps(update_data), headers={"Content-Type": "application/json"})
print("Updated Book:", response.json())

# 5️⃣ DELETE book
# response = requests.delete(f"{BASE_URL}{book_id}/")
# print("Delete Status Code:", response.status_code)
