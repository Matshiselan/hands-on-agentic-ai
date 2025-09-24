import requests
import base64
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai import APIClient
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.foundation_models.schema import TextChatParameters

# Setup credentials and client
credentials = Credentials(url="https://us-south.ml.cloud.ibm.com")
client = APIClient(credentials)

# Load and encode images
url_image_1 = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/5uo16pKhdB1f2Vz7H8Utkg/image-1.png'
url_image_2 = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/fsuegY1q_OxKIxNhf6zeYg/image-2.png'
url_image_3 = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/KCh_pM9BVWq_ZdzIBIA9Fw/image-3.png'
url_image_4 = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/VaaYLw52RaykwrE3jpFv7g/image-4.png'

image_urls = [url_image_1, url_image_2, url_image_3, url_image_4]

print("Encoding images...")
encoded_images = []
for url in image_urls:
    encoded_images.append(base64.b64encode(requests.get(url).content).decode("utf-8"))
print(f"✓ Encoded {len(encoded_images)} images\n")

# Setup model
model_id = "meta-llama/llama-3-2-90b-vision-instruct"
project_id = "skills-network"
params = TextChatParameters()

model = ModelInference(
    model_id=model_id,
    credentials=credentials,
    project_id=project_id,
    params=params
)

# ============================================
# TODO: COMPLETE THIS FUNCTION
# ============================================
def generate_model_response(encoded_image, user_query, assistant_prompt="You are a helpful assistant. Answer the following user query in 1 or 2 sentences: "):
    """
    Send an image + question to the AI model and get back an answer.
    
    Parameters:
    - encoded_image: Base64 string of the image
    - user_query: Your question about the image
    - assistant_prompt: Optional system prompt (defaults to helpful assistant)
    
    Returns:
    - The AI's response as a string
    """
    
    # TODO: Create the messages list
    # Should have role "user" with content containing both text and image
    messages = [
        {
            "role": "user",
            "content": [
                # Add text part here (combine assistant_prompt + user_query)
                # Add image part here (use "data:image/jpeg;base64," + encoded_image)
            ]
        }
    ]
    
    # TODO: Send to the model using model.chat(messages=messages)
    response = None
    
    # TODO: Extract the text from response['choices'][0]['message']['content']
    return None


# ============================================
# TESTS
# ============================================

print("="*50)
print("TESTING YOUR FUNCTION")
print("="*50)

# Test 1: Street scene description
print("\n=== Test 1: Basic Image Description ===")
# TODO: Call your function with encoded_images[0] and the query
print(f"Query: Describe this image")
print(f"Response: [YOUR RESULT HERE]\n")

# Test 2: Clothing detection
print("=== Test 2: Specific Object Detection ===")
# TODO: Call your function with encoded_images[1]
print(f"Query: What is the person wearing?")
print(f"Response: [YOUR RESULT HERE]\n")

# Test 3: Weather analysis
print("=== Test 3: Scene Analysis ===")
# TODO: Call your function with encoded_images[2]
print(f"Query: What weather condition is shown in this image?")
print(f"Response: [YOUR RESULT HERE]\n")

# Test 4: Text extraction
print("=== Test 4: Text Recognition ===")
# TODO: Call your function with encoded_images[3]
print(f"Query: What is the serving size listed on this label?")
print(f"Response: [YOUR RESULT HERE]\n")

print("="*50)
print("All tests completed! ✓")
print("="*50)
