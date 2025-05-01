from __future__ import annotations

from typing import List

from dataclasses import dataclass

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class SonicColorsDSArchipelagoOptions:
    pass


class SonicColorsDSGame(Game):
    name = "Sonic Colors DS"
    platform = KeymastersKeepGamePlatforms.DS

    platforms_other = None

    is_adult_only_or_unrated = False

    options_cls = SonicColorsDSArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Finish ZONE ACT",
                data={
                    "ZONE": (self.zones, 1),
                    "ACT": (self.acts, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Get at least one Red Star Ring in ZONE ACT",
                data={
                    "ZONE": (self.zones, 1),
                    "ACT": (self.acts, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Defeat BOSS",
                data={
                    "BOSS": (self.bosses, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Finish ZONE ACT with at least 50 Rings",
                data={
                    "ZONE": (self.zones, 1),
                    "ACT": (self.acts, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Finish SPECIAL with an S Rank",
                data={
                    "SPECIAL": (self.specials, 1)
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Finish ZONE ACT with an S Rank",
                data={
                    "ZONE": (self.zones, 1),
                    "ACT": (self.acts, 1)
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Defeat BOSS with an S Rank",
                data={
                    "BOSS": (self.bosses, 1)
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Get all five Red Star Rings in ZONE ACT",
                data={
                    "ZONE": (self.zones, 1),
                    "ACT": (self.acts, 1)
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Win the race in ZONE SIM in Eggman's Sonic Simulator",
                data={
                    "ZONE": (self.zones, 1),
                    "SIM": (self.sims, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Win the race in ZONE SIM in Eggman's Sonic Simulator with at least 50 Rings",
                data={
                    "ZONE": (self.zones, 1),
                    "SIM": (self.sims, 1)
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=1,
            ),
        ]

    @staticmethod
    def zones() -> List[str]:
        return [
            "Tropical Resort",
            "Sweet Mountain",
            "Starlight Carnival",
            "Planet Wisp",
            "Aquarium Park",
            "Asteroid Coaster"
        ]
        
    @staticmethod
    def acts() -> List[str]:
        return [
            "Act 1",
            "Act 2",
            "Mission 1",
            "Mission 2",
            "Mission 3"
        ]
        
    @staticmethod
    def bosses() -> List[str]:
        return [
            "Globotron in Tropical Resort",
            "Captain Jelly in Sweet Mountain",
            "Orcan in Starlight Carnival",
            "Drillinator in Planet Wisp",
            "Admiral Jelly in Aquarium Park",
            "Skullian in Asteroid Coaster",
            "Nega Wisp Armor in Terminal Velocity",
            "Nega Mother Wisp above Planet Wisp"
        ]
        
    @staticmethod
    def specials() -> List[str]:
        return [
            "Special Stage 1",
            "Special Stage 2",
            "Special Stage 3",
            "Special Stage 4",
            "Special Stage 5",
            "Special Stage 6",
            "Special Stage 7"
        ]
        
    @staticmethod
    def sims() -> List[str]:
        return [
            "Act 1",
            "Act 2",
            "Act 3",
            "Opponent's Choice"
        ]
    

# Archipelago Options
# ...
