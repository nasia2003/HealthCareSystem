# 1. Build base image (chứa các thư viện chung)
Write-Host "Building base image..."
docker build -t python-base:latest -f Dockerfile.base .

# 2. Build và chạy docker-compose cho các service
Write-Host "Building and starting services..."
docker-compose up --build --force-recreate
