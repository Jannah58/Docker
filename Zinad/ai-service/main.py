from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.schema import BaseOutputParser
import uvicorn
import logging
from typing import Optional

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="AI Service API",
    description="LangChain + Ollama powered AI service",
    version="1.0.0"
)

# Pydantic models for request/response
class ChatRequest(BaseModel):
    message: str
    model: Optional[str] = "llama2"  # Default to llama2
    temperature: Optional[float] = 0.7
    max_tokens: Optional[int] = 1000

class ChatResponse(BaseModel):
    response: str
    model_used: str
    status: str

class HealthResponse(BaseModel):
    status: str
    message: str
    ollama_connected: bool

# Initialize Ollama LLM
def get_llm(model_name: str = "llama2", temperature: float = 0.7):
    try:
        llm = Ollama(
            model=model_name,
            base_url="http://ollama:11434",  # Docker service name
            temperature=temperature
        )
        return llm
    except Exception as e:
        logger.error(f"Failed to initialize Ollama LLM: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to initialize LLM: {str(e)}")

# Custom output parser
class SimpleOutputParser(BaseOutputParser):
    def parse(self, text: str) -> str:
        return text.strip()

@app.get("/", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    try:
        # Test Ollama connection
        test_llm = get_llm()
        # Simple test to check if Ollama is responsive
        test_response = test_llm.invoke("Hello")
        ollama_connected = True
        logger.info("Ollama connection successful")
    except Exception as e:
        logger.error(f"Ollama connection failed: {e}")
        ollama_connected = False
    
    return HealthResponse(
        status="healthy",
        message="AI Service is running",
        ollama_connected=ollama_connected
    )

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Main chat endpoint that processes user requests using LangChain and Ollama"""
    try:
        logger.info(f"Received chat request: {request.message[:50]}...")
        
        # Initialize LLM with user-specified model and temperature
        llm = get_llm(model_name=request.model, temperature=request.temperature)
        
        # Create a prompt template
        prompt_template = PromptTemplate(
            input_variables=["user_input"],
            template="""You are a helpful AI assistant. Please provide a clear, accurate, and helpful response to the following question or request:

User: {user_input}
}"""
        )
        
        # Create LLMChain
        chain = LLMChain(
            llm=llm,
            prompt=prompt_template,
            output_parser=SimpleOutputParser()
        )
        
        # Generate response
        response = chain.invoke({"user_input": request.message})
        
        logger.info(f"Generated response for user request")
        
        return ChatResponse(
            response=response["text"] if isinstance(response, dict) else str(response),
            model_used=request.model,
            status="success"
        )
        
    except Exception as e:
        logger.error(f"Error processing chat request: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to process request: {str(e)}")

@app.get("/models")
async def list_models():
    """List available models"""
    return {
        "available_models": [
            "llama2",
            "codellama",
            "mistral",
            "neural-chat",
            "starling-lm"
        ],
        "default_model": "llama2"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
