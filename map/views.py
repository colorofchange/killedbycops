import json
from django.shortcuts import render
from django.http.response import HttpResponse

from models import StoryEmbed


def stories_json(request):
    embeds = [{'name': s.name,
               'url': s.url,
               'image': s.image.url,
               'county_fips': s.county.fips_code()} for s in StoryEmbed.objects.all()]
    data = json.dumps(embeds)
    return HttpResponse(data, content_type='application/json')


def map(request):
    STATE_CODES = (
        ('Alabama', 1),
        ('Alaska', 2),
        ('Arizona', 4),
        ('Arkansas', 5),
        ('California', 6),
        ('Colorado', 8),
        ('Connecticut', 9),
        ('Delaware', 10),
        ('District of Columbia', 11),
        ('Florida', 12),
        ('Georgia', 13),
        ('Hawaii', 15),
        ('Idaho', 16),
        ('Illinois', 17),
        ('Indiana', 18),
        ('Iowa', 19),
        ('Kansas', 20),
        ('Kentucky', 21),
        ('Louisiana', 22),
        ('Maine', 23),
        ('Maryland', 24),
        ('Massachusetts', 25),
        ('Michigan', 26),
        ('Minnesota', 27),
        ('Mississippi', 28),
        ('Missouri', 29),
        ('Montana', 30),
        ('Nebraska', 31),
        ('Nevada', 32),
        ('New Hampshire', 33),
        ('New Jersey', 34),
        ('New Mexico', 35),
        ('New York', 36),
        ('North Carolina', 37),
        ('North Dakota', 38),
        ('Ohio', 39),
        ('Oklahoma', 40),
        ('Oregon', 41),
        ('Pennsylvania', 42),
        ('Rhode Island', 44),
        ('South Carolina', 45),
        ('South Dakota', 46),
        ('Tennessee', 47),
        ('Texas', 48),
        ('Utah', 49),
        ('Vermont', 50),
        ('Virginia', 51),
        ('Washington', 53),
        ('West Virginia', 54),
        ('Wisconsin', 55),
        ('Wyoming', 56)
    )

    return render(request, 'map.html', {'STATE_CODES': STATE_CODES,
        'title': "KilledByCops 2000-2015 | Thousands Killed. Incomplete Data. Insufficient Action."}
    )
