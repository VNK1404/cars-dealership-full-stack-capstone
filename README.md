# Cars Dealership Full-Stack Cloud Development Capstone

A full-stack cloud application designed for national car dealership management, multi-branch catalog browsing, user authentication, customer review submissions, and sentiment analysis.

---

## 🏛️ Architecture Overview

The application follows a distributed microservices and containerized multi-tier architecture:

```
+-------------------------------------------------------+
|                   Client Browser                      |
|  - Static Pages (About.html, Contact.html)            |
|  - React Frontend (Vite, Components, Register.jsx)   |
+---------------------------+---------------------------+
                            |
           REST API Calls / | JSON Responses
                            v
+-------------------------------------------------------+
|               Django Backend & Services               |
|  - Authentication (Login, Logout, Register)           |
|  - Dealership Directory & Proxy Endpoints             |
|  - Car Makes & Models Catalog                         |
|  - Review Submission & Sentiment Analytics Pipeline   |
+---------------------------+---------------------------+
                            |
                            v
+-------------------------------------------------------+
|             Express / Flask Microservices             |
|  - Dealership Records & Reviews API                   |
|  - Natural Language Sentiment Analysis Microservice   |
+-------------------------------------------------------+
```

---

## 📁 Repository Structure

```
cars-dealership-full-stack-capstone/
├── README.md
├── .gitignore
│
├── server/
│   ├── manage.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── dealership/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   └── frontend/
│       ├── static/
│       │   ├── About.html
│       │   ├── Contact.html
│       │   └── style.css
│       │
│       └── src/
│           └── components/
│               └── Register/
│                   ├── Register.jsx
│                   └── Register.css
│
├── frontend/
│   ├── package.json
│   ├── index.html
│   ├── Dockerfile
│   └── src/
│       ├── main.jsx
│       └── style.css
│
├── api/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
└── submission-evidence/
    ├── django_server.txt
    ├── loginuser.txt
    ├── logoutuser.txt
    ├── getdealerreviews.txt
    ├── getalldealers.txt
    ├── getdealerbyid.txt
    ├── getdealersbyState.txt
    ├── getallcarmakes.txt
    ├── analyzereview.txt
    ├── CICD.txt
    └── deploymentURL.txt
```

---

## 🚀 API Endpoints

### 1. Dealership Services
- `GET /dealers/` or `GET /api/dealers`: Fetch all dealerships across all states.
- `GET /dealers/?state=<state_name>`: Filter dealerships by state.
- `GET /dealer/<dealer_id>/` or `GET /api/dealers/<dealer_id>`: Retrieve specific dealership details by ID.
- `GET /dealers/<state>` or `GET /api/dealers/state/<state>`: Fetch dealerships located in the specified state.

### 2. Reviews & Sentiment Analysis
- `GET /reviews/dealer/<dealer_id>/` or `GET /api/dealers/<dealer_id>/reviews`: Get all reviews for a specific dealership.
- `POST /add_review/` or `POST /api/dealers/<dealer_id>/reviews`: Submit a new review for a dealership.
- `POST /api/analyze`: Natural language sentiment analysis analyzer returning `positive`, `neutral`, or `negative`.

### 3. Car Makes & Models
- `GET /get_cars/` or `GET /api/cars`: Retrieve available car makes and models.

### 4. Authentication
- `POST /login/`: User authentication endpoint.
- `POST /logout/`: User session termination.
- `POST /register/` or `POST /djangoapp/register`: New user registration endpoint.

---

## 💻 Local Setup & Execution

### Prerequisites
- Python 3.10+
- Node.js 18+ / npm
- Git

### 1. Django Backend Setup
```bash
cd server
pip install -r requirements.txt
python manage.py runserver 0.0.0.0:8000
```
- Django API will be running on `http://127.0.0.1:8000/`.
- Static pages are accessible via `http://127.0.0.1:8000/static/About.html` and `http://127.0.0.1:8000/static/Contact.html`.

### 2. Flask Microservice Setup
```bash
cd api
pip install -r requirements.txt
python app.py
```
- Microservice will be running on `http://127.0.0.1:8000/`.

### 3. React Frontend Setup
```bash
cd frontend
npm install
npm run start
```
- Frontend application will be accessible at `http://localhost:5173/`.

---

## 🐳 Docker Containerization

Each component includes its own `Dockerfile` for containerized execution.

### Build and Run Frontend Container
```bash
cd frontend
docker build -t cars-dealership-frontend .
docker run -p 4173:4173 cars-dealership-frontend
```

### Build and Run Backend Container
```bash
cd server
docker build -t cars-dealership-backend .
docker run -p 8000:8000 cars-dealership-backend
```

### Build and Run API Microservice Container
```bash
cd api
docker build -t cars-dealership-api .
docker run -p 8000:8000 cars-dealership-api
```

---

## ☁️ Deployment Preparation

1. **Continuous Integration & Delivery (CI/CD)**: Configure GitHub Actions workflow (`.github/workflows/main.yml`) for automated linting, testing, and container registry publishing.
2. **Container Registry**: Push Docker images to IBM Cloud Container Registry (ICR) or Docker Hub.
3. **Cloud Deployment**: Deploy the container images on Kubernetes (IKS) / Red Hat OpenShift or IBM Code Engine.
4. **Environment Configuration**: Set production secrets (e.g. database credentials, API keys) securely via Kubernetes Secrets or Cloud Environment Variables.

---

## 🔒 Security Best Practices
- Never commit `.env` files, API keys, or cloud credentials to source control.
- Ensure strict `.gitignore` rules prevent tracking sensitive credentials.
- In production, set `DEBUG = False` and define explicit `ALLOWED_HOSTS` in Django settings.
