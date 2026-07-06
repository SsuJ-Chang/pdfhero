# PDF Hero

> A local-first, privacy-minded PDF conversion tool for images and Word documents.

[繁體中文](./README.zh-TW.md) | English

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Status](https://img.shields.io/badge/hosting-offline-lightgrey)](#project-status)

## Project Status

PDF Hero is no longer hosted publicly.

The previous AWS EC2 instance and `pdfhero.rj-tw.com` deployment have been terminated. This repository is kept as a portfolio and local development project. You can still run the application locally with Docker Compose.

## Features

- **Fast conversion** - Convert images and Word documents to PDF.
- **Privacy-minded architecture** - No database; uploaded files are processed temporarily.
- **No registration flow** - The app is designed for direct use.
- **Modern UI** - React-based interface with responsive layout and dark-mode styling.
- **Local Docker setup** - Frontend and backend can run together with Docker Compose.

## Supported Conversions

| From | To | Status |
| --- | --- | --- |
| Images (PNG, JPG, JPEG, WebP) | PDF | Supported |
| Word Documents (DOC, DOCX) | PDF | Supported |
| Excel Spreadsheets | PDF | Planned |
| PowerPoint Presentations | PDF | Planned |

## Tech Stack

### Frontend

- **React** with TypeScript
- **Vite** for development and builds
- **Tailwind CSS** for styling

### Backend

- **FastAPI** (Python 3.11+)
- **LibreOffice Headless** for document conversion
- **Pillow** for image processing

### Local Infrastructure

- **Docker**
- **Docker Compose**

## Project Structure

```text
pdfhero/
├── backend/                # FastAPI backend
│   ├── src/
│   │   ├── domain/         # Business entities and interfaces
│   │   ├── use_cases/      # Application logic
│   │   ├── infrastructure/ # Converter implementations
│   │   └── adapters/       # API controllers
│   └── tests/              # Unit tests
├── frontend/               # React frontend
│   ├── src/
│   │   ├── components/     # React components
│   │   ├── api/            # API client
│   │   └── context/        # React context providers
│   └── public/             # Static assets
├── nginx/                  # Archived Nginx configuration
└── scripts/                # Archived deployment helper scripts
```

## Design Notes

### Privacy-Minded Architecture

- **No database**: Conversion requests do not persist user accounts or file records.
- **Temporary processing**: Files are only needed during the conversion request.
- **Simple runtime boundary**: The frontend calls the FastAPI backend through the `/api` route.

### Resource Optimization

- **Small deployment target**: The original deployment was tuned for a low-spec EC2 instance.
- **Concurrency control**: Backend conversion work is guarded by a semaphore.
- **Containerized services**: Docker keeps frontend and backend setup reproducible.

## Local Development

Start the full stack:

```bash
docker-compose up --build
```

Local URLs:

| Service | URL |
| --- | --- |
| Frontend | `http://localhost:5173` |
| Backend | `http://localhost:8000` |

Stop the stack:

```bash
docker-compose down
```

## Testing

```bash
# Run unit tests
docker-compose run backend pytest

# Run unit tests with coverage
docker-compose run backend pytest --cov=src
```

## Archived Deployment Notes

PDF Hero previously used the following production setup:

- AWS EC2
- Docker Compose
- Nginx reverse proxy
- Let's Encrypt SSL/TLS
- GitHub Actions SSH deployment
- Domain: `pdfhero.rj-tw.com`

That deployment path is no longer active. These files are kept only as historical reference:

| File | Purpose |
| --- | --- |
| `.github/workflows/deploy.yml` | Archived EC2 deployment workflow |
| `scripts/deploy.sh` | Old server-side deployment script |
| `scripts/setup-nginx.sh` | Old Nginx setup helper |
| `scripts/setup-ssl.sh` | Old Let's Encrypt setup helper |
| `scripts/setup-domain-redirect.sh` | Old domain redirect helper |
| `nginx/pdfhero.conf` | Old Nginx reverse proxy config |

Provision a new server and domain before reusing any archived deployment files.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Contact

- GitHub: [@SsuJ-Chang](https://github.com/SsuJ-Chang)
