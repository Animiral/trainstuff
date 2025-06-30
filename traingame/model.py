from dataclasses import dataclass, field
from typing import List, Dict, Tuple, Union
from enum import Enum
import random

# Constants
MAP_SIZE = (10, 10)
N_CITIES = 6
CITY_NAMES = [
    "London",
    "Paris",
    "Berlin",
    "Midgard",
    "Atlantis",
    "New York",
    "Tokyo",
    "Rome",
    "Madrid",
    "Sydney",
    "Moscow",
    "Toronto",
    "Rio de Janeiro",
    "Dubai",
    "Cape Town",
    "Valhalla",
    "Elysium",
    "Asgard",
    "Themyscira",
    "Shambhala"
]
COMPANY_NAMES = [
    "United Rail Co.",
    "Iron Horse Railways",
    "Steel & Steam Group",
    "Intrack Ltd.",
    "Great Western Lines",
    "Midland Railway Co.",
    "Transcontinental Express",
    "Eastern Railroad Corp.",
    "Golden Spike Railways",
    "Atlantic Pacific Rail"
]

class Connection(Enum):
    NORTH_EAST = "north-east"
    NORTH_SOUTH = "north-south"
    NORTH_WEST = "north-west"
    SOUTH_EAST = "south-east"
    SOUTH_WEST = "south-west"
    EAST_WEST = "east-west"

# Data Classes
@dataclass
class City:
    name: str
    depots: List[str] = field(default_factory=list)

@dataclass
class TrackTile:
    track: set[Connection] = field(default_factory=set)

@dataclass
class Player:
    cash: int
    shares: Dict[str, int] = field(default_factory=dict)  # Company name to number of shares

@dataclass
class Company:
    name: str
    home: List[str] = field(default_factory=list)  # List of city names where depots are located
    trains: List[str] = field(default_factory=list)  # List of trains that the company operates

@dataclass
class Map:
    grid: List[List[Union[City, TrackTile]]] = field(default_factory=list)
    cities: Dict[str, Tuple[int, int]] = field(default_factory=dict)  # Lookup by name to grid location

    def randomize(self, map_size = None, city_names = None, n_cities = None):
        if map_size is None:
            map_size = MAP_SIZE
        if city_names is None:
            city_names = CITY_NAMES
        if n_cities is None:
            n_cities = N_CITIES
        self.grid = [[TrackTile() for _ in range(map_size[0])] for _ in range(map_size[1])]
        self.cities = dict()
        city_names = random.sample(city_names, n_cities)
        all_locations = [(x, y) for x in range(map_size[0]) for y in range(map_size[1])]
        city_locations = random.sample(all_locations, n_cities)
        for name, (x, y) in zip(city_names, city_locations):
            self.grid[x][y] = City(name=name)
            self.cities[name] = (x, y)
        return self

@dataclass
class Model:
    map: Map = field(default_factory=Map)
    players: List[Player] = field(default_factory=list)
    companies: List[Company] = field(default_factory=list)

    def randomize(self, n_players: int):
        self.map.randomize()
        self.players = [Player(cash=1000,) for _ in range(n_players)]
        company_names = random.sample(COMPANY_NAMES, n_players)
        company_homes = random.sample(list(self.map.cities.keys()), n_players)
        self.companies = [Company(name=name, home=[home])
            for (name, home) in zip(company_names, company_homes)]
        return self
