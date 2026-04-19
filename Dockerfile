# 使用輕量 Python 3.11 基礎鏡像
FROM python:3.11-slim

# 設定工作目錄
WORKDIR /app

# 先複製 requirements，Docker 快取用
COPY requirements.txt .

# 安裝依賴
RUN pip install --no-cache-dir -r requirements.txt

# 複製專案檔案
COPY . .

# 建立非 root 使用者 (安全)
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# 暴露 8000 port
EXPOSE 8000

# 用 gunicorn 啟動生產環境
CMD ["gunicorn", "app.main:app", \
     "--workers", "4", \
     "--worker-class", "uvicorn.workers.UvicornWorker", \
     "--bind", "0.0.0.0:8000", \
     "--access-logfile", "-", \
     "--error-logfile", "-", \
     "--reload"]