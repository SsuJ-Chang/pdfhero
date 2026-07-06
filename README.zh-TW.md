# PDF Hero

> 本機優先、重視隱私的 PDF 轉換工具，可將圖片與 Word 文件轉成 PDF。

繁體中文 | [English](./README.md)

[![授權](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![狀態](https://img.shields.io/badge/hosting-offline-lightgrey)](#專案狀態)

## 專案狀態

PDF Hero 目前已經沒有公開部署。

原本部署在 AWS EC2 上的服務，以及 `pdfhero.rj-tw.com` 網域對應的線上版本，已經停止使用。這個 repo 目前保留作為作品集與本機開發專案，仍然可以用 Docker Compose 在本機跑起來。

## 功能

- **快速轉換**：將圖片與 Word 文件轉成 PDF。
- **重視隱私的架構**：沒有資料庫；上傳檔案只在轉換流程中暫時處理。
- **不需要註冊流程**：設計上可直接使用。
- **現代化介面**：React 介面，支援響應式版面與深色系樣式。
- **本機 Docker 環境**：前端與後端可以透過 Docker Compose 一起啟動。

## 支援轉換格式

| 來源格式 | 目標格式 | 狀態 |
| --- | --- | --- |
| 圖片（PNG、JPG、JPEG、WebP） | PDF | 已支援 |
| Word 文件（DOC、DOCX） | PDF | 已支援 |
| Excel 試算表 | PDF | 規畫中 |
| PowerPoint 簡報 | PDF | 規畫中 |

## 技術棧

### 前端

- **React** 搭配 TypeScript
- **Vite** 作為開發與建置工具
- **Tailwind CSS** 負責樣式

### 後端

- **FastAPI**（Python 3.11+）
- **LibreOffice Headless** 處理文件轉換
- **Pillow** 處理圖片轉換

### 本機基礎建設

- **Docker**
- **Docker Compose**

## 專案結構

```text
pdfhero/
├── backend/                # FastAPI 後端
│   ├── src/
│   │   ├── domain/         # 業務實體與介面
│   │   ├── use_cases/      # 應用邏輯
│   │   ├── infrastructure/ # 轉換器實作
│   │   └── adapters/       # API 控制器
│   └── tests/              # 單元測試
├── frontend/               # React 前端
│   ├── src/
│   │   ├── components/     # React 元件
│   │   ├── api/            # API client
│   │   └── context/        # React context providers
│   └── public/             # 靜態資源
├── nginx/                  # 已封存的 Nginx 設定
└── scripts/                # 已封存的部署輔助腳本
```

## 設計筆記

### 重視隱私的架構

- **沒有資料庫**：轉換請求不會保存使用者帳號或檔案紀錄。
- **暫時處理檔案**：檔案只在轉換請求期間使用。
- **簡單的執行邊界**：前端透過 `/api` 路徑呼叫 FastAPI 後端。

### 資源使用最佳化

- **低規格部署目標**：原本的部署曾經針對低規格 EC2 instance 調整。
- **併發控制**：後端轉換工作有 semaphore 限制。
- **容器化服務**：Docker 讓前後端環境比較容易重現。

## 本機開發

啟動完整服務：

```bash
docker-compose up --build
```

本機網址：

| 服務 | URL |
| --- | --- |
| 前端 | `http://localhost:5173` |
| 後端 | `http://localhost:8000` |

停止服務：

```bash
docker-compose down
```

## 測試

```bash
# 執行單元測試
docker-compose run backend pytest

# 執行測試並產生 coverage
docker-compose run backend pytest --cov=src
```

## 已封存的部署紀錄

PDF Hero 以前使用過以下正式環境：

- AWS EC2
- Docker Compose
- Nginx reverse proxy
- Let's Encrypt SSL/TLS
- GitHub Actions SSH 部署
- 網域：`pdfhero.rj-tw.com`

這條部署路徑目前已經停用。以下檔案只保留作為歷史參考：

| 檔案 | 用途 |
| --- | --- |
| `.github/workflows/deploy.yml` | 已封存的 EC2 部署 workflow |
| `scripts/deploy.sh` | 舊的伺服器端部署腳本 |
| `scripts/setup-nginx.sh` | 舊的 Nginx 設定輔助腳本 |
| `scripts/setup-ssl.sh` | 舊的 Let's Encrypt 設定輔助腳本 |
| `scripts/setup-domain-redirect.sh` | 舊的網域轉址輔助腳本 |
| `nginx/pdfhero.conf` | 舊的 Nginx reverse proxy 設定 |

如果未來要重新部署，需要先準備新的伺服器與網域，再評估是否沿用這些封存檔案。

## 授權

本專案使用 MIT License。詳細內容請見 [LICENSE](LICENSE)。

## 聯絡

- GitHub：[@SsuJ-Chang](https://github.com/SsuJ-Chang)
