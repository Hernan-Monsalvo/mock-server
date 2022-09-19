import json
from typing import List, Dict
from ninja import NinjaAPI
from .models import Track
from .schema import TrackSchema, NotFoundSchema

api = NinjaAPI()


@api.get("/tracks", response=List[TrackSchema])
def tracks(request):
    return Track.objects.all()


@api.get("/tracks/{track_id}", response={200: TrackSchema, 404: NotFoundSchema})
def track(request, track_id: int):
    try:
        return 200, Track.objects.get(pk=track_id)
    except Track.DoesNotExist:
        return 404, {"message": "Track does not exist"}


@api.get("/teams", response=List[Dict])
def teams(request):
    f = open('response_teams.json')

    return 200, json.load(f)


@api.get("/teams/{team_key}", response={200: Dict, 404: Dict})
def team(request, team_key):
    f = open('response_teams.json')
    try:
        team = list(filter(lambda x: x["Key"] == team_key.upper(), json.load(f)))[0]
        return 200, team
    except IndexError:
        return 404, {"message": "Team does not exist"}


@api.get("/schedule", response=List[Dict])
def schedules(request):
    f = open('response_schedule.json')

    return 200, json.load(f)


@api.get("/schedule/{team_key}", response={200: List[Dict], 404: Dict})
def schedule(request, team_key):
    f = open('response_schedule.json')
    try:
        sch = list(
            filter(lambda x: x["AwayTeam"] == team_key.upper() or x["HomeTeam"] == team_key.upper(), json.load(f)))
        return 200, sch
    except IndexError:
        return 404, {"message": "Team does not exist"}


@api.get("/week/{week_id}", response={200: List[Dict], 404: Dict})
def schedule(request, week_id):
    try:
        f = open(f'response_scores_week_{week_id}_2022.json')
        return 200, json.load(f)
    except FileNotFoundError:
        return 404, {"message": "Week not played yet"}


@api.get("/league/{league_id}", response={200: Dict, 404: Dict})
def schedule(request, league_id):
    league1 = {
        "name": "Job Guys League",
        "teams": [
            {
                "position": 1,
                "name": "The orange machine",
                "moneyRemaining": 6,
                "results": "11-5-0",
                "pts": 1776,
                "PtsAgst": 1507,
                "of": [
                    {
                        "key": "GB",
                        "value": 58
                    },
                    {
                        "key": "PHI",
                        "value": 1
                    }
                ],
                "de": [
                    {
                        "key": "IND",
                        "value": 25
                    },
                    {
                        "key": "PHI",
                        "value": 10
                    }
                ]
            },
            {
                "position": 2,
                "name": "The Grim Ripper",
                "moneyRemaining": 12,
                "results": "10-6-0",
                "pts": 1729,
                "PtsAgst": 1536,
                "of": [
                    {
                        "key": "KC",
                        "value": 58
                    },
                    {
                        "key": "LAC",
                        "value": 1
                    }
                ],
                "de": [
                    {
                        "key": "NE",
                        "value": 20
                    },
                    {
                        "key": "LAC",
                        "value": 15
                    }
                ]
            },
            {
                "position": 3,
                "name": "Money maker",
                "moneyRemaining": 8,
                "results": "10-6-0",
                "pts": 1709,
                "PtsAgst": 1561,
                "of": [
                    {
                        "key": "TE",
                        "value": 54
                    },
                    {
                        "key": "NY",
                        "value": 10
                    }
                ],
                "de": [
                    {
                        "key": "KE",
                        "value": 20
                    },
                    {
                        "key": "COR",
                        "value": 5
                    }
                ]
            },
            {
                "position": 4,
                "name": "Silvia's Team",
                "moneyRemaining": 10,
                "results": "9-7-0",
                "pts": 1691,
                "PtsAgst": 1578,
                "of": [
                    {
                        "key": "ARI",
                        "value": 54
                    },
                    {
                        "key": "BUF",
                        "value": 24
                    }
                ],
                "de": [
                    {
                        "key": "PA",
                        "value": 12
                    },
                    {
                        "key": "ARI",
                        "value": 5
                    }
                ]
            }

        ]
    }

    league2 = {
        "name": "Cousins League",
        "teams": [
            {
                "position": 1,
                "name": "Little Nicky",
                "moneyRemaining": 16,
                "results": "10-6-0",
                "pts": 1726,
                "PtsAgst": 1507,
                "of": [
                    {
                        "key": "GB",
                        "value": 58
                    },
                    {
                        "key": "PHI",
                        "value": 1
                    }
                ],
                "de": [
                    {
                        "key": "IND",
                        "value": 25
                    },
                    {
                        "key": "PHI",
                        "value": 10
                    }
                ]
            },
            {
                "position": 2,
                "name": "Old Devil knows best",
                "moneyRemaining": 12,
                "results": "10-6-0",
                "pts": 1701,
                "PtsAgst": 1536,
                "of": [
                    {
                        "key": "KC",
                        "value": 58
                    },
                    {
                        "key": "LAC",
                        "value": 1
                    }
                ],
                "de": [
                    {
                        "key": "NE",
                        "value": 20
                    },
                    {
                        "key": "LAC",
                        "value": 15
                    }
                ]
            },
            {
                "position": 3,
                "name": "Joey and Pam",
                "moneyRemaining": 8,
                "results": "10-6-0",
                "pts": 1699,
                "PtsAgst": 1561,
                "of": [
                    {
                        "key": "TE",
                        "value": 54
                    },
                    {
                        "key": "NY",
                        "value": 10
                    }
                ],
                "de": [
                    {
                        "key": "KE",
                        "value": 20
                    },
                    {
                        "key": "COR",
                        "value": 5
                    }
                ]
            },
            {
                "position": 4,
                "name": "Uncle Bob",
                "moneyRemaining": 10,
                "results": "8-8-0",
                "pts": 1687,
                "PtsAgst": 1678,
                "of": [
                    {
                        "key": "ARI",
                        "value": 54
                    },
                    {
                        "key": "BUF",
                        "value": 24
                    }
                ],
                "de": [
                    {
                        "key": "PA",
                        "value": 12
                    },
                    {
                        "key": "ARI",
                        "value": 5
                    }
                ]
            }

        ]
    }

    leagues = {"1": league1, "2": league2}
    print(leagues[league_id])
    if league_id in ["1", "2"]:
        return 200, leagues[league_id]
    else:
        return 404, {"message": "League not found"}
