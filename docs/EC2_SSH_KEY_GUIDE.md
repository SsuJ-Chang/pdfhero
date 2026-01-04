# EC2 SSH 私鑰說明文件

## 🔑 EC2_SSH_KEY 是什麼？

`EC2_SSH_KEY` 就是您**連線到 AWS EC2 時使用的 SSH 私鑰檔案內容**。

---

## 📍 如何找到這個檔案？

### 當初建立 EC2 時
AWS 會要求您下載一個 `.pem` 檔案，例如：
- `my-ec2-key.pem`
- `pdfhero-key.pem`
- `aws-ubuntu-key.pem`

這個檔案**通常儲存在您的電腦上**：
- **Windows**: `C:\Users\您的用戶名\Downloads\` 或桌面
- **Mac/Linux**: `~/Downloads/` 或 `~/.ssh/`

---

## 📝 如何取得檔案內容？

### Windows (PowerShell)

```powershell
# 方法 1: 直接顯示內容
Get-Content C:\path\to\your-key.pem

# 方法 2: 複製到剪貼簿
Get-Content C:\path\to\your-key.pem -Raw | Set-Clipboard
```

### Mac/Linux (Terminal)

```bash
# 方法 1: 直接顯示內容
cat ~/path/to/your-key.pem

# 方法 2: 複製到剪貼簿 (Mac)
cat ~/path/to/your-key.pem | pbcopy
```

---

## ✅ 正確的私鑰格式

私鑰內容應該**長這樣**：

```
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
... (很多行) ...
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
-----END RSA PRIVATE KEY-----
```

**重點**：
- ✅ 必須包含開頭 `-----BEGIN RSA PRIVATE KEY-----`
- ✅ 必須包含結尾 `-----END RSA PRIVATE KEY-----`
- ✅ 中間有很多行亂碼（這是正常的）
- ✅ 所有換行都要保留

---

## 🎯 如何設定到 GitHub Secrets

1. 複製整個私鑰內容（含開頭結尾）
2. 前往 GitHub Repository → Settings → Secrets and variables → Actions
3. 點擊「New repository secret」
4. **Name**: `EC2_SSH_KEY`
5. **Secret**: 貼上剛剛複製的私鑰內容
6. 點擊「Add secret」

---

## ⚠️ 如果找不到私鑰檔案怎麼辦？

### 情況 1: 檔案遺失
您可能需要：
1. 在 AWS Console 建立新的 Key Pair
2. 關閉 EC2 實例
3. Detach 原本的 Root Volume
4. Attach 到新實例並修改 `authorized_keys`
5. 或者直接重建 EC2（如果資料不多）

### 情況 2: 用密碼登入而非私鑰
如果您是用密碼登入 EC2，那需要先設定 SSH Key-based 登入。

---

## 🔍 測試私鑰是否正確

在本地執行：
```bash
ssh -i /path/to/your-key.pem ubuntu@您的EC2_IP
```

如果能成功登入，代表私鑰正確！

---

## 💡 安全提醒

- ❌ **絕對不要** commit 私鑰到 Git Repository
- ❌ **絕對不要** 分享給他人
- ✅ 只儲存在 GitHub Secrets（已加密）
- ✅ 定期備份私鑰檔案
