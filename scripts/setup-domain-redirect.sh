#!/bin/bash
# 為主域名 rj-tw.com 設定跳轉到 pdfhero.rj-tw.com

set -e

echo "🔧 設定主域名跳轉..."

# 1. 確認 DNS 已設定
echo "⚠️  請先確認以下 DNS 記錄已設定："
echo "   A記錄: rj-tw.com → EC2 IP"
echo "   A記錄: www.rj-tw.com → EC2 IP"
echo ""
read -p "DNS 已設定完成？(y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    echo "請先設定 DNS 記錄再執行此腳本"
    exit 1
fi

# 2. 複製 Nginx 配置
echo "📝 複製 Nginx 跳轉配置..."
sudo cp nginx/rj-tw.com-redirect.conf /etc/nginx/sites-available/rj-tw.com

# 3. 啟用配置
echo "🔗 啟用配置..."
sudo ln -sf /etc/nginx/sites-available/rj-tw.com /etc/nginx/sites-enabled/rj-tw.com

# 4. 測試配置
echo "🧪 測試 Nginx 配置..."
sudo nginx -t

# 5. 重啟 Nginx
echo "🔄 重啟 Nginx..."
sudo systemctl reload nginx

echo "✅ HTTP 跳轉已設定完成！"
echo ""
echo "📋 下一步：為主域名申請 SSL 憑證"
echo "執行以下指令："
echo "sudo certbot --nginx -d rj-tw.com -d www.rj-tw.com"
echo ""
echo "💡 SSL 設定完成後，HTTPS 跳轉也會自動生效"
