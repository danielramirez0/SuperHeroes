from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Superhero

# Create your views here.


def index(request):
    all_heroes = Superhero.objects.all()
    context = {
        'all_heroes': all_heroes
    }
    return render(request, 'superheroes/index.html', context)


def detail(request, hero_id):
    single_hero = Superhero.objects.get(pk=hero_id)
    context = {
        'hero': single_hero
    }
    return render(request, 'superheroes/detail.html', context)


def create(request):
    if request.method == 'POST':
        # Save the form contents as a new db object
        # return to index
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary = request.POST.get('primary')
        secondary = request.POST.get('secondary')
        catchphrase = request.POST.get('catchphrase')
        new_hero = Superhero(name=name, alter_ego=alter_ego, primary_ability=primary,
                             secondary_ability=secondary, catch_phrase=catchphrase)
        new_hero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request, 'superheroes/create.html')


def edit(request, hero_id):
    hero = Superhero.objects.get(pk=hero_id)

    if request.method == 'POST':
        hero = Superhero.objects.get(pk=hero_id)
        hero.name = request.POST.get('name')
        hero.alter_ego = request.POST.get('alter_ego')
        hero.primary_ability = request.POST.get('primary')
        hero.secondary_ability = request.POST.get('secondary')
        hero.catch_phrase = request.POST.get('catchphrase')
        hero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        context = {
            'hero': hero
        }
        return render(request, 'superheroes/edit.html', context)

def delete(request, hero_id):
    hero = Superhero.objects.get(pk=hero_id)
    hero.delete()
    return HttpResponseRedirect(reverse('superheroes:index'))