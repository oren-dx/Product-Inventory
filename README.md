# WADP-L4 Demonstration-1 [Product Inventory]
# 🛒 Django Product Inventory System

A simple **Product Management Web Application** built with **Python and Django**.
This project provides user authentication and product management features, including product name, category, price, quantity, image, and availability status.

## 🚀 Features

* 🔐 Custom User Authentication
* 👤 User Registration & Login
* 📝 User Full Name
* 📦 Product Management
* 🏷️ Product Category
* 💰 Product Price
* 🔢 Product Quantity
* 🖼️ Product Image Upload
* ✅ Product Availability Status
* 📅 Product Creation Date
* 🗄️ Database Management with Django ORM

## 🛠️ Technologies Used

* **Python**
* **Django**
* **SQLite / Database**
* **HTML**
* **CSS**
* **Django ORM**
* **Pillow** — Image Upload Handling

## 📂 Main Models

### UserModel

A custom user model based on Django's `AbstractUser`.

python
class UserModel(AbstractUser):
    full_name = models.CharField(max_length=100, null=True)


### ProductDataModel

Stores product information such as:

* Product Name
* Category
* Price
* Quantity
* Product Image
* Product Status
* Created Date

## 📊 Product Status

The application supports two product statuses:

* **Available**
* **Out of Stock**

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repository.git
```

### 2. Go to the Project Directory

```bash
cd your-repository
```

### 3. Create a Virtual Environment

```bash
python -m venv env
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
env\Scripts\activate
```

**Linux / macOS:**

```bash
source env/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create Superuser

```bash
python manage.py createsuperuser
```

### 8. Run the Development Server

```bash
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

## 📁 Project Structure

```text
project/
│
├── app/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── admin.py
│
├── templates/
│   └── ...
│
├── media/
│   └── products_img/
│
├── manage.py
├── requirements.txt
└── README.md
```

## 🎯 Project Purpose

The main purpose of this project is to practice **Django backend development**, including:

* Custom User Models
* Django Models
* CRUD Operations
* Form Handling
* Image Upload
* Authentication
* Database Operations
* Django ORM

## 🔮 Future Improvements

Some features that can be added in the future:

* 🔍 Product Search
* 🏷️ Category Filtering
* 📄 Pagination
* 🛒 Shopping Cart
* ❤️ Wishlist
* 💳 Online Payment
* 📦 Order Management
* ⭐ Product Reviews
* 📊 Admin Dashboard
* 🔌 REST API using Django REST Framework

## 👨‍💻 Developer

**Oren Michael Dessai**

Python & Django Backend Developer
Interested in building web applications, REST APIs, and database-driven systems.

---

⭐ If you find this project useful, consider giving it a **star**!

