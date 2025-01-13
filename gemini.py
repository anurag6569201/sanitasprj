from dotenv import load_dotenv
import os
from langchain import LLMChain, PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain_google_genai import ChatGoogleGenerativeAI
import logging

from dotenv import load_dotenv
import os

load_dotenv() #laoding all the envs
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel("gemini-pro") #loading the generative model
model1=genai.GenerativeModel("gemini-pro-vision") #loading the image based model

# function for asking question with the image as well
def get_gemini_vision_response(question,image):
    if question!="":
        response=model1.generate_content([question,image])
        print(response.text)
    else:
        response=model1.generate_content(image)
        print(response.text)

# function for generating the text contant
def get_gemini_response(question):
    response=model.generate_content(question)
    return response

get_gemini_response("write about healthcare under 100 words")