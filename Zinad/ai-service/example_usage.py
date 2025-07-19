#!/usr/bin/env python3
"""
Example usage script for the AI Service API
Demonstrates how to interact with the LangChain + Ollama powered service
"""

import requests
import json
import time

# Configuration
AI_SERVICE_URL = "http://localhost:8000"

def check_health():
    """Check if the AI service is healthy"""
    try:
        response = requests.get(f"{AI_SERVICE_URL}/")
        return response.json()
    except Exception as e:
        print(f"Health check failed: {e}")
        return None

def get_available_models():
    """Get list of available models"""
    try:
        response = requests.get(f"{AI_SERVICE_URL}/models")
        return response.json()
    except Exception as e:
        print(f"Failed to get models: {e}")
        return None

def chat_with_ai(message, model="llama2", temperature=0.7):
    """Send a chat message to the AI service"""
    try:
        payload = {
            "message": message,
            "model": model,
            "temperature": temperature
        }
        
        response = requests.post(
            f"{AI_SERVICE_URL}/chat",
            json=payload,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Request failed with status {response.status_code}")
            print(f"Error: {response.text}")
            return None
            
    except Exception as e:
        print(f"Chat request failed: {e}")
        return None

def main():
    """Main demonstration function"""
    print("🤖 AI Service Example Usage")
    print("=" * 50)
    
    # Check service health
    print("1. Checking service health...")
    health = check_health()
    if health:
        print(f"   ✅ Service status: {health['status']}")
        print(f"   🔗 Ollama connected: {health['ollama_connected']}")
    else:
        print("   ❌ Service is not available")
        return
    
    print()
    
    # Get available models
    print("2. Getting available models...")
    models = get_available_models()
    if models:
        print(f"   📋 Available models: {', '.join(models['available_models'])}")
        print(f"   🎯 Default model: {models['default_model']}")
    
    print()
    
    # Example chat interactions
    print("3. Example chat interactions...")
    
    examples = [
        {
            "message": "Hello! Can you explain what LangChain is?",
            "model": "llama2"
        },
        {
            "message": "Write a simple Python function to calculate factorial",
            "model": "llama2",
            "temperature": 0.3  # Lower temperature for code generation
        },
        {
            "message": "What are the benefits of using Docker for AI applications?",
            "model": "llama2",
            "temperature": 0.8  # Higher temperature for creative responses
        }
    ]
    
    for i, example in enumerate(examples, 1):
        print(f"\n   Example {i}:")
        print(f"   💬 User: {example['message']}")
        print(f"   ⚙️  Model: {example['model']}, Temperature: {example.get('temperature', 0.7)}")
        
        result = chat_with_ai(**example)
        if result:
            print(f"   🤖 AI: {result['response'][:200]}{'...' if len(result['response']) > 200 else ''}")
            print(f"   📊 Status: {result['status']}")
        else:
            print("   ❌ Failed to get response")
        
        # Add small delay between requests
        time.sleep(1)

if __name__ == "__main__":
    main()