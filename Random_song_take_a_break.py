import time
import webbrowser
import random

#Feel Good Inc.
a = "https://www.youtube.com/watch?v=NxxjLD2pmlk"
#When You Were Young
b = "https://www.youtube.com/watch?v=0k-v9cp9Fxc"
#Burnin' For You
c = "https://www.youtube.com/watch?v=ipqqEFoJPL4"
#Changes
d = "https://www.youtube.com/watch?v=omhNnvX3Sx0"
#Rock the Casbah
e = "https://www.youtube.com/watch?v=0pCFVX6lzHU"
#Down Under
f = "https://www.youtube.com/watch?v=hfmxO-HQ5rU"
#Take Me Out
g = "https://www.youtube.com/watch?v=RMmRac5wYv4"
#Ruby
h = "https://www.youtube.com/watch?v=XioruVM0pU8"
#Here I Drempt I Was an Architect
i = "https://www.youtube.com/watch?v=Sy0NySwzDzY"
#Enjoy the Silence
j = "https://www.youtube.com/watch?v=6bYKZbWxKoQ"
#The Promise
k = "https://www.youtube.com/watch?v=vyLtOeT-5vY"
#Hold Me Now
l = "https://www.youtube.com/watch?v=FxvbED6gTBI"
#Bring Me to Life
m = "https://www.youtube.com/watch?v=6CA-8OSX5U0"
#Kryptonite
n = "https://www.youtube.com/watch?v=tQ-EM6DbFQk"
#All Star
o = "https://www.youtube.com/watch?v=Je_8A5hurSY"
#Africa
p = "https://www.youtube.com/watch?v=QAo_Ycocl1E"
#Viva la Vida
q = "https://www.youtube.com/watch?v=zOQ4ld6NsXE"
#Over the Hills and Far Away
r = "https://www.youtube.com/watch?v=60iwmyhV8pQ"
#Seasons Change
s = "https://www.youtube.com/watch?v=zJD2jLjXsls"
#I Can't Wait
t = "https://www.youtube.com/watch?v=UJ1tBVtYOBc"
#Rocketeer
u = "https://www.youtube.com/watch?v=hnK5sv9mWeo"
#Sit Next to Me
v = "https://www.youtube.com/watch?v=uypLTcMfwHE"
#Stylo
w = "https://www.youtube.com/watch?v=OmwZtFwFj94"
#Stand by Me
x = "https://www.youtube.com/watch?v=xICj8-Psl5A"
#Zion and Babylon
y = "https://www.youtube.com/watch?v=O7mgzsZOnoI"
#Lean on
z = "https://www.youtube.com/watch?v=rn9AQoI7mYU"

foo = [a,b,c,d,e,f,g,h,i,j,k,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
# 'l' is omitted from list foo becasue the algorythm that selects numbers at random seems to favor 'l'

def take_a_break():
    for i in range (1,1000*1000):
        time.sleep(1) 
        print(i + 1)

        if i % 3600 == 0:
            webbrowser.open(random.choice(foo)) 
        
        

take_a_break() 
