#gtts app by durgeshrawat
import os,time
from tkinter import *
from tkinter import messagebox as msg
from tkinter import ttk
import pygame
from gtts import gTTS

if os.path.isdir('.cache')==False:
    os.system('mkdir .cache')
    os.system('mkdir compiled_tts')

pygame.init()
root=Tk()
root.maxsize(720,1080)
root.minsize(720,1080)
class data:
	def __init__(self):
		self.width=720
		self.height=1225
	
class buttonFUNCTIONS:
	def playsound(self):
		pygame.mixer.music.load('.cache/'+t+'.mp3')
		pygame.mixer.music.play(1)
		
	def cleartext(self):
		text.set('')
	
	def save(self):
		global t
		os.system('mv .cache/'+t+'.mp3 compiled_tts')
		msg.showinfo('saved ','file Saved sucessfully in \nrespective address in \nfolder compiled_tts')
		
	def delete(self):
		os.system('rm -rf .cache && mkdir .cache')
		msg.showinfo('Task completed','file deleted sucessfully !')
		
	def maketts(self):
		global drop,var,text,t
		t=text.get()
		language=drop.get()
		speedvalue=var.get()
		languagelist=['Hindi',
						'English (India)',
						'English (US)',
						'English (UK',
						'English (Canada)',
						'English (Ireland)',
						'English (SouthAfrica)',
						'French (Canada)',
						'French (France)',
						'Mandarian (China Mainland)',
						'Manderian (Taiwan)',
						'Portuguese (Brazil)',
						'Portuguese (Portugal)',
						'Spanish (Maxico)',
						'Spanish (Spain)',
						'Spanish (US)']			
		code_for_lan=['hi','en','en','en','en','en','en','fr','fr','zh-CN','zh-TW','pt','pt','es','es','es']
		lancode=code_for_lan[languagelist.index(language)]
		speedrate=False
		if speedvalue==-1.0:
			speedrate=True
		try:
			speech=gTTS(text=t,lang=lancode,slow=speedrate)
			speech.save('.cache/'+t+'.mp3')
			after_maketts=Toplevel()
			after_maketts.title('Compiled Your TTS')
			after_maketts.geometry('300x400+100+200')
			Button(after_maketts,text='play',command=buttonFUNCTIONS().playsound).place(x=80,y=50)
			Button(after_maketts,text='delete',command=buttonFUNCTIONS().delete).place(x=70,y=150)
			Button(after_maketts,text='save',command=buttonFUNCTIONS().save).place(x=80,y=250)
		except:
			msg.showwarning('connection inturupted!','please check your internet \nconnection and try again.')
		
class main(data):
	def taptocontinue(self):
		can=Canvas(root,width=self.width,height=self.height).place(x=0,y=0)
		Label(can,text='Google Text To Speech'+' '*39,bg='light blue',padx=40,pady=25).place(x=0,y=0)
		global text
		text=StringVar()
		Label(can,text='Text').place(x=60,y=150)
		Entry(can,textvariable=text,width=30,fg='blue').place(x=60,y=200)
		Label(can,text='Select Language').place(x=60,y=270)
		global drop
		drop=StringVar()
		langs=ttk.Combobox(can,width=29,textvariable=drop)
		langs['values']=('Hindi',
						'English (India)',
						'English (US)',
						'English (UK',
						'English (Canada)',
						'English (Ireland)',
						'English (SouthAfrica)',
						'French (Canada)',
						'French (France)',
						'Mandarian (China Maunland)',
						'Manderian (Taiwan)',
						'Portuguese (Brazil)',
						'Portuguese (Portugal)',
						'Spanish (Maxico)',
						'Spanish (Spain)',
						'Spanish (US)'
						)
		langs.place(x=60,y=330)
		langs.current(0)
		Label(can,text='Speed').place(x=60,y=400)
		global var
		var=DoubleVar()
		speedslider=Scale(can,{'from':-1,'to':1},variable=var,orient=HORIZONTAL,tickinterval=1,length=500).place(x=90,y=440)
		sp='Slow,Default,Fast'.split(',')
		x=90
		for i in sp:
			Label(can,text=i,font='verdana 6').place(x=x,y=515)
			x+=220
		Button(can,text='Make TTS',bg='light blue',command=buttonFUNCTIONS().maketts).place(x=90,y=900)
		Button(can,text='clear TEXT',command=buttonFUNCTIONS().cleartext).place(x=370,y=900)

class design(data):
	def welcome_screen(self):
		txt='gTTs'
		color='red,green,orange,blue'.split(',')
		xpos=(160,150+100,150+205,150+300)
		ypos=(530,500,500,500)
		for i in range(4):
			Label(root,text=txt[i],font='verdana 40 bold',fg=color[i]).place(x=xpos[i],y=ypos[i])
		Label(root,text='devloper[ DURGESH ]',font='verdana 6',fg='grey').place(x=self.width-self.width*1/2-100+20,y=670)
		Label(root,text='loading ...',font='verdana 8').place(x=300,y=1080)

myapp=design()
myapp.welcome_screen()
root.update_idletasks()
time.sleep(1.5)
main().taptocontinue()

root.mainloop()