#!/bin/bash
# ARCHIVED DEPLOYMENT NOTE: The previous AWS EC2 deployment was terminated. This file is kept for historical reference only.

# PDF Hero - Nginx 配置部署腳本

set -e

echo "🔧 開始配置 Nginx..."

# 1. 檢查是否有提供域名參數
if [ -z "$1" ]; then
    echo "❌ 請提供您的域名作為參數"
    echo "用法: ./setup-nginx.sh your-domain.com"
    exit 1
fi

DOMAIN=$1

# 2. 備份原始 Nginx 配置（如果存在）
if [ -f /etc/nginx/sites-available/pdfhero ]; then
    echo "📦 備份現有配置..."
    sudo cp /etc/nginx/sites-available/pdfhero /etc/nginx/sites-available/pdfhero.backup.$(date +%Y%m%d_%H%M%S)
fi

# 3. 複製配置檔並替換域名
echo "📝 更新 Nginx 配置..."
sed "s/your-domain.com/$DOMAIN/g" nginx/pdfhero.conf | sudo tee /etc/nginx/sites-available/pdfhero > /dev/null

# 4. 建立 symbolic link
echo "🔗 啟用站點配置..."
sudo ln -sf /etc/nginx/sites-available/pdfhero /etc/nginx/sites-enabled/pdfhero

# 5. 移除預設站點（避免衝突）
sudo rm -f /etc/nginx/sites-enabled/default

# 6. 測試配置
echo "🧪 測試 Nginx 配置..."
sudo nginx -t

# 7. 重啟 Nginx
echo "🔄 重啟 Nginx..."
sudo systemctl restart nginx
sudo systemctl enable nginx

echo "✅ Nginx 配置完成！"
echo ""
echo "📋 下一步："
echo "1. 確認域名 DNS 已指向此伺服器"
echo "2. 執行: bash scripts/setup-ssl.sh $DOMAIN your-email@example.com"
echo "3. Certbot 會自動配置 HTTPS"
