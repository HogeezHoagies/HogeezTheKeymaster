from __future__ import annotations

from typing import List

from dataclasses import dataclass

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class TouhouLunaNightsArchipelagoOptions:
    pass


class TouhouLunaNightsGame(Game):
    name = "Touhou Luna Nights"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.SW,
        KeymastersKeepGamePlatforms.XONE,
        KeymastersKeepGamePlatforms.PS4,
        KeymastersKeepGamePlatforms.PS5,
    ]
    
    is_adult_only_or_unrated = False

    options_cls = TouhouLunaNightsArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Complete without using Knives.",
                data=dict(),
            ),
        ]

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="From a fresh save file, collect the EARLYITEM",
                data={"EARLYITEM": (self.earlyitems, 1)},
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="From a fresh save file, dunk a can in EARLYDUNK",
                data={"EARLYDUNK": (self.earlydunks, 1)},
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="By any method necessary, dunk a can in LATEDUNK",
                data={"LATEDUNK": (self.latedunks, 1)},
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="By any method necessary, defeat BOSS",
                data={"BOSS": (self.bosses, 1)},
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="From a fresh save file, defeat Meiling",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
        ]

    @staticmethod
    def earlyitems() -> List[str]:
        return [
            "Eternal Clock in Stage 1",
            "HP Upgrade in Stage 1",
            "MP Upgrade in Stage 1",
            "Stun Knife in Stage 1",
            "Auto Aim in Stage 1",
            "Red Key in Stage 1",
            "Sliding Knife in Stage 1",
        ]
        
    @staticmethod
    def earlydunks() -> List[str]:
        return [
            "Wastebin 1 in Stage 1",
            "Wastebin 2 in Stage 1",
            "Wastebin 3 in Stage 1",
            "every Wastebin in Stage 1",
        ]
        
    @staticmethod
    def latedunks() -> List[str]:
        return [
            "Wastebin 1 in Stage 2",
            "Wastebin 2 in Stage 2",
            "Wastebin 3 in Stage 2",
            "every Wastebin in Stage 2",
            "Wastebin 1 in Stage 3",
            "Wastebin 2 in Stage 3",
            "Wastebin 3 in Stage 3",
            "every Wastebin in Stage 3",
            "Wastebin 1 in Stage 4",
            "Wastebin 2 in Stage 4",
            "Wastebin 3 in Stage 4",
            "every Wastebin in Stage 4",
            "Wastebin 1 in Stage 5",
            "Wastebin 2 in Stage 5",
            "Wastebin 3 in Stage 5",
            "every Wastebin in Stage 5",
        ]

    @staticmethod
    def bosses() -> List[str]:
        return [
            "Meiling",
            "Marisa",
            "Patchouli",
            "Remilia",
            "Nitori",
            "Flandre",
        ]

# Archipelago Options
# ...
