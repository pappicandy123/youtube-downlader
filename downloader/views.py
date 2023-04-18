from django.shortcuts import redirect, render
from pytube import YouTube
import pathlib

from django.contrib import messages

# Create your views here.
def index(request):
   # urlget = request.GET.get('link')
   # yts = YouTube(urlget)
   if request.method =='POST':
      paste = request.POST['link']
      yt = YouTube(paste)
      folder = f'{pathlib.Path.home() / "Downloads"}'
      yd = yt.streams.get_highest_resolution()
      yd.download(folder)
      # big = yt.title
      # views = yt.views
   

      messages.success(request, 'Dowloaded successful ')
      return redirect('index')
     
   # context={
   # 'big':big,
   # 'views':views,
   # }
     
   return render(request,'index.html')

