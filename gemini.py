from dotenv import load_dotenv
import os
from langchain import LLMChain, PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain_google_genai import ChatGoogleGenerativeAI
import logging

from dotenv import load_dotenv
import os

load_dotenv()
google_gemini_api = "AIzaSyDXoJrtCEA4bR6h8KKm4FvGV"

if not google_gemini_api:
    raise EnvironmentError("Missing GOOGLE_API_KEY. Ensure it is set in the environment.")

# Initialize Generative Model with langchain-google-genai
try:
    text_model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=google_gemini_api)
except Exception as e:
    raise ConnectionError(f"Failed to initialize Google Gemini model: {e}")

# Define Prompt Template for Text-Based Queries
text_prompt_template = PromptTemplate(
    input_variables=["question"],
    template=(
        "You are a helpful and knowledgeable healthcare assistant for Sanitas, "
        "a platform for tracking diseases and providing medical insights. "
        "Please respond thoroughly and accurately to this query: {question} "
        "under 100 words."
    )
)

# Memory for Conversation Context
memory = ConversationBufferMemory()

# LLMChain for Text Queries
healthcare_chain = LLMChain(
    llm=text_model,
    prompt=text_prompt_template,
    memory=memory
)

# Function to Handle Text-Based Queries
def get_healthcare_response(question: str) -> str:
    try:
        # Validate input
        if not question.strip():
            return "Please provide a valid healthcare query."
        
        # Generate and return response
        response = healthcare_chain.run(question)
        return response.strip() if response else "No response received. Please try again."
    
    except ValueError as ve:
        logging.error(f"ValueError encountered: {ve}")
        return "There was an issue processing your query. Please refine your question."
    
    except ConnectionError as ce:
        logging.error(f"Connection error: {ce}")
        return "Unable to connect to the healthcare assistant service. Please try again later."
    
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return "An unexpected error occurred. Please try again."

# Example usage
if __name__ == "__main__":
    query = "What are the symptoms of dengue fever?"
    print(get_healthcare_response(query))
