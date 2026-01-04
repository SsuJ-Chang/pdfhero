#!/bin/bash
# PDF Hero - 自動部署腳本
# 由 Drone CI 觸發執行

set -e

echo "🚀 開始部署 PDF Hero..."

# 1. 進入專案目錄
cd ~/pdfhero

# 2. 拉取最新代碼
echo "📥 拉取最新代碼..."
git pull origin main

# 3. 重啟容器
echo "🔄 重啟 Docker 容器..."
docker-compose down
docker-compose up -d --build

# 4. 等待容器啟動
echo "⏳ 等待容器啟動..."
sleep 10

# 5. 檢查容器狀態
echo "✅ 檢查容器狀態..."
docker ps

echo "🎉 部署完成！"
