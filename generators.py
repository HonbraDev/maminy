import random
from typing import Callable, Dict

from data import get_person, get_value


def generate_sending_you(person: str = get_person()) -> str:
    place = get_value("places")
    thing = get_value("things")

    return f"{person} z {place} vám posíl{random.choice(['á', 'ají'])} ({random.randint(0, 10)}) {thing}."


def generate_wants_you(person: str = get_person()) -> str:
    place = get_value("places")

    return f"{person} z {place} vás chtějí!"


generators: Dict[Callable, int] = {
    generate_sending_you: 5,
    generate_wants_you: 1
}


def generate(person: str = get_person()) -> str:
    generator = random.choices(list(generators.keys()), weights=generators.values(), k=1)[0]
    return generator(person)
