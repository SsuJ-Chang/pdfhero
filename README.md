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
- 📱 **Fully Responsive** - Works on desktop, tablet, and mobile devices
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
- **Concurrency Control**: `asyncio.Semaphore(3)` optimized for t3.micro throughput
- **Rate Limiting**: Nginx IP-based throttling (1 req/s, burst 5) to prevent abuse
- **Minimal Docker Images**: Using slim base images

### Responsive Experience
- **Mobile Support**: Fully responsive design for all screen sizes
- **Drag & Drop**: Intuitive file upload
- **Dark Mode**: Eye-friendly default theme

## 📊 Analytics & Monetization

- **Google Analytics 4**: Custom event tracking for conversions
- **Google AdSense**: Auto Ads for revenue
- **SEO Optimized**: Comprehensive meta tags and sitemap

## 🚢 Deployment

The application is designed to run on low-spec infrastructure:

### AWS EC2 Requirements
- **Instance**: t3.micro
- **OS**: Ubuntu 22.04 LTS
- **RAM**: 1GB + 2GB Swap
- **Storage**: 10GB minimum

## 🧪 Testing

```bash
# Run unit tests
docker-compose run backend pytest

# Run with coverage
docker-compose run backend pytest --cov=src
```

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
