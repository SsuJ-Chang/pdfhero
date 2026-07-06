#!/bin/bash
# ARCHIVED DEPLOYMENT NOTE: The previous AWS EC2 deployment was terminated. This file is kept for historical reference only.

# PDF Hero - SSL 憑證安裝腳本

set -e

echo "🔐 開始安裝 SSL 憑證..."

# 1. 檢查參數
if [ -z "$1" ] || [ -z "$2" ]; then
    echo "❌ 請提供域名和 Email"
    echo "用法: ./setup-ssl.sh your-domain.com your-email@example.com"
    exit 1
fi

DOMAIN=$1
EMAIL=$2

# 2. 安裝 Certbot
echo "📦 安裝 Certbot..."
sudo apt-get update
sudo apt-get install -y certbot python3-certbot-nginx

# 3. 申請憑證
echo "📜 申請 SSL 憑證..."
sudo certbot --nginx \
    -d $DOMAIN \
    --non-interactive \
    --agree-tos \
    --email $EMAIL \
    --redirect

# 4. 測試自動更新
echo "🔄 設定自動更新..."
sudo certbot renew --dry-run

echo "✅ SSL 憑證安裝完成！"
echo ""
echo "🎉 您的網站現在已啟用 HTTPS！"
echo "🌐 訪問: https://$DOMAIN"
