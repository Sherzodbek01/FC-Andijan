import datetime as datetime
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializer import *


@api_view(['GET'])
def get_new_slider(request):
    header = Slider.objects.all().order_by('-id')[:3]
    ser = SliderSerializer(header, many=True).data
    return Response(ser)


@api_view(['GET'])
def get_video(request):
    video = Video.objects.all().order_by('-id')[:4]
    ser = VideoSerializer(video, many=True).data
    return Response(ser)


@api_view(['GET'])
def get_players(request):
    team = Players.objects.all()
    data = {
        'time': datetime.datetime.now().time(),
        'date': datetime.datetime.now().date(),
        'team': TeamSerializer(team, many=True).data,
        'team_count': team.count(),
        'last_player': TeamSerializer(team.last()).data,
    }
    return Response(data)


@api_view(['DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def delete_players_view(request, pk):
    Players.objects.get(id=pk).delete()
    return Response({"message": "Done"})


@api_view(['GET'])
def get_shop(request):
    shop = Shop.objects.all()
    ser = ShopSerializer(shop, many=True).data
    return Response(ser)


@api_view(['DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def delete_players_view(request, pk):
    Shop.objects.get(id=pk).delete()
    return Response({"message": "Done"})


@api_view(['GET'])
def get_information(request):
    info = Information.objects.all()
    ser = InformationSerializer(info, many=True).data
    return Response(ser)


@api_view(['GET'])
def get_partners(request):
    partner = Partners.objects.all().order_by('-id')[:5]
    ser = PartnersSerializer(partner, many=True).data
    return Response(ser)


@api_view(['GET'])
def get_news(request):
    news = News.objects.all().order_by('-id').last()
    ser = NewsSerializer(news).data
    return Response(ser)


@api_view(['GET'])
def get_(request):
    news = News.objects.all().order_by('-id').last()
    ser = NewsSerializer(news).data
    return Response(ser)


@api_view(['GET'])
def ckeditor(request):
    content = Content.objects.all()
    ser = ContentSerializer(content, many=True).data
    return Response(ser)



@api_view(['GET'])
def get_club(request):
    content = Content.objects.all()
    ser = ContentSerializer(content, many=True).data
    return Response(ser)


@api_view(['GET'])
def get_academy(request):
    content = Academy.objects.all()
    ser = AcademySerializer(content, many=True).data
    return Response(ser)

@api_view(['GET'])
def get_arena(request):
    content = Arena.objects.all()
    ser = ArenaSerializer(content, many=True).data
    return Response(ser)

@api_view(['GET'])
def get_background(request):
    background = Background.objects.all()
    ser = BackgroundSerializer(background, many=True).data
    return Response(ser)
