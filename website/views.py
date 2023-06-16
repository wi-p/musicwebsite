from django.shortcuts import render
from datetime import date
from website.models import Music, PlayList, Singer
# Create your views here.

def index(request):
    musics = Music.objects.all()[:5]
    playlists = PlayList.objects.all()[:5]
    singers = Singer.objects.all()[:5]
   
    return render(request, 'website/index.html',
        {'date' : date.today(), 
        'musics':musics, 
        'playlists' : playlists,
        'singers' : singers}
    )
    
def result(request, search_item = ''):
    if request.method == 'POST':
        musics = Music.objects.filter(name = request.POST.get('search'))
        playlists = PlayList.objects.filter(name = request.POST.get('search'))
        
    else:
        musics = Music.objects.filter(slug = search_item)
        playlists = PlayList.objects.filter(slug = search_item)
        
    return render(request, 'website/resultpage.html', {'musics' : musics, 'playlists' : playlists})
    
def cdPage(request, cd_name = ''):
    playlist = PlayList.objects.get(slug = cd_name)
    musics = Music.objects.filter(playlist = playlist.id)
    
    return render(
        request,
        'website/cdpage.html',
        {'playlist' : playlist, 'musics' : musics}
    )
    
def singerPage(request, singer_name = ''):
    singer = Singer.objects.get(slug = singer_name)
    musics = Music.objects.filter(singer = singer.id)
    
    return render(request, 'website/singerpage.html', {'singer' : singer, 'musics' : musics})