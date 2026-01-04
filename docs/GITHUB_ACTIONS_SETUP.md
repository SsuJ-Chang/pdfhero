# GitHub Actions CI/CD 設定指南

## 🎯 為什麼選擇 GitHub Actions？

- ✅ **完全免費**（公開 Repo 無限制，私有 Repo 每月 2000 分鐘）
- ✅ **無需額外註冊**（直接使用 GitHub 帳號）
- ✅ **整合在 GitHub**（代碼與 CI/CD 同一平台）
- ✅ **社群龐大**（豐富的 Actions Marketplace）

---

## 🚀 設定步驟（5 分鐘完成）

### Step 1: 設定 GitHub Secrets

1. 前往 GitHub Repository：`https://github.com/您的帳號/pdfhero`
2. 點擊 **Settings**（設定）
3. 左側選單選擇 **Secrets and variables** → **Actions**
4. 點擊 **New repository secret**

依序新增以下 3 個 Secrets：

#### Secret 1: EC2_HOST
- **Name**: `EC2_HOST`
- **Secret**: 您的 EC2 公網 IP（例如：`34.237.72.62`）

#### Secret 2: EC2_USER
- **Name**: `EC2_USER`  
- **Secret**: `ubuntu`

#### Secret 3: EC2_SSH_KEY
- **Name**: `EC2_SSH_KEY`
- **Secret**: 您的 EC2 SSH 私鑰內容

**如何取得私鑰內容：**

##### Windows (PowerShell):
```powershell
# 假設您的私鑰檔案是 my-key.pem
Get-Content -Path C:\path\to\my-key.pem -Raw
# 複製輸出的全部內容
```

##### Mac/Linux:
```bash
cat ~/path/to/my-key.pem
# 複製輸出的全部內容（含 -----BEGIN 和 -----END）
```

**注意**：
- 必須包含完整的私鑰（含開頭 `-----BEGIN RSA PRIVATE KEY-----` 和結尾 `-----END RSA PRIVATE KEY-----`）
- 所有換行都要保留

---

### Step 2: 推送代碼觸發 Workflow

設定完 Secrets 後，任何對 `main` 分支的推送都會自動觸發部署：

```bash
git add .
git commit -m "Setup GitHub Actions CI/CD"
git push origin main
```

---

### Step 3: 查看部署狀態

1. 前往 GitHub Repository
2. 點擊頂部的 **Actions** 標籤
3. 看到您剛剛的 commit 正在執行
4. 點擊進去查看詳細日誌

**成功的樣子**：
- ✅ 綠色勾勾
- 日誌最後顯示「✅ 部署完成！」

---

## 🧪 測試自動部署

### 測試方法
修改任何文件，例如在 `README.md` 加一行文字：

```bash
echo "# PDF Hero - 測試自動部署" >> README.md
git add README.md
git commit -m "Test: GitHub Actions auto-deploy"
git push origin main
```

然後：
1. 到 GitHub Actions 查看執行狀態
2. 等待完成（約 30-60 秒）
3. SSH 到 EC2 檢查：`cd ~/pdfhero && git log`

---

## 🎯 成功後的工作流程

```
1. 本地修改代碼
2. git commit -m "..."
3. git push origin main
4. ☕ GitHub Actions 自動部署（30-60 秒）
5. 🎉 網站自動更新！
```

**完全不需要手動 SSH 到 EC2！**

---

## 🐛 常見問題

### Q: Workflow 失敗，顯示「Permission denied」
**原因**：SSH 私鑰設定錯誤

**解決**：
1. 檢查 `EC2_SSH_KEY` Secret 是否包含完整私鑰
2. 確認沒有多餘的空格或換行
3. 確認 EC2 Security Group 允許 GitHub Actions 的 IP 連線（建議允許所有來源的 SSH，或使用 GitHub Actions 的 IP 範圍）

### Q: 怎麼查看部署日誌？
**解答**：
GitHub → Your Repo → Actions → 點擊任一 Workflow → 點擊 "Deploy to EC2" 步驟

### Q: 想要暫停自動部署怎麼辦？
**解答**：
刪除或重命名 `.github/workflows/deploy.yml` 文件即可

---

## 📊 監控建議

- **GitHub Actions 頁面**：定期檢查部署成功率
- **EC2 系統資源**：`htop`, `df -h`
- **Docker 容器狀態**：`docker ps`, `docker-compose logs`

---

## 🎁 額外功能（進階）

GitHub Actions 還可以做：
- 自動執行測試（`npm test`, `pytest`）
- 自動建置 Docker 映像
- 多環境部署（dev/staging/production）
- 定時任務（cron）

**現在您已經有完整的 CI/CD 了！** 🚀
