# FAQ Management API

This is a Django-based REST API for managing Frequently Asked Questions (FAQs) with **multi-language translation support**, **WYSIWYG editor integration**, and **caching** using Redis. It is designed to be scalable, efficient, and easy to use.

## **Installation**

### **1. Clone the Repository**
```bash
git clone https://github.com/KushalGoyal09/faq-app.git
cd faq-app
```

### **2. Set Up Virtual Environment**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

## **Running the Application**

### **Development**
```bash
python manage.py runserver
```
- Access the API at: `http://localhost:8000/api/faqs/`
- Access the admin panel at: `http://localhost:8000/admin/`


## **API Endpoints**

### **Fetch FAQs**
- **Default (English)**:
  ```bash
  GET /api/faqs/
  ```
- **Hindi**:
  ```bash
  GET /api/faqs/?lang=hi
  ```
- **Bengali**:
  ```bash
  GET /api/faqs/?lang=bn
  ```

---

## **Admin Panel**
- Access the admin panel at: `http://localhost:8000/admin/`
- Use the superuser credentials created during setup to log in.
- Manage FAQs, including translations and rich text formatting.

---

## **Contributing**
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "feat: Add your feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

