import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

print("="*70)
print("🔍 AZURE OPENAI CONNECTION TEST")
print("="*70)

# Get credentials
api_key = os.getenv("AZURE_OPENAI_API_KEY")
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4o-mini")
api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2024-12-01-preview")

print("\n📋 Configuration:")
print(f"API Key: {api_key[:10] if api_key else 'NOT SET'}...{api_key[-5:] if api_key else ''}")
print(f"Endpoint: {endpoint}")
print(f"Deployment: {deployment}")
print(f"API Version: {api_version}")

# Check if credentials exist
if not api_key:
    print("\n❌ AZURE_OPENAI_API_KEY is not set!")
    exit(1)

if not endpoint:
    print("\n❌ AZURE_OPENAI_ENDPOINT is not set!")
    exit(1)

# Try to connect
print("\n🔌 Testing connection...")
try:
    client = AzureOpenAI(
        api_key=api_key,
        api_version=api_version,
        azure_endpoint=endpoint
    )
    
    print("✅ Client created successfully")
    
    # Test completion
    print("\n📤 Sending test request...")
    response = client.chat.completions.create(
        model=deployment,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Say 'Connection successful!' if you can read this."}
        ],
        max_tokens=50
    )
    
    result = response.choices[0].message.content
    print(f"✅ Response: {result}")
    
    print("\n" + "="*70)
    print("✅ AZURE OPENAI CONNECTION SUCCESSFUL!")
    print("="*70)
    
except Exception as e:
    print(f"\n❌ Connection failed: {e}")
    print("\n🔍 Debugging info:")
    print(f"   - Check if API key is correct")
    print(f"   - Check if endpoint URL is correct (should end with /)")
    print(f"   - Check if deployment name '{deployment}' exists")
    print(f"   - Check Azure Portal for key/endpoint")