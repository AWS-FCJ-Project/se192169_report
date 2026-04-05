---
title: "Proposal"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 2. </b> "
---
<!-- {{% notice warning %}}
⚠️ **Note:** The information below is for reference purposes only. Please **do not copy verbatim** for your report, including this warning.
{{% /notice %}}

In this section, you need to summarize the contents of the workshop that you **plan** to conduct. -->

# EduTrust — AI-Integrated Online Exam Monitoring Platform  
## A Fullstack AWS Solution for Exam Proctoring and Smart Learning Support  

### 1. Executive Summary  
EduTrust is an online exam management platform designed for educational environments (schools, training centers), aiming to digitize exam organization, provide AI-assisted proctoring, and support learning through an intelligent chatbot. The system serves three main user groups: **Admin** (school), **Teacher** (create exams, proctor), and **Student** (take exams, view results). The backend uses FastAPI (Python) with MongoDB, Redis, Amazon S3, and a YOLO model for cheating detection via camera. The frontend is built with Next.js + Tailwind CSS and deployed on AWS Amplify.  

### 2. Problem Statement  
*Current Problems*  
Online exams face multiple challenges: manual proctoring is labor-intensive, cheating is difficult to detect (phones, multiple faces in frame, leaving the camera), there is no centralized system to manage classes — exams — results, and students lack intelligent learning support tools.  

*The Solution*  
EduTrust provides a comprehensive platform including:  
- **Class & Exam Management**: Admin creates classes, assigns homeroom/subject teachers; teachers create multiple-choice exams with secret keys and start/end times.  
- **AI Proctoring**: Integrates YOLOv26n (object detection) to detect violations in real time — including multiple faces (MULTIPLE_FACES), leaving camera (FACE_DISAPPEARED: cell Phone), and forbidden objects (FORBIDDEN_OBJECT). Evidence images are stored in Amazon S3 and logged in MongoDB.  
- **AI Learning Assistant**: A multi-agent system using Pydantic AI (technical, social, general, web search) helps students search knowledge, ask questions, and find learning materials.  
- **Authentication & Security**: JWT (via Cognito) with role-based access control (RBAC).  

*Benefits and ROI*  
The solution reduces manual proctoring workload, improves transparency and fairness, and automates grading with evidence stored in S3. Operational cost remains low by leveraging MongoDB Atlas (free tier), Redis Cloud, and AWS S3/Amplify. Estimated AWS cost is under 5 USD/month for a mid-size school.  

### 3. Solution Architecture  
EduTrust applies a **fullstack monorepo** architecture with a Python FastAPI backend and a Next.js frontend, deployed via Docker containers. Data is stored in MongoDB (users, exams, classes, submissions, violations), session/conversation cache uses Redis, and violation images are stored in Amazon S3.  

![EduTrust Solution Architecture](/images/2-Proposal/edutrust-architect.png)

*Services & Technology (aligned with the architecture)*  
- *AWS Amplify + CloudFront*: Hosts the Next.js frontend and delivers content via CDN.  
- *Amazon Route 53 + AWS ACM*: DNS and TLS/HTTPS certificate management.  
- *AWS WAF*: Web application firewall protection.  
- *Amazon VPC (public/private subnets)*: Network isolation and segmentation.  
- *Application Load Balancer (ALB)*: Distributes traffic to backend services.  
- *Amazon EC2 Auto Scaling*: Scales backend compute based on load.  
- *Amazon ECR*: Container registry for backend images.  
- *Amazon S3*: Stores violation images, ALB logs, and Terraform state.  
- *Amazon DynamoDB*: Key-value data store (as shown in the architecture).  
- *Amazon ElastiCache for Redis*: Cache/session layer for fast access.  
- *Amazon Cognito*: Authentication and user management.  
- *Amazon CloudWatch + VPC Flow Logs + SNS*: Monitoring, logs, and alerting.  
- *AWS KMS + SSM Parameter Store + PrivateLink*: Secrets and secure internal access.  
- *Terraform + GitHub Actions*: Infrastructure as Code and CI/CD automation.  

*Application Stack*  
- *FastAPI*: Async backend API framework with automatic docs (Swagger/ReDoc).  
- *Next.js 16 + Tailwind CSS v4*: Frontend SPA with App Router, server/client components.  
- *YOLOv26n (Ultralytics)*: Object detection for exam proctoring.  
- *Pydantic AI + LiteLLM*: Multi-agent orchestration for the learning assistant.  
- *Docker*: Containerize backend with multi-stage build (Ubuntu 24.04).  

*Component Design*  
- *Authentication (Auth)*: JWT access/refresh tokens, session via cookies, RBAC (admin/teacher/student).  
- *Class Management*: Assign homeroom/subject teachers, add/remove students, auto update status (active/inactive).  
- *Exam Management*: Create MCQ exams, auto generate secret keys, control start/end time, auto grading on submit.  
- *Camera Proctoring (Detection)*: CameraService receives frames, ObjectDetector (YOLO) detects violations, ViolationLogger writes MongoDB + S3, ScreenshotUtils captures evidence.  
- *AI Agent*: UnifiedAgent orchestrates sub-agents (technical, social, general, web_search) with tool delegation and WebSocket streaming.  

### 4. Technical Implementation  
*Implementation Phases*  
The project is divided into 5 main phases:  
1. *Study core AWS services*: Learn the services in the architecture (VPC, EC2/ALB/ASG, S3, ECR, Cognito, CloudWatch, KMS, SSM, WAF) and CI/CD/IaC workflows.  
2. *Research and design architecture*: Study technologies (FastAPI, Next.js, YOLO, Pydantic AI), design database schema, API contract, and system architecture.  
3. *Develop core features*: Build auth (Cognito JWT), class CRUD, exam management, and auto grading.  
4. *Integrate AI & Camera*: Integrate YOLO for violation detection, build multi-agent chatbot, connect S3/Redis.  
5. *Frontend & testing*: Complete Next.js dashboard for three roles, end-to-end testing, and containerization.  

*Technical Requirements*  
- *Backend*: Python ≥ 3.11, FastAPI, Motor (async MongoDB driver), Redis ≥ 5.0, Boto3 (AWS SDK), Ultralytics (YOLO), Pydantic AI + LiteLLM, Kreuzberg (document parsing), SlowAPI (rate limiting).  
- *Frontend*: Next.js 16, React 19, Tailwind CSS v4, Lucide React (icons), React Markdown + KaTeX (render math), ONNX Runtime Web, next-intl (i18n).  
- *Infrastructure*: Docker (multi-stage build), MongoDB Atlas, Redis Cloud, Amazon S3, AWS Amplify, Logfire (observability).  

### 5. Timeline & Milestones  
- *Weeks 1–2*: Study AWS services in the architecture (VPC, EC2/ALB/ASG, S3, ECR, Cognito, CloudWatch, KMS/SSM, WAF) and CI/CD/IaC workflows.  
- *Weeks 3–4*: Research technologies, design architecture and database schema.  
- *Weeks 5–6*: Develop backend core (auth, classes, exams, submissions).  
- *Weeks 7–8*: Integrate YOLO detection, AI chatbot (multi-agent), S3 storage.  
- *Week 9*: Develop frontend dashboard (admin/teacher/student views).  
- *Week 10*: Integration testing, performance optimization, and containerization.  

### 6. Budget Estimation  

*Architecture Assumptions*  
- Small environment (staging/small production), low-to-medium traffic.  
- Backend runs on EC2 Auto Scaling (t3.small, 2 instances), ALB running 24/7.  
- Frontend hosted on Amplify + CloudFront, with WAF enabled.  
- Violation data stored on S3 (~10–20 GB/month).  

*Infrastructure Cost (monthly estimate)*  
- VPC Endpoints (Interface for ECR/SSM/STS/Logs…): ~30–60 USD  
- EC2 Auto Scaling (2 x t3.small): ~30–40 USD  
- Application Load Balancer: ~16–25 USD  
- Amazon S3 (violation images, ALB logs, terraform state): ~2–6 USD  
- Amazon CloudFront + Amplify: ~1–5 USD  
- AWS WAF: ~5–10 USD  
- Amazon ElastiCache (Redis – small cache): ~15–25 USD  
- Amazon DynamoDB (low traffic): ~1–3 USD  
- Amazon ECR (image storage): ~1–3 USD  
- Amazon Cognito (<= 50k MAU): ~0–2 USD  
- Amazon CloudWatch + VPC Flow Logs + SNS: ~5–10 USD  
- AWS KMS + SSM Parameter Store: ~1–3 USD  
- Data Transfer: ~2–6 USD  

*Estimated total*: ~110–195 USD/month (including VPC Endpoints; depends on traffic and S3 storage).  

*Third-party API Costs*  
- OpenAI/LiteLLM API: depends on usage.  
- External search services (if used): depends on plan.  

### 7. Risk Assessment  
*Risk Matrix*  
- Low YOLO accuracy (false positive/negative): High impact, medium probability.  
- Student camera/network disconnection: Medium impact, medium probability.  
- API budget overrun (LLM calls): Medium impact, low probability.  
- Switching from MongoDB to MySQL changes schema & query complexity: Medium–high impact, medium probability.  

*Mitigation Strategies*  
- YOLO: Tune confidence threshold (min 0.5), alert only after multiple consecutive frames, allow manual teacher review.  
- Network: Client-side detection with ONNX Runtime Web (fallback), log locally and sync when online.  
- API cost: Rate limiting (SlowAPI), budget alerts, use lighter models for simple tasks.  
- Database: Repository abstraction, normalized schema, and migration scripts if switching to MySQL.  

*Contingency Plan*  
- Switch to manual proctoring if AI detection fails.  
- Use SQLite/local storage as fallback if MongoDB Atlas is unavailable.  
- Docker images allow deployment on any cloud provider (avoid AWS lock-in).  

### 8. Expected Outcomes  
*Technical improvements*: Automate proctoring with AI (YOLO) to replace manual monitoring. Auto-grading with evidence stored in S3. 24/7 multi-agent chatbot for student learning support.  
*Long-term value*: Scalable to multiple schools, supports multi-language (next-intl), integrates more exam types (essay with AI grading), and can evolve into a full SaaS education platform. Violation data accumulated over time can be used to improve detection models.
