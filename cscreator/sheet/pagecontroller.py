import logging

from cscreator.character.characterenums import CHProperty
from cscreator.components.custom.generic_component import component_file_parser
from cscreator.components.properties import Properties
from cscreator.components.standard.box import BoxController
from cscreator.sheet.pagemodel import PageModel
from cscreator.views.pageview import PageView

logger = logging.getLogger(__name__)


class PageController:
    def __init__(self, character_controller):
        self.page_model = self.set_standard_layout(character_controller)
        self.page_view = PageView(scene=self.page_model)
        # self.page_view.show()
        logger.info("PageView constructed")

    def set_standard_layout(self, active_character_controller):
        main_grid = PageModel()

        banner = component_file_parser("resc/components/banner.json")
        main_grid.add_component_controller(
            banner.get_component(Properties(0, 0, 50, 10))
        )

        bottom_row_start = 64

        column_1_start = 2
        column_1_width = 15

        column_2_start = 17
        column_2_width = 16

        column_3_start = 33
        column_3_width = 15

        ability_skills_attack_row = 49
        hp_grip_flaws_row = 32
        #
        # # Column1
        main_grid.add_component_controller(
            BoxController(
                Properties(column_1_start, bottom_row_start - 12, column_1_width, 12),
                "Personality Traits",
                CHProperty.PERSONALITY_TRAITS,
                active_character_controller,
            )
        )
        main_grid.add_component_controller(
            BoxController(
                Properties(0, 0, 12, 12),
                "OTHER PROFICIENCIES & LANGUAGES",
                CHProperty.PERSONALITY_TRAITS,
                active_character_controller,
            )
        )
        # # main_grid.add_component(
        # #     SingleLineBox(
        # #         Properties(column_1_start, 49, column_1_width, 3),
        # #         "PASSIVE WISDOM (PERCEPTION)",
        # #         "passive_wisdom",
        # #     )
        # # )
        # ability_scores_grid = SubGrid(
        #     Properties(column_1_start, ability_skills_attack_row-37, 5, 37), 1, 6
        # )
        # # ability_scores_grid.add_component(
        # #     AbilityBox(Properties(0, 5, 1, 1), "STRENGTH", "standard")
        # # )
        # # ability_scores_grid.add_component(
        # #     AbilityBox(Properties(0, 4, 1, 1), "DEXTERITY", "standard")
        # # )
        # # ability_scores_grid.add_component(
        # #     AbilityBox(Properties(0, 3, 1, 1), "CONSTITUTION", "standard")
        # # )
        # # ability_scores_grid.add_component(
        # #     AbilityBox(Properties(0, 2, 1, 1), "INTELLIGENCE", "standard")
        # # )
        # # ability_scores_grid.add_component(
        # #     AbilityBox(Properties(0, 1, 1, 1), "WISDOM", "standard")
        # # )
        # # ability_scores_grid.add_component(
        # #     AbilityBox(Properties(0, 0, 1, 1), "CHARISMA", "standard")
        # # )
        # main_grid.add_component(ability_scores_grid)
        main_grid.add_component_controller(
            BoxController(
                Properties(7, ability_skills_attack_row - 23, 10, 23),
                "SKILLS",
                CHProperty.SENSES,
                active_character_controller,
            )
        )
        main_grid.add_component_controller(
            BoxController(
                Properties(7, 35, 10, 9),
                "SAVING THROWS",
                CHProperty.SAVE_MODIFIERS,
                active_character_controller,
            )
        )
        # # main_grid.add_component(
        # #     SingleLineBox(Properties(7, 14, 10, 3), "INSPIRATION", "inspiration")
        # # )
        # # main_grid.add_component(
        # #     SingleLineBox(
        # #         Properties(7, 11, 10, 3), "PROFICIENCY BONUS", "proficiency_bonus"
        # #     )
        # # )
        #
        # # Column 2
        # main_grid.add_component(
        #     Box(
        #         Properties(column_2_start, bottom_row_start-15, column_2_width, 15),
        #         "EQUIPMENT",
        #         CH.CP,
        #         "standard",
        #     )
        # )
        # main_grid.add_component(
        #     Box(
        #         Properties(column_2_start, ability_skills_attack_row-17, column_2_width, 17),
        #         "ATTACKS & SPELLCASTING",
        #         CH.ATTACKS,
        #         "standard",
        #     )

        # hp_grid = component_file_parser("resc/components/hp_grid.json")
        # main_grid.add_component(
        #     hp_grid.get_component(
        #         Properties(column_2_start, hp_grip_flaws_row - 21, column_2_width, 21)
        #     )
        # )

        # # Column 3
        # main_grid.add_component(
        #     Box(
        #         Properties(column_3_start, bottom_row_start-32, column_3_width, 32),
        #         "FEATURES & TRAITS",
        #         CH.FEATURES_TRAITS
        #     )
        # )
        # personality_grid = SubGrid(
        #     Properties(column_3_start, hp_grip_flaws_row-21, column_3_width, 21), 1, 4
        # )
        # personality_grid.add_component(
        #     Box(Properties(0, 62, 1, 1), "PERSONALITY TRAITS", CH.PERSONALITY_TRAITS, "standard")
        # )
        # personality_grid.add_component(Box(Properties(0, 2, 1, 1), "IDEALS", CH.IDEALS, "standard"))
        # personality_grid.add_component(Box(Properties(0, 1, 1, 1), "BONDS", CH.BONDS, "standard"))
        # personality_grid.add_component(Box(Properties(0, 0, 1, 1), "FLAWS", CH.FLAWS, "standard"))
        # main_grid.add_component(personality_grid)

        return main_grid
