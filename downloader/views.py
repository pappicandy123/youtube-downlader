from django.shortcuts import redirect, render
from pytube import YouTube
import pathlib
import os
import time
import urllib.request
from tqdm import tqdm

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



# def index(request):
#     if request.method =='POST':
#         paste = request.POST['link']
#         yt = YouTube(paste)
#         folder = f'{pathlib.Path.home() / "Downloads"}'
#         yd = yt.streams.get_highest_resolution()

#         # Get the file size of the video
#         file_size = yd.filesize

#         # Create a progress bar with the file size
#         progress_bar = tqdm(total=file_size, unit="B", unit_scale=True)

#         # Download the video in chunks
#         yd.download(folder)

#         # Close the progress bar
#         progress_bar.close()

#         # Print a message indicating the download is complete
#         messages.success(request, 'Download successful')
#         return redirect('index')
   
#     return render(request, 'index.html')







# def index(request):
#     if request.method == 'POST':
#         paste = request.POST['link']
#         yt = YouTube(paste)
#         folder = f'{pathlib.Path.home() / "Downloads"}'
#         yd = yt.streams.get_highest_resolution()

#         # Get the file size of the video
#         file_size = yd.filesize

#         # Create a progress bar with the file size
#         progress_bar = tqdm(total=file_size, unit="B", unit_scale=True)

#         # Download the video in chunks
#         for data in yd.stream().iter_content(chunk_size=4096):
#             progress_bar.update(len(data))
#             urllib.request.urlretrieve(folder, data)

#         # Close the progress bar
#         progress_bar.close()

#         messages.success(request, 'Download successful')
#         return redirect('index')
   
#     return render(request, 'index.html')


# def index(request):
#     if request.method == 'POST':
#         paste = request.POST['link']
#         yt = YouTube(paste)
#         folder = f'{pathlib.Path.home() / "Downloads"}'
#         yd = yt.streams.get_highest_resolution()

#         # Get the file size of the video
#         file_size = yd.filesize

#         # Create a progress bar with the file size
#         progress_bar = tqdm(total=file_size, unit="B", unit_scale=True)

#         # Download the video in chunks
#         for data in yd.stream().iter_content(chunk_size=4096):
#             progress_bar.update(len(data))
#             urllib.request.urlretrieve(folder, data)

#         # Close the progress bar 
#         progress_bar.close()

#         messages.success(request, 'Download successful')
#         return redirect('index')

#     # Create an empty progress bar for initial rendering
#     progress_bar = tqdm(total=100, unit="B", unit_scale=True, dynamic_ncols=True, leave=False)

#     context = {
#         'progress_bar': progress_bar
#     }

#     return render(request, 'index.html', context)


