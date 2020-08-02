import requests
import pyttsx3
def speak(words):
    engine=pyttsx3.init()
    engine.say(words)
    engine.runAndWait()
def send_message(text,email_address,cc_list,file_attachment):
    api_key='3aa065ece6fdb90f5c34186be0d0f8ca-a65173b1-7e342786'
    domain='sandbox4e23937762fd4b43ac9852ce179a6819.mailgun.org'
    base_url=f'https://api.mailgun.net/v3/{domain}/messages'
    sender='Mailgun Sandbox <postmaster@sandbox4e23937762fd4b43ac9852ce179a6819.mailgun.org>'
    
    subject='random'
    receiver=email_address
    if len(email_address)==0:
        speak("no email address")
        return
        
    if len(cc_list)==0:
        if not file_attachment:
            return requests.post(base_url,auth=('api',api_key),data={"from": sender, "to":receiver,"subject":subject,
    "text":text})
        else:
            files=[]
            for location in file_attachment:
                files.append(("attachment",(location,open(location,'rb').read())))
            return requests.post(base_url,auth=('api',api_key),files=files,data={"from": sender, "to":receiver,"subject":subject,
    "text":text})
    else:
        if not file_attachment:
            return requests.post(base_url,auth=('api',api_key),data={"from": sender, "to":receiver,'cc':cc_list,"subject":subject,
    "text":text})
        else:
            files=[]
            for location in file_attachment:
                files.append(("attachment",(location,open(location,'rb').read())))
            return requests.post(base_url,auth=('api',api_key),files=files,data={"from": sender, "to":receiver,'cc':cc_list,"subject":subject,
    "text":text})

        


  
    






def send_simple_message():
	return requests.post(
		"https://api.mailgun.net/v3/sandbox4e23937762fd4b43ac9852ce179a6819.mailgun.org/messages",
		auth=("api", "3aa065ece6fdb90f5c34186be0d0f8ca-a65173b1-7e342786"),
		data={"from": "Mailgun Sandbox <postmaster@sandbox4e23937762fd4b43ac9852ce179a6819.mailgun.org>",
			"to": "Hamza Yusuff <hamzalondon27yusuff@gmail.com>",
			"subject": "Hello Hamza Yusuff",
			"text": "Congratulations Hamza Yusuff, you just sent an email with Mailgun!  You are truly awesome!"})
speak('Please input the number of email adresses down below')
n=int(input("Number of addresses: "))
email = []
filename=[]
cc=[]
speak("Please enter the email addresses one by one")
for i in range(n):
    email.append(input("EMAIL : "))
speak("Do you want to add cc")
responsecc=input("yes or no : ")
if responsecc.lower()=="yes":
    speak("How many cc?")
    number=int(input("number of cc : "))
    for i in range(number):
        cc.append(input("cc : "))

speak("Do you want to add attachments?")
responseattachment=input("yes or no: ")
if responseattachment.lower()=='yes':
    speak("how many attachments ?")
    numattachment=int(input("number of attachments: "))
    
    for k in range(numattachment):
        speak("enter the filename make sure its in the same directory")
        filename.append(input("filename :"))
speak("Please input the text")
text=input("WRITE THE TEXT : ")
send_message(text,email,cc,filename)
speak("Thank you the email is sent successfully")