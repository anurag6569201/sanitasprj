from dotenv import load_dotenv
import google.generativeai as genai
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
