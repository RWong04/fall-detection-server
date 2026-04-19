set -e

echo "⬆️  啟動 fall-detection-server..."

# 啟動服務
docker-compose up -d --build

# 等待 3 秒
sleep 3

# 檢查狀態
echo ""
echo "=========服務狀態========="
docker-compose ps

echo ""
echo "=========服務已啟動=========="
