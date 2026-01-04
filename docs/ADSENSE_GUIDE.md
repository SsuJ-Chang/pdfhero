# Google AdSense 申請與設定指南

## 📋 申請前確認清單

在申請 AdSense 前，請確認您的網站符合以下條件：

- ✅ **網站已上線**：https://pdfhero.rj-tw.com 可正常訪問
- ✅ **內容原創**：網站功能正常且有實際價值
- ✅ **符合政策**：無違反 AdSense 政策內容（色情、暴力、版權侵權等）
- ⏳ **有一定流量**（建議）：雖非必須，但有自然流量會提高通過率

---

## 🚀 申請步驟

### Step 1: 前往 AdSense 官網
👉 https://www.google.com/adsense/

### Step 2: 開始申請
1. 點擊「開始使用」
2. 使用您的 Google 帳號登入
3. 填寫網站資訊：
   - **網站 URL**：`https://pdfhero.rj-tw.com`
   - **Email**：用於接收重要通知
   - **國家/地區**：選擇您的所在地

### Step 3: 連結網站
Google 會提供一段驗證程式碼，格式如下：
```html
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1234567890123456"
        crossorigin="anonymous"></script>
```

**您的發布商 ID** 就是 `?client=` 後面的那串數字，例如：`ca-pub-1234567890123456`

### Step 4: 將程式碼加入網站
1. 複製您的發布商 ID（`ca-pub-XXXXXXXXXXXXXXXX`）
2. 打開 `frontend/index.html`
3. 找到第 58 行：`ca-pub-YOUR_ADSENSE_PUBLISHER_ID`
4. 替換成您的 ID
5. 刪除註解符號（第 57 行的 `<!--` 和第 60 行的 `-->`）

**修改前**：
```html
<!--
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-YOUR_ADSENSE_PUBLISHER_ID"
        crossorigin="anonymous"></script>
-->
```

**修改後**（假設您的 ID 是 ca-pub-1234567890123456）：
```html
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1234567890123456"
        crossorigin="anonymous"></script>
```

### Step 5: 部署到伺服器
```bash
git add frontend/index.html
git commit -m "Enable Google AdSense Auto Ads"
git push origin main

# 在 EC2 上
cd ~/pdfhero
git pull origin main
docker-compose restart frontend
```

### Step 6: 回到 AdSense 後台送出審核
1. 回到 AdSense 後台
2. 確認「已在網站上找到 AdSense 程式碼」打勾
3. 點擊「送出審核」

---

## ⏳ 審核時間

- **預期時間**：1-2 週（有時更快，有時更慢）
- **結果通知**：透過 Email 通知
- **審核期間**：網站不會顯示廣告

---

## ✅ 審核通過後

### 啟用 Auto Ads（自動廣告）

1. AdSense 後台 → 左側「廣告」→「依網站顯示」
2. 點擊您的網站（pdfhero.rj-tw.com）
3. 開啟「自動廣告」
4. 選擇廣告格式：
   - ✅ **錨定廣告**（頁面頂部/底部）
   - ✅ **穿插廣告**（內容之間）
   - ✅ **文字和展示廣告**
   - ⚠️ **重疊廣告**（可能影響用戶體驗，建議關閉）

5. 點擊「套用至網站」

**24-48 小時後**，廣告就會開始自動顯示在您的網站上！

---

## 💰 收益與付款

### 收益門檻
- **最低付款金額**：美金 $100
- **付款方式**：
  - 電匯（需提供銀行帳戶）
  - 支票（較慢）
  - Western Union（某些地區）

### 查看收益
- AdSense 後台 → 左側「報表」
- 可以看到：
  - 預估收益
  - 點擊次數
  - 曝光次數
  - CPC（每次點擊成本）

---

## ⚠️ 常見問題

### Q: 申請被拒絕了怎麼辦？
A: Google 會說明原因（如內容不足、違反政策等），改善後可以重新申請

### Q: 廣告太多影響用戶體驗？
A: 可以在 AdSense 後台調整「廣告載入」數量或關閉某些廣告格式

### Q: 多久才能賺到 $100？
A: 取決於流量，一般小型網站可能需要數個月到一年

### Q: 可以自己點擊廣告嗎？
A: **絕對不行！** 這會導致帳戶被永久停權

---

## 📊 優化建議

1. **增加流量**：SEO、社群分享、內容行銷
2. **提高點擊率**：廣告位置要自然，不要干擾用戶
3. **監控數據**：定期查看 AdSense 報表，優化廣告配置
4. **結合 GA4**：分析哪些頁面帶來更多廣告收益
