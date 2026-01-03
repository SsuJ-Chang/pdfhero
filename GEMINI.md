# 專案名稱：PDF Hero (PDF 救星)

## 1. 專案願景
建立一個「永久免費」、「極簡好用」且「資源節約」的線上轉檔工具。
專注於 Desktop 使用者體驗，透過乾淨的介面與 Google 自動廣告 (Auto Ads) 維持營運。

## 2. 學習目標 (Learning Objectives)
作為開發者，本專案旨在練習：
* **後端架構：** Python FastAPI, Clean Architecture (SOLID), MVC 模式。
* **前端整合：** React, TypeScript, Tailwind CSS, API 串接。
* **DevOps：** Docker (低資源優化), AWS EC2 部署, Nginx 反向代理, GitHub Actions (CI/CD)。
* **系統設計：** 在無資料庫且記憶體有限 (Low-Spec) 的環境下處理併發任務 (Concurrency Control)。

## 3. 技術堆疊 (Tech Stack)
* **Backend:** Python 3.11+ (Slim), FastAPI, Poetry, LibreOffice (Headless), Pillow.
* **Frontend:** React (Vite), TypeScript, Tailwind CSS.
* **Infra:** Docker & Docker Compose, AWS EC2 (t2/t3.micro), Nginx, Sentry (Logs/Error Tracking).

## 4. 關鍵架構決策 (Critical Constraints)
1.  **不使用資料庫：** 採用暫存檔 (Temporary File) 策略，閱後即焚，節省成本與維護心力。
2.  **低資源生存模式 (Survival Mode)：**
    * AWS EC2 需設定 2GB Swap File。
    * Docker 映像檔需極小化 (使用 `--no-install-recommends`)。
    * 應用層使用 `asyncio.Semaphore` 限制同時只能有 1-2 個轉檔程序，避免 OOM (Out Of Memory)。
3.  **電腦版限定 (Desktop First)：** 前端需阻擋手機/平板裝置，顯示提示訊息。

## 5. 開發階段規劃 (Roadmap)

### Phase 1: 骨架搭建 (Skeleton)
* 建立 Clean Architecture 目錄結構。
* 設定 Docker 環境 (前後端連通)。
* 初始化 Poetry 與 Vite 專案。

### Phase 2: 後端核心 (Core Logic)
* 定義 Entity (File) 與 Interface (FileConverter)。
* 實作 Use Case (ConvertFileUseCase) 與單元測試 (Pytest)。
* 實作 Mock Converter 確認流程。

### Phase 3: 轉檔實作 (Implementation)
* 實作 `PillowConverter` (圖片轉 PDF)。
* 實作 `LibreOfficeConverter` (Word 轉 PDF)。
* 優化 Dockerfile 安裝依賴。
* 加入 Semaphore 併發控制。

### Phase 4: 前端與介面 (UI/UX)
* 實作「拖曳上傳」功能。
* 實作「檔案上傳」功能。
* 實作「下載」功能。
* 實作「錯誤處理」功能。
* 實作「預設深色模式」與「主題切換開關」。

### Phase 5: 部署與監控 (Deployment)
* AWS 環境準備 (Swap 設定)。
* 設定 Nginx 與 HTTPS (Certbot)。
* 設定 Sentry 監控。
* 設定 GitHub Actions 自動部署。

## 6. 指令備忘 (Cheat Sheet)
* 啟動本地開發：`docker-compose up --build`
* 執行測試：`docker-compose run backend pytest`
* 清理 Docker：`docker system prune -a`

---
