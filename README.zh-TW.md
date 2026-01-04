# PDF Hero (PDF 救星)

> **永久免費、隱私優先的 PDF 轉檔工具**

繁體中文 | [English](./README.md)

[![線上展示](https://img.shields.io/badge/demo-線上展示-success)](https://pdfhero.rj-tw.com)
[![授權](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## ✨ 特色功能

- 🚀 **極速轉換** - 秒級完成圖片與 Word 文件轉 PDF
- 🔒 **隱私至上** - 無資料庫，檔案轉換後立即刪除
- 💰 **永久免費** - 廣告支持，完全免費使用
- 🎨 **現代化介面** - 簡潔優雅，預設深色模式
- 📱 **桌面優化** - 專為桌面使用者設計，行動裝置友善提示
- 🌐 **免註冊** - 立即使用，無需登入

## 🎯 支援的轉換格式

| 來源格式 | 目標格式 | 狀態 |
|---------|---------|------|
| 圖片 (PNG, JPG, JPEG, WebP) | PDF | ✅ 已支援 |
| Word 文件 (DOC, DOCX) | PDF | ✅ 已支援 |
| Excel 試算表 | PDF | 🔜 即將推出 |
| PowerPoint 簡報 | PDF | 🔜 即將推出 |

## 🛠️ 技術堆疊

### 前端
- **React 18** with TypeScript
- **Vite** 極速開發工具
- **Tailwind CSS** 樣式框架

### 後端
- **FastAPI** (Python 3.11+)
- **LibreOffice Headless** 文件轉換引擎
- **Pillow** 圖片處理函式庫

### 基礎架構
- **Docker & Docker Compose** 容器化
- **AWS EC2** 雲端主機
- **Nginx** 反向代理
- **Let's Encrypt** SSL/TLS 憑證
- **GitHub Actions** CI/CD 自動化部署

## 🏗️ 專案結構

```
pdfhero/
├── backend/             # FastAPI 後端
│   ├── src/
│   │   ├── domain/     # 業務實體與介面
│   │   ├── use_cases/  # 應用邏輯
│   │   ├── infrastructure/ # 轉換器實作
│   │   └── adapters/   # API 控制器
│   └── tests/          # 單元測試
├── frontend/           # React 前端
│   ├── src/
│   │   ├── components/ # React 元件
│   │   ├── api/       # API 客戶端
│   │   └── contexts/  # React 上下文
│   └── public/        # 靜態資源
├── nginx/             # Nginx 配置
└── scripts/           # 部署腳本
```

## 🎨 設計理念

### 隱私優先架構
- **無資料庫**：所有轉換在記憶體中完成
- **自動清理**：暫存檔案下載後立即刪除
- **零追蹤**：不儲存用戶資料（分析除外）

### 資源優化
- **低記憶體設計**：1GB RAM + 2GB Swap 即可運行
- **併發控制**：使用 `asyncio.Semaphore` 避免記憶體溢位
- **精簡映像檔**：使用 slim 基礎映像減少資源佔用

### 桌面優先體驗
- **行動裝置阻擋**：友善提示行動用戶使用桌面版
- **拖放上傳**：直覺的檔案上傳體驗
- **深色模式**：護眼的預設主題

## 📊 分析與營利

- **Google Analytics 4**：自定義事件追蹤轉換行為
- **Google AdSense**：自動廣告營利
- **SEO 優化**：完整的 meta 標籤與網站地圖

## 🚢 部署

本應用專為低規格基礎設施設計：

### AWS EC2 需求
- **實例類型**：t3.micro
- **作業系統**：Ubuntu 22.04 LTS
- **記憶體**：1GB + 2GB Swap
- **儲存空間**：最少 10GB

### 自動化部署

每次推送到 `main` 分支會透過 GitHub Actions 自動部署：

```bash
git push origin main
# ☕ 等待約 60 秒
# ✅ 變更自動上線到 https://pdfhero.rj-tw.com
```

## 🧪 測試

```bash
# 執行單元測試
docker-compose run backend pytest

# 含覆蓋率報告
docker-compose run backend pytest --cov=src
```

## 📄 授權

本專案採用 MIT 授權 - 詳見 [LICENSE](LICENSE) 檔案

## 🙏 致謝

- 由 [RJ Chang](https://github.com/SsuJ-Chang) 用 ❤️ 打造
- 基於開源技術構建
- 特別感謝 FastAPI 與 React 社群

## 📧 聯絡方式

- 網站：[pdfhero.rj-tw.com](https://pdfhero.rj-tw.com)
- GitHub：[@SsuJ-Chang](https://github.com/SsuJ-Chang)

---

**⭐ 如果您覺得這個專案有用，請考慮給它一顆星星！**
