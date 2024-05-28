from Bot.settings.setting import settings
import os
import google.generativeai as genai


class Geminiapp:
  
  def __init__(self):
  
    self.genai= genai.configure(api_key=settings.GEMINI_API_KEY)
    self.generation_config = {
      "temperature": 1,
      "top_p": 0.95,
      "top_k": 64,
      "max_output_tokens": 8192,
      "response_mime_type": "text/plain",
    }
    self.settingsx=settings.SEFTY_SETTINGS
  
    self.safety_settings = [
        {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
      },
      {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
      },
      {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
      },
      {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
      },
    ]
    
    self.model = genai.GenerativeModel(
      model_name="gemini-1.5-pro",
      safety_settings=self.safety_settings,
      generation_config=self.generation_config,
    )
  
    
  def geminiapp(self,text:str,img):

    response = self.model.generate_content(text, img)
    
    return response
  
  def geminitext(self,text:str):
     chat_session=self.model.start_chat(
       history=[ ],
       
     )
     
     responce=chat_session.send_message(text)
     
     return {
        "chat_session":chat_session.history,
        "responce":responce
     }



