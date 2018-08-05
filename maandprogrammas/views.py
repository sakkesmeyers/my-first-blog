from django.shortcuts import render
from django.utils import timezone
from .models import Maandprogramma

# Create your views here.

groepen = ['kajotters', 'noenies', 'lippies', 'jetties', 'rabbits', 'deltas']

styling = styling = '            .jumbotron {                background-color: #f4511e;                color: white;                padding: 100px 25px;            }                    .bg-grey {                background-color: #f6f6f6;            }                    .container-fluid{                padding: 60px 50px;            }                    .logo {                font-size: 200px;            }                    @media screen and (max-width: 768px) {            .col-sm-4 {                text-align: center;                margin: 25px 0;            }        }            .logo-small{                color:#f4511e;                font-size: 50px;            }                    .logo {                color: #f4511e;                font-size: 200px;            }                    .logo-smallest{                color: white;                font-size: 25px;            }                    .thumbnail {            padding: 0 0 15px 0;            border: none;            border-radius: 0;        }                .thumbnail img {            width: 100%;            height: 100%;            margin-bottom: 10px;        }                .navbar{            margin-bottom: 0;            background-color: #f4511e;            z-index: 9999;            border: 0;            font-size: 12px ;            line-height: 1.42857143;            letter-spacing: 4px;            border-radius: 0;        }                .navbar li a, .navbar .navbar-brand {            color: #fff !important;        }                .navbar-nav li a:hover, .navbar-nav li.active a {            color: #f4511e !important;            background-color: #fff !important;        }                .navbar-default .navbar-toggle {            border-color: transparent;            color: #fff !important;        }                .panel-heading{            color: #f4511e;            background-color: #f4511e;        }				.carousel-control.right, .carousel-control.left {    background-image: none;    color: #f4511e;}.carousel-indicators li {    border-color: #f4511e;}.carousel-indicators li.active {    background-color: #f4511e;}.item h4 {    font-size: 19px;    line-height: 1.375em;    font-weight: 400;    font-style: italic;    margin: 70px 0;}.item span {    font-style: normal;}'



def maandprogrammas_list(request):

    kajotters = Maandprogramma.objects.order_by('-created_date').filter(group='kajotters')
    noenies = Maandprogramma.objects.order_by('-created_date').filter(group='noenies')
    lippies = Maandprogramma.objects.order_by('-created_date').filter(group='lippies')
    jetties = Maandprogramma.objects.order_by('-created_date').filter(group='jetties')
    rabbits = Maandprogramma.objects.order_by('-created_date').filter(group='rabbits')
    deltas = Maandprogramma.objects.order_by('-created_date').filter(group='deltas')

    return render(request, 'maandprogrammas/maandprogrammas_list.html', {'kajotters':kajotters, \
    'noenies':noenies, 'lippies':lippies, 'jetties':jetties, 'rabbits'\
    :rabbits, 'deltas':deltas, 'styling':styling})

