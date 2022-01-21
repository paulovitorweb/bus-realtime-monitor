import json

from django.db import migrations
from django.contrib.gis.geos import GEOSGeometry

from bus.models import Terminal


def add_terminal_geofence(apps, schema_editor):
    geofence_dict = {
        'type': 'Polygon',
        'coordinates': [
            [
                [
                    -34.88981276750564,
                    -7.117208210783799
                ],
                [
                    -34.88984763622284,
                    -7.117216195409665
                ],
                [
                    -34.889933466911316,
                    -7.117367903274767
                ],
                [
                    -34.89000856876373,
                    -7.117495657227537
                ],
                [
                    -34.89008903503418,
                    -7.11764736500025
                ],
                [
                    -34.8901292681694,
                    -7.117804395799862
                ],
                [
                    -34.89015609025955,
                    -7.1179614265457465
                ],
                [
                    -34.89014804363251,
                    -7.118107811090956
                ],
                [
                    -34.89015072584152,
                    -7.11821427254906
                ],
                [
                    -34.89009976387024,
                    -7.118270164804671
                ],
                [
                    -34.89004343748093,
                    -7.118320733982444
                ],
                [
                    -34.889960289001465,
                    -7.1183420262661645
                ],
                [
                    -34.88975912332535,
                    -7.118355333942986
                ],
                [
                    -34.88961696624756,
                    -7.118363318548892
                ],
                [
                    -34.889560639858246,
                    -7.1183393647307565
                ],
                [
                    -34.889603555202484,
                    -7.1182541955894765
                ],
                [
                    -34.88963574171066,
                    -7.118083857259489
                ],
                [
                    -34.88970279693603,
                    -7.117650026539666
                ],
                [
                    -34.88974303007125,
                    -7.117397180225421
                ],
                [
                    -34.88979935646057,
                    -7.117234826202824
                ],
                [
                    -34.88981276750564,
                    -7.117208210783799
                ]
            ]
        ]
    }

    geofence = GEOSGeometry(json.dumps(geofence_dict), srid=4326)
    geofence.transform(31985)

    terminal = Terminal(
        name='Terminal de Integração do Varadouro',
        geofence=geofence
    )
    terminal.save()


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0001_initial')
    ]

    operations = [migrations.RunPython(add_terminal_geofence)]
