#!/bin/bash

echo "🔧 Testing Zinad Frontend Build Process..."
echo "========================================"

# Navigate to frontend directory
cd frontend

echo "📦 Installing dependencies..."
npm install

if [ $? -eq 0 ]; then
    echo "✅ Dependencies installed successfully"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi

echo "🏗️  Building React app..."
npm run build

if [ $? -eq 0 ]; then
    echo "✅ Build completed successfully"
    echo "📁 Build output:"
    ls -la build/
else
    echo "❌ Build failed"
    exit 1
fi

echo ""
echo "🐳 Testing Docker build..."
cd ..
docker compose build --no-cache frontend

if [ $? -eq 0 ]; then
    echo "✅ Docker build successful"
else
    echo "❌ Docker build failed"
    exit 1
fi

echo ""
echo "🚀 All tests passed! Your frontend should now work properly."
echo "To start the application, run: docker compose up"