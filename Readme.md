# 🚀 Flask API with CI/CD, Docker & Automated Deployment

## 📌 Overview
This project demonstrates a production-like DevOps setup for a Python Flask API using Docker, CI/CD pipelines, and automated deployment to a remote server.

The goal of this project was to simulate a real-world backend deployment workflow with health checks, rollback strategy, and service orchestration.

---

## 🏗️ Tech Stack

- Python (Flask)
- Docker & Docker Compose
- Nginx (reverse proxy)
- PostgreSQL
- Gunicorn (WSGI server)
- GitHub Actions (CI/CD)

---

## ⚙️ Features

### ✅ Containerized Application
- Multi-container setup using Docker Compose:
  - Flask API
  - PostgreSQL database
  - Nginx reverse proxy
  - pgAdmin (optional)

---

### ✅ CI/CD Pipeline
- Automated deployment using GitHub Actions
- SSH-based deployment to remote server
- Steps:
  1. Pull latest code
  2. Build Docker image
  3. Restart services
  4. Run health checks

---

### ✅ Health Checks
- Application endpoint: `/health`
- Docker HEALTHCHECK configured
- CI verifies application availability after deployment

---

### ✅ Rollback Strategy
- If health check fails:
  - Previous version is restored automatically
  - Deployment is marked as failed

---

### ✅ Database Initialization
- App waits for PostgreSQL to become available
- Automatic DB initialization on container startup

---

### ✅ Reverse Proxy (Nginx)
- Routes external traffic to Flask app
- Handles HTTP/HTTPS layer
- Prevents direct exposure of application container

---

## 🧪 Example Endpoints

- `/` – main endpoint
- `/health` – health check endpoint

---

## 🚀 Deployment Flow

```text
Developer push → GitHub → CI/CD pipeline → Remote server → Docker build → Run containers → Health check → Success / Rollback

📦 How to Run Locally

docker-compose up --build

🔥 Key DevOps Concepts Demonstrated

CI/CD automation
Infrastructure as Code (Docker Compose)
Service orchestration
Health monitoring
Zero-downtime mindset (rollback strategy)
Reverse proxy configuration
Dependency handling (DB readiness)

📈 Future Improvements
Use Docker registry (Docker Hub / ECR)
Add HTTPS with Let's Encrypt
Move deployment to cloud (AWS EC2)
Introduce Terraform for infrastructure provisioning

👩‍💻 Author

Kristina Perez
DevOps Engineer (Junior)

