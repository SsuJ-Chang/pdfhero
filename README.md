# PDF Hero

> **A Free, Privacy-First PDF Conversion Tool**

[繁體中文](./README.zh-TW.md) | English

[![Live Demo](https://img.shields.io/badge/demo-live-success)](https://pdfhero.rj-tw.com)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## ✨ Features

- 🚀 **Lightning Fast** - Convert images and Word documents to PDF in seconds
- 🔒 **Privacy First** - No database, files auto-deleted after conversion
- 💰 **Forever Free** - Supported by ads, completely free for users
- 🎨 **Modern UI** - Clean, dark-mode-first interface
- 📱 **Desktop Optimized** - Designed for desktop users with mobile blocking
- 🌐 **No Registration** - Use immediately without sign-up

## 🎯 Supported Conversions

| From | To | Status |
|------|-----|--------|
| Images (PNG, JPG, JPEG, WebP) | PDF | ✅ |
| Word Documents (DOC, DOCX) | PDF | ✅ |
| Excel Spreadsheets | PDF | 🔜 Coming Soon |
| PowerPoint Presentations | PDF | 🔜 Coming Soon |

## 🛠️ Tech Stack

### Frontend
- **React 18** with TypeScript
- **Vite** for blazing-fast development
- **Tailwind CSS** for styling

### Backend
- **FastAPI** (Python 3.11+)
- **LibreOffice Headless** for document conversion
- **Pillow** for image processing

### Infrastructure
- **Docker & Docker Compose** for containerization
- **AWS EC2** for hosting
- **Nginx** as reverse proxy
- **Let's Encrypt** for SSL/TLS
- **GitHub Actions** for CI/CD

## 🚀 Quick Start

### Prerequisites

- Docker & Docker Compose
- Git

### Local Development

```bash
# Clone the repository
git clone https://github.com/SsuJ-Chang/pdfhero.git
cd pdfhero

# Start all services
docker-compose up --build

# Access the application
# Frontend: http://localhost:5173
# Backend API: http://localhost:8000
```

### Environment Setup

The application works out of the box with Docker Compose. No additional environment variables are required for local development.

## 🏗️ Project Structure

```
pdfhero/
├── backend/             # FastAPI backend
│   ├── src/
│   │   ├── domain/     # Business entities & interfaces
│   │   ├── use_cases/  # Application logic
│   │   ├── infrastructure/ # Converters implementation
│   │   └── adapters/   # API controllers
│   └── tests/          # Unit tests
├── frontend/           # React frontend
│   ├── src/
│   │   ├── components/ # React components
│   │   ├── api/       # API client
│   │   └── contexts/  # React contexts
│   └── public/        # Static assets
├── nginx/             # Nginx configuration
└── scripts/           # Deployment scripts
```

## 🎨 Design Philosophy

### Privacy-First Architecture
- **No Database**: All conversions happen in-memory
- **Auto-Cleanup**: Temporary files deleted immediately after download
- **Zero Tracking**: No user data stored (except analytics)

### Resource Optimization
- **Low-Memory Design**: Runs on 1GB RAM with 2GB swap
- **Concurrency Control**: `asyncio.Semaphore` prevents OOM
- **Minimal Docker Images**: Using slim base images

### Desktop-First Experience
- **Mobile Blocking**: Redirect mobile users with friendly message
- **Drag & Drop**: Intuitive file upload
- **Dark Mode**: Eye-friendly default theme

## 📊 Analytics & Monetization

- **Google Analytics 4**: Custom event tracking for conversions
- **Google AdSense**: Auto Ads for revenue
- **SEO Optimized**: Comprehensive meta tags and sitemap

## 🚢 Deployment

The application is designed to run on low-spec infrastructure:

### AWS EC2 Requirements
- **Instance**: t3.micro or t2.micro
- **OS**: Ubuntu 22.04 LTS
- **RAM**: 1GB + 2GB Swap
- **Storage**: 10GB minimum

### Automated Deployment

Every push to `main` branch triggers automatic deployment via GitHub Actions:

```bash
git push origin main
# ☕ Wait ~60 seconds
# ✅ Changes live at https://pdfhero.rj-tw.com
```

For detailed deployment instructions, see [docs/GITHUB_ACTIONS_SETUP.md](docs/GITHUB_ACTIONS_SETUP.md)

## 🧪 Testing

```bash
# Run unit tests
docker-compose run backend pytest

# Run with coverage
docker-compose run backend pytest --cov=src
```

## 📝 API Documentation

Once the backend is running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with ❤️ by [RJ Chang](https://github.com/SsuJ-Chang)
- Powered by open-source technologies
- Special thanks to the FastAPI and React communities

## 📧 Contact

- Website: [pdfhero.rj-tw.com](https://pdfhero.rj-tw.com)
- GitHub: [@SsuJ-Chang](https://github.com/SsuJ-Chang)

---

**⭐ If you find this project useful, please consider giving it a star!**
