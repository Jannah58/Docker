#!/bin/bash

# Setup script for downloading Ollama models

echo "Setting up Ollama models for AI service..."

# Wait for Ollama service to be ready
echo "Waiting for Ollama service to start..."
sleep 10

# Download llama2 model (default)
echo "Downloading llama2 model..."
docker exec -it zinad-ollama-1 ollama pull llama2

# Download additional models (optional, uncomment as needed)
echo "Downloading additional models..."
# docker exec -it zinad-ollama-1 ollama pull codellama
# docker exec -it zinad-ollama-1 ollama pull mistral
# docker exec -it zinad-ollama-1 ollama pull neural-chat

echo "Model setup complete!"
echo ""
echo "Available endpoints:"
echo "- Health check: http://localhost:8000/"
echo "- Chat API: http://localhost:8000/chat"
echo "- Available models: http://localhost:8000/models"
echo "- API docs: http://localhost:8000/docs"