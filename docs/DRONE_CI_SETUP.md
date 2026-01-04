# Drone CI 設定指南

## 📋 前置準備

在開始之前，請確認您有：
- ✅ GitHub Repository 已建立且可訪問
- ✅ AWS EC2 已運行且 Docker 容器正常
- ✅ EC2 的 SSH 私鑰檔案（.pem）

---

## 🚀 Step 1: 連接 Drone Cloud

### 1.1 註冊/登入 Drone Cloud
1. 前往 [https://cloud.drone.io/](https://cloud.drone.io/)
2. 點擊「Continue with GitHub」
3. 授權 Drone 訪問您的 GitHub 帳號

### 1.2 同步 Repository
1. 登入後，點擊右上角的「SYNC」按鈕
2. 等待 Repository 列表更新
3. 找到 `pdfhero` Repository

### 1.3 啟用 Repository
1. 點擊 `pdfhero` 右側的「ACTIVATE」按鈕
2. Repository 狀態會變成「Active」

---

## 🔐 Step 2: 設定 Secrets

點擊 Repository → 左側選單「Settings」→ 「Secrets」

### 2.1 新增 `ssh_host`
- **Name**: `ssh_host`
- **Value**: 您的 EC2 公網 IP（例如：`34.237.72.62`）
- 勾選「Allow Pull Requests」：❌ 不勾選

### 2.2 新增 `ssh_user`
- **Name**: `ssh_user`
- **Value**: `ubuntu`
- 勾選「Allow Pull Requests」：❌ 不勾選

### 2.3 新增 `ssh_key`（最重要）
- **Name**: `ssh_key`
- **Value**: 您的 EC2 SSH 私鑰內容

**如何取得私鑰內容：**

#### Windows (PowerShell):
```powershell
# 假設您的私鑰檔案是 my-key.pem
Get-Content -Path C:\path\to\my-key.pem -Raw | Set-Clipboard
# 私鑰已複製到剪貼簿，直接貼到 Drone Secret 的 Value 欄位
```

#### Mac/Linux:
```bash
cat ~/path/to/my-key.pem | pbcopy  # Mac
cat ~/path/to/my-key.pem | xclip   # Linux
```

**注意**：
- 私鑰格式必須包含 `-----BEGIN RSA PRIVATE KEY-----` 和 `-----END RSA PRIVATE KEY-----`
- 整個內容（含開頭結尾）都要貼上
- 勾選「Allow Pull Requests」：❌ **絕對不要勾選**（安全考量）

---

## ✅ Step 3: 測試部署

### 3.1 推送代碼觸發 Pipeline
```bash
# 在本地專案目錄
git add .
git commit -m "Test Drone CI deployment"
git push origin main
```

### 3.2 查看 Pipeline 執行狀態
1. 回到 Drone Cloud → 點擊 `pdfhero`
2. 應該會看到新的 Build 出現
3. 點擊 Build → 查看執行日誌

**成功的樣子**：
```
✓ deploy-to-ec2
  🚀 開始部署 PDF Hero...
  📥 拉取最新代碼...
  🔄 重啟 Docker 容器...
  ✅ 檢查容器狀態...
  🎉 部署完成！
```

### 3.3 驗證網站更新
訪問 `https://pdfhero.rj-tw.com`，確認變更已生效。

---

## 🐛 常見問題排查

### Q1: Build 失敗，顯示「Permission denied (publickey)」
**原因**：SSH 私鑰設定錯誤

**解決**：
1. 確認私鑰內容完整（包含開頭結尾）
2. 確認 EC2 Security Group 允許 SSH 連線
3. 確認 `ssh_user` 是 `ubuntu` 而非 `ec2-user`

### Q2: Build 成功但網站沒更新
**原因**：容器重啟失敗或代碼未拉取

**排查**：
1. SSH 登入 EC2
2. 執行 `cd ~/pdfhero && git log` 查看最新 commit
3. 執行 `docker ps` 查看容器狀態
4. 執行 `docker-compose logs --tail=50` 查看日誌

### Q3: 想要停用自動部署
**解決**：
Drone Cloud → Repository Settings → 關閉「Active」

---

## 🎯 成功後的工作流程

從現在開始，您的開發流程變成：

```
1. 本地修改代碼
2. git commit -m "..."
3. git push origin main
4. ☕ 喝杯咖啡（Drone 自動部署中）
5. 🎉 網站自動更新完成！
```

**不再需要手動 SSH 到 EC2！**

---

## 📊 監控建議

建議定期檢查：
- Drone Build 歷史記錄（確認部署成功率）
- EC2 系統資源（`htop`, `df -h`）
- Docker 容器日誌（`docker-compose logs`）
