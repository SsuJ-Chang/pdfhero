# 主域名跳轉設定指南

## ⚠️ 重要：現在先別設定！

因為 `nslookup rj-tw.com` 失敗，表示 DNS 記錄還沒設定或還沒生效。

**建議：先暫緩此設定，等 AdSense 審核結果出來再說**

---

## 為什麼不急著設定？

1. **AdSense 審核**可能只需要網站有 AdSense 程式碼即可
2. 審核員可能直接測試 `pdfhero.rj-tw.com`，不一定會測 `rj-tw.com`
3. 設定這個需要額外的 SSL 憑證和 DNS 配置

---

## 如果真的需要設定（未來）

### Step 1: 在 GoDaddy 加 DNS 記錄
```
類型: A
主機: @
指向: 您的 EC2 公網 IP
```

### Step 2: 確認 DNS 生效
```bash
nslookup rj-tw.com
# 應該要看到您的 EC2 IP
```

### Step 3: 緊急修復（如果 Nginx 已經壞了）
```bash
# SSH 到 EC2
sudo rm /etc/nginx/sites-enabled/rj-tw.com
sudo nginx -t
sudo systemctl reload nginx
```

### Step 4: 重新部署（DNS 生效後）
```bash
cd ~/pdfhero
git pull origin main
sudo cp nginx/rj-tw.com-redirect.conf /etc/nginx/sites-available/rj-tw.com
sudo ln -s /etc/nginx/sites-available/rj-tw.com /etc/nginx/sites-enabled/rj-tw.com
sudo nginx -t
sudo systemctl reload nginx
```

### Step 5: 申請 SSL
```bash
sudo certbot --nginx -d rj-tw.com
```

---

## 🎯 目前建議

**直接用 `pdfhero.rj-tw.com` 送審 AdSense 即可！**

如果審核被拒且 Google 要求主域名也要有內容，再回來做這個設定。
