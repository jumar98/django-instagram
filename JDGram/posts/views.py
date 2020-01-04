from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


posts = [
    {
        'title': "Forget everything that you think you know",
        'user': {
            'name': "Dr. Strange",
            'picture': 'https://codigoespagueti.com/wp-content/uploads/2017/08/thor-strange-1080x600.png'
        },
        'timestamp': datetime.now().strftime('%b %dTh, %Y - %H:%M Hrs'),
        'photo': 'https://codigoespagueti.com/wp-content/uploads/2017/08/thor-strange-1080x600.png'
    },
    {
        'title': "I am Iron Man",
        'user': {
            'name': "Iron Man",
            'picture': 'https://cdn.colombia.com/sdi/2018/09/04/avengers-4-quien-sera-el-sucesor-de-iron-man-668712.jpg'
        },
        'timestamp': datetime.now().strftime('%b %dTh, %Y - %H:%M Hrs'),
        'photo':'https://cdn.colombia.com/sdi/2018/09/04/avengers-4-quien-sera-el-sucesor-de-iron-man-668712.jpg'    
    },
    {
        'title': "You can't justify murder by masking it with a cause",
        'user':{
            'name': "Captain America",
            'picture': 'https://www.screengeek.net/wp-content/uploads/2019/11/avengers-endgame-captain-america.jpg'
        },
        'timestamp': datetime.now().strftime('%b %dTh, %Y - %H:%M Hrs'),
        'photo': 'https://www.screengeek.net/wp-content/uploads/2019/11/avengers-endgame-captain-america.jpg'
    }
]

# Create your views here.
def list_posts(requests):
    return render(requests, 'posts/feed.html', {'posts': posts})