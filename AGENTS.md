# AGENTS.md - System Instructions for "PDF Hero"

## Project Overview
**Name:** PDF Hero
**Description:** A free, web-based file-to-PDF converter (Word, Images) designed for low-resource environments.
**Role:** You are a Senior Full Stack Software Architect specializing in Python (FastAPI), React, and Clean Architecture.

---

## 1. Backend Specifications (Python/FastAPI)

### Architecture Style
- **Pattern:** Clean Architecture (Onion Architecture).
- **Strict Separation:** - `src/domain`: Entities (Pure Python, no libs).
    - `src/use_cases`: Business logic & interactors.
    - `src/interfaces`: Abstract Base Classes (Ports).
    - `src/adapters`: Implementation of interfaces (FastAPI routers, File converters).
    - `src/infrastructure`: Frameworks, Drivers, External libs.

### Coding Standards
- **Language:** Python 3.11+
- **Dependency Manager:** Poetry
- **Typing:** Strict Type Hinting (`typing` module) is mandatory.
- **Documentation:** Google-style docstrings for all public methods.
- **Testing:** Pytest is required for all Use Cases.
- **Error Handling:** Create a custom `DomainException` base class. Never return raw 500 errors; catch and log them using `structlog`.

### Critical Business Logic
- **No Database:** Do not set up SQL/NoSQL. Use temporary file storage handling (`tempfile`).
- **Concurrency Control:** Implement `asyncio.Semaphore` to strictly limit concurrent heavy tasks (LibreOffice) to **maximum 2** processes to prevent OOM on 1GB RAM servers.
- **File Limits:** - Max size: 10MB.
    - Types: `.doc`, `.docx`, `.jpg`, `.png`.
    - Validation: Check Magic Numbers (MIME type), not just extensions.

---

## 2. Frontend Specifications (React)

### Tech Stack
- **Framework:** React 18+ (Vite)
- **Language:** TypeScript (Strict mode)
- **Styling:** Tailwind CSS

### UI/UX & Layout
- **Target Device:** **Desktop Only**.
- **Mobile Guard:** Implement a check at the root level. If viewport width < 1024px, hide the app and render a full-screen "Desktop Only" message overlay.
- **Layout Structure:**
    - **Single Column Layout:** Use a centered container for the main converter tool.
    - **Auto Ads:** No manual ad containers. Let Google Auto Ads handle the placement.
- **Aesthetics:** Clean, professional, "Google Drive-like" feel. Use Blue (#2563EB) for primary actions.
- **Theme Support:** Default to **Dark Theme**. Provide a toggle switch (Sun/Moon icon) for users to switch to Light Theme. Use CSS variables for easy theme swapping.

---

## 3. Infrastructure & DevOps (Docker/AWS)

### Docker Optimization (Crucial)
- **Base Image:** Use `python:3.11-slim-bookworm` to keep size down.
- **LibreOffice Installation:** - Must use `--no-install-recommends` to avoid installing GUI/docs.
    - Install minimal dependencies: `libreoffice-writer`, `libreoffice-java-common`, `default-jre-headless`, `fonts-noto-cjk`.
- **Cleanup:** Clear apt lists (`rm -rf /var/lib/apt/lists/*`) in the same RUN instruction.

### Deployment Context
- **Platform:** AWS EC2 (Low spec).
- **Proxy:** Nginx as a reverse proxy for both Frontend (Static files) and Backend (Uvicorn).
- **SSL:** Configuration placeholder for Certbot (Let's Encrypt).
- **CI/CD:** GitHub Actions workflow to run tests -> build image -> push to registry.

### Monitoring
- **Logs:** JSON structured logging.
- **Sentry:** Integrate Sentry SDK in both Backend (FastAPI middleware) and Frontend (ErrorBoundary).

---

## 4. Development Workflow for Agent
When asked to generate code, follow this sequence:
1.  **Scaffold:** Create directory structure first.
2.  **Domain:** Define core Entities and Interfaces.
3.  **Core:** Implement Use Cases with Unit Tests.
4.  **Adapters:** Implement Converters (Pillow/LibreOffice) and API Routers.
5.  **UI:** Build React components connecting to APIs.
6.  **Config:** Dockerfiles and Nginx setup.