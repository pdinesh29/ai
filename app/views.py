from django.shortcuts import render,redirect
import os
import google.generativeai as genai
from .models import accounts
genai.configure(api_key='AIzaSyA4Uk_W9B_mRiF-UoQr0qVO2xar_REDCkE')
from django.contrib.sessions.models import Session
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
       if user_exists:
          con=list(req.session.get('chat'))
          return render(req,'ui.html',{'str1':con})
    return render(req,'login.html')
def signup(req):
    if req.method=='POST':
       user=accounts()
       user.name=req.POST.get('name')
       user.email=req.POST.get('email')
       user.password=req.POST.get('pass')
       req.session['email']=user.email
       req.session['password']=user.password
       req.session['chat']=tuple()
       user.save()
       return redirect('login')
    return render(req,'signup.html')
def v1(req):
    con=list(req.session.get('chat'))
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
          req.session['chat']=tuple(con)
          print(x)
    return render(req,'ui.html',{'str1':con,})
