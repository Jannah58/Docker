🚀 Getting Started
Once everything is set up, follow these steps to launch the application:

1️⃣ Start the Application
Run the following command from the root directory:

👉 `cd Zinad && docker-compose up`

This will build and start all containers:
- **Frontend** (React) - Port 3000
- **Backend** (Flask) - Port 5000  
- **AI Service** (FastAPI + LangChain + Ollama) - Port 8000
- **Ollama** (LLM Runtime) - Port 11434

2️⃣ Access the Website
Open your browser and navigate to:

👉 http://localhost:3000

If everything is running correctly, you’ll see your React app live!



2️⃣ Setup AI Models
After services are running, download AI models:

👉 `./Zinad/ai-service/setup_models.sh`

3️⃣ Access the Services
Open your browser and navigate to:

- **Main App**: http://localhost:3000
- **AI Service API**: http://localhost:8000
- **AI Service Docs**: http://localhost:8000/docs

## 🤖 AI Service Features

The new AI service provides:
- **Chat API** powered by LangChain and Ollama
- **Multiple LLM support** (llama2, codellama, mistral, etc.)
- **RESTful API** with automatic documentation
- **Local inference** - no external API keys needed
- **Docker containerized** for easy deployment

### Quick AI API Test:
```bash
curl -X POST "http://localhost:8000/chat" \
     -H "Content-Type: application/json" \
     -d '{"message": "Hello! Explain Docker in simple terms."}'
```
