set -e  # 任何指令失敗就停

echo "開始初始化 fall-detection-server..."

# 建 data 資料夾
mkdir -p data
echo "data/ 資料夾已建立"

# 檢查 docker-compose.yml
if [ ! -f "docker-compose.yml" ]; then
    echo "docker-compose.yml 不存在！"
    exit 1
fi

# 建鏡像
echo "建置 Docker 鏡像..."
docker compose build --no-cache

echo "=========初始化完成========="
echo ""
echo "=========使用方式==========="
echo "  ./start.sh     # 啟動服務"
echo "  ./down.sh   # 停止服務"
echo "  ./logs.sh   # 看 log"