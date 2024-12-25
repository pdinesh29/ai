from django.shortcuts import render,redirect
import os
import google.generativeai as genai
from .models import accounts
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
def login(req):
    if req.method=='POST':
       email1=req.POST.get('email')
       password1=req.POST.get('password')
       user_exists = accounts.objects.filter(email=email1,password=password1).exists()
       print(email1,password1,user_exists)
       if user_exists:
          return redirect('v1')
    return render(req,'login.html')
def signup(req):
    if req.method=='POST':
       user=accounts()
       user.name=req.POST.get('name')
       user.email=req.POST.get('email')
       user.password=req.POST.get('pass')
       user.save()
       return redirect('login')
    return render(req,'signup.html')
con=[]
def v1(req):
    if req.method=='POST':
        x=str(req.POST.get('inpu'))
        if(x=='clear'):
            con.clear()
            return render(req,'ui.html',{'str1':con,})
        if con and x==con[-1][0]:
          return render(req,'ui.html',{'str1':con,})
        else:
          response = chat_session.send_message(x)
          con.append([x,response.text])
          print(x)
    return render(req,'ui.html',{'str1':con,})
