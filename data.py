import random
from typing import Dict

data: Dict[str, Dict[str, int]] = {
    "people": {
        "Mamina": 5,
        "Maminy": 3,
        "Kate25": 1
    },
    "peoplePrefix": {
        "Nadržená": 1,
        "Nadržené": 1
    },
    "places": {
        "Prague": 5,
        "vaše okolí": 4,
        "Brno": 3,
        "Olomouc": 3,
        "Aš": 1,
        "Deutsche": 1
    },
    "things": {
        "fotografie": 5,
        "videa": 3,
        "pusinky": 1,
        "srdíčka": 1
    },
    "websites": {
        "shawl-anderson.org": 1,
        "portabrace.com": 1,
        "friendsoffrontenac.com": 1,
        "montaluce.com": 1,
        "w1.123movies-org.site": 1,
        "watchseries.pub": 1,
        "freemoviedownload.sk": 1,
        "freemoviedownload.tk": 1,
        "news7h.com": 1,
        "www2.hurawatch.org": 1,
        "yomovies.cam": 1,
        "game-config.com": 1,
        "dramacool.ac": 1,
        "www2.sflix.cc": 1
    }
}


def get_value(name: str) -> str:
    try:
        the_dict = data[name]
        return random.choices(list(the_dict.keys()), weights=the_dict.values(), k=1)[0]
    except KeyError:
        raise KeyError(f"The data key '{name}' could not be found.")


def get_person() -> str:
    if random.random() < 0.5:
        return f"{get_value('peoplePrefix')} {get_value('people')}"
    else:
        return get_value("people")
