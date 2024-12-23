from django.shortcuts import render
import os
import google.generativeai as genai
genai.configure(api_key='AIzaSyA4Uk_W9B_mRiF-UoQr0qVO2xar_REDCkE')

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
  ]
)
con=[]
def v1(req):
    if req.method=='POST':
        x=str(req.POST.get('inpu'))
        if(x=='clear'):
            con.clear()
            return render(req,'ui.html',{'str1':con})
        response = chat_session.send_message(x)
        con.append([x,response.text])
    return render(req,'ui.html'{'str1':con})
