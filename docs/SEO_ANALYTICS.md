# SEO & Analytics 整合指南

## 📊 Google Analytics 4 (GA4) 設定步驟

### 1. 建立 GA4 帳戶
1. 前往 [Google Analytics](https://analytics.google.com/)
2. 點擊「開始測量」→ 建立帳戶
3. 設定資源名稱：`PDF Hero`
4. 選擇報表時區：`台灣` 或您所在地區
5. 選擇產業類別：`工具與公用程式`

### 2. 建立資料串流
1. 選擇平台：`網站`
2. 輸入網站網址：`https://pdfhero.rj-tw.com`
3. 串流名稱：`PDF Hero Production`
4. 點擊「建立串流」

### 3. 取得測量 ID
- 複製測量 ID（格式：`G-XXXXXXXXXX`）
- 在 `frontend/index.html` 中找到這行：
  ```html
  <!-- TODO: Replace GA_MEASUREMENT_ID with your actual Google Analytics 4 Measurement ID -->
  ```
- 將所有 `GA_MEASUREMENT_ID` 替換成您的測量 ID
- 移除 `<!--` 和 `-->` HTML 註解標籤以啟用追蹤

### 4. 部署並驗證
```bash
git add frontend/index.html
git commit -m "Enable GA4 tracking"
git push origin main

# 在 EC2 上
cd ~/pdfhero
git pull origin main
docker-compose restart frontend
```

---

## 💰 Google AdSense 設定步驟

### ⚠️ 重要提醒
Google AdSense 需要網站符合以下條件：
- ✅ 網站已正式上線且可正常訪問 (HTTPS)
- ✅ 有原創且有價值的內容
- ✅ 符合 AdSense 政策
- ⏳ 建議運行 2-4 週後再申請

### 申請步驟
1. 前往 [Google AdSense](https://www.google.com/adsense/)
2. 點擊「開始使用」
3. 輸入網站網址與 Email
4. 將提供的驗證碼添加到 `index.html` 的 `<head>` 中
5. 等待審核（通常需要 1-2 週）

---

## 🔍 SEO 優化建議

### 已完成
- ✅ Meta 標籤（title, description, keywords）
- ✅ Open Graph 標籤（社群媒體分享）
- ✅ robots.txt（允許爬蟲）
- ✅ sitemap.xml（網站地圖）
- ✅ HTTPS 加密
- ✅ Canonical URL

### 後續可優化
- 📝 新增使用教學或 FAQ 頁面
- 🔗 建立外部連結（社群媒體、論壇）
- ⚡ 改善 Core Web Vitals（頁面載入速度）
- 📱 確保響應式設計完善

---

## 📈 監控與分析

### Google Analytics 重要指標
- **即時報表**：查看當前訪客
- **客層**：了解使用者來自哪裡
- **事件追蹤**：追蹤文件轉換次數（需額外設定）
- **轉換率**：分析使用者行為

### Google Search Console
建議同時設定 [Search Console](https://search.google.com/search-console/)：
1. 驗證網站擁有權
2. 提交 sitemap.xml
3. 監控搜尋表現與索引狀態
