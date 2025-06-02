# 🌐 Vacation Management System – Backend

A clean and functional full-stack backend project built with **Python** and **SQLite**, part of a Full Stack Web Development course. This RESTful API allows user authentication, vacation listings, and interaction through likes/unlikes. Role-based access ensures separation between admin and regular users.

---

## 📚 Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Database Schema](#database-schema)
- [Installation](#installation)
- [Usage](#usage)
- [API Overview](#api-overview)
- [Testing with Postman](#testing-with-postman)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Contributors](#contributors)
- [License](#license)

---

## ✨ Features

- 🔐 **User Authentication** (Login / Register)
- 👥 **Role Management** (Admin vs. User)
- 📆 **Vacation CRUD** for Admins
- ❤️ **Like / Unlike** vacations for Users
- 🗃️ SQLite relational schema with constraints & cascading deletes
- 🧪 Pre-built Postman test collection for all endpoints

---

## 🛠️ Tech Stack

| Layer        | Technology     |
|--------------|----------------|
| Language     | Python         |
| Database     | SQLite         |
| Architecture| MVC (Model-View-Controller) |
| API Test     | Postman        |
| Environment  | Virtualenv     |

---

## 🗃️ Database Schema

### Tables:

- **Roles**
  - `id` (PK), `name` (`Admin`, `User`)

- **Users**
  - `id` (PK), `first_name`, `last_name`, `email`, `password`, `role_id` (FK)

- **Countries**
  - `id` (PK), `name`

- **Vacations**
  - `id` (PK), `country_id` (FK), `description`, `start_date`, `end_date`, `price`, `image_filename`

- **Likes**
  - Composite Key: `user_id` (FK), `vacation_id` (FK)

> ✔️ **Cascade Delete:** Deleting a vacation also deletes its related likes.

---

## 🧰 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/vacation-management-backend.git
cd vacation-management-backend

# Set up a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## 🚀 Usage

- Run the server:
  ```bash
  python app.py
  ```

- Access the API via tools like Postman or curl.

---

## 📡 API Overview

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/register` | POST | Register a new user |
| `/login` | POST | Login with email and password |
| `/vacations` | GET | Get all vacations (sorted by start date) |
| `/vacations/:id` | GET | Get vacation by ID |
| `/vacations` | POST | Add new vacation *(Admin only)* |
| `/vacations/:id` | PUT | Update vacation *(Admin only)* |
| `/vacations/:id` | DELETE | Delete vacation *(Admin only)* |
| `/like` | POST | Like a vacation *(User only)* |
| `/like` | DELETE | Unlike a vacation *(User only)* |

---

## 🧪 Testing with Postman

A full set of API requests is included in a Postman collection:
- All CRUD endpoints
- Auth flows
- Like/Unlike functionality

> Run `app.py` and then import the collection into Postman.

---

## ⚙️ Configuration

Your SQLite DB should include:
- 2 Roles: Admin, User
- At least 2 users (1 Admin, 1 User)
- 10+ countries
- 12+ vacations
- Empty Likes table initially

Environment is managed using `virtualenv`.

---

## 🧩 Troubleshooting

- **User registration issues?** Check email format, password length (≥ 4 chars), and duplicate emails.
- **Vacation validation failed?** Ensure dates are valid and prices ≤ 10,000.
- **Cascade deletes not triggered?** Double-check your foreign key definitions.

---

## 👨‍💻 Contributors

Developed as part of the **John Bryce Full Stack Python Course** by participating students.  
Project guide: John Bryce Instructors.

---

## 📜 License

© 2025 John Bryce Education Group, part of Matrix. All rights reserved.

---

🎯 *This backend system provides a solid API foundation for any frontend integration in the future!*
