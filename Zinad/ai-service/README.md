# AI Service - LangChain + Ollama + FastAPI

This AI service provides a RESTful API powered by LangChain and Ollama, allowing you to interact with various Large Language Models (LLMs) through a simple HTTP interface.

## 🚀 Features

- **FastAPI** backend with automatic API documentation
- **LangChain** for advanced prompt engineering and chain operations
- **Ollama** for running LLMs locally without external API dependencies
- **Multiple model support** (llama2, codellama, mistral, etc.)
- **Configurable parameters** (temperature, max tokens)
- **Health checks** and monitoring
- **Docker containerized** for easy deployment

## 📋 API Endpoints

### Health Check
```
GET /
```
Returns service health status and Ollama connection status.

### Chat Endpoint
```
POST /chat
```
Send a message to the AI and get a response.

**Request Body:**
```json
{
    "message": "Your question or prompt here",
    "model": "llama2",           // Optional, default: "llama2"
    "temperature": 0.7,          // Optional, default: 0.7
    "max_tokens": 1000          // Optional, default: 1000
}
```

**Response:**
```json
{
    "response": "AI generated response",
    "model_used": "llama2",
    "status": "success"
}
```

### Available Models
```
GET /models
```
Returns list of available models and default model.

### API Documentation
```
GET /docs
```
Interactive Swagger UI documentation (available when service is running).

## 🛠️ Setup and Usage

### 1. Start the Services
From the project root directory:

```bash
cd Zinad
docker-compose up -d
```

This will start:
- **Ollama service** on port `11434`
- **AI service** on port `8000`
- Your existing **backend** and **frontend** services

### 2. Download Models
After the services are running, download the required models:

```bash
# Run the setup script
./ai-service/setup_models.sh

# Or manually download models
docker exec -it zinad-ollama-1 ollama pull llama2
docker exec -it zinad-ollama-1 ollama pull codellama  # Optional
```

### 3. Test the Service
```bash
# Check health
curl http://localhost:8000/

# Send a chat message
curl -X POST "http://localhost:8000/chat" \
     -H "Content-Type: application/json" \
     -d '{"message": "Hello! Tell me about Docker."}'

# Or run the example script
cd ai-service
python3 example_usage.py
```

## 🐳 Docker Configuration

The AI service includes these containers in `docker-compose.yml`:

```yaml
# Ollama service for running LLMs
ollama:
  image: ollama/ollama:latest
  ports:
    - "11434:11434"
  volumes:
    - ollama_data:/root/.ollama

# AI service using LangChain + FastAPI
ai-service:
  build: ./ai-service
  ports:
    - "8000:8000"
  depends_on:
    - ollama
```

## 📝 Example Usage

### Python Script
```python
import requests

# Chat with the AI
response = requests.post("http://localhost:8000/chat", json={
    "message": "Explain machine learning in simple terms",
    "model": "llama2",
    "temperature": 0.7
})

result = response.json()
print(result["response"])
```

### cURL
```bash
curl -X POST "http://localhost:8000/chat" \
     -H "Content-Type: application/json" \
     -d '{
       "message": "Write a Python function to reverse a string",
       "model": "llama2",
       "temperature": 0.3
     }'
```

### JavaScript/Fetch
```javascript
const response = await fetch('http://localhost:8000/chat', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        message: "What are the benefits of microservices?",
        model: "llama2",
        temperature: 0.8
    })
});

const result = await response.json();
console.log(result.response);
```

## 🔧 Configuration

### Environment Variables
- `OLLAMA_BASE_URL`: Base URL for Ollama service (default: `http://ollama:11434`)

### Available Models
- `llama2` (default) - General purpose model
- `codellama` - Specialized for code generation
- `mistral` - Alternative general purpose model
- `neural-chat` - Conversational model
- `starling-lm` - Advanced instruction following

To add more models, download them via Ollama:
```bash
docker exec -it zinad-ollama-1 ollama pull <model-name>
```

## 🚨 Troubleshooting

### Common Issues

1. **Ollama not responding**
   ```bash
   # Check if Ollama is running
   docker logs zinad-ollama-1
   
   # Restart Ollama service
   docker-compose restart ollama
   ```

2. **Model not found**
   ```bash
   # List downloaded models
   docker exec -it zinad-ollama-1 ollama list
   
   # Download missing model
   docker exec -it zinad-ollama-1 ollama pull llama2
   ```

3. **AI service startup issues**
   ```bash
   # Check service logs
   docker logs zinad-ai-service-1
   
   # Rebuild the service
   docker-compose build ai-service
   docker-compose up -d ai-service
   ```

### Performance Tips

1. **GPU Support**: Uncomment the GPU configuration in `docker-compose.yml` if you have NVIDIA GPU
2. **Model Size**: Use smaller models like `llama2:7b` for faster responses
3. **Temperature**: Lower values (0.1-0.3) for consistent outputs, higher (0.7-1.0) for creative responses

## 📊 Monitoring

- Health endpoint: `http://localhost:8000/`
- Logs: `docker logs zinad-ai-service-1`
- Ollama status: `docker exec -it zinad-ollama-1 ollama list`

## 🔗 Integration

This AI service can be easily integrated with your existing application:

1. **Frontend Integration**: Call the API from your React/Vue/Angular app
2. **Backend Integration**: Use it as a microservice from your Flask/Django backend
3. **Webhook Support**: Easy to add webhook endpoints for external integrations

## 📄 License

This AI service is part of your project and follows your project's licensing terms.