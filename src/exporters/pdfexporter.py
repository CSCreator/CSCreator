import csv
import os

from PySide2.QtCore import QStandardPaths
from fitz import fitz

from src.models.charactermodel import CH

conversion_key = {
    "Front_Character Name": "CH.CHARACTER_NAME",
    "Front_Race": "CH.CHARACTER_NAME",
    "Front_Background": "CH.BACKGROUND",
    "Front_Alignment": "CH.ALIGNMENT",
    "Front_XP": "CH.XP",
    "Front_Level": "CH.CLASS_LEVEL",
    "Front_Proficiency": "CH.PROF_BONUS",
    "Front_Passive Perception": "CH.PASSIVE_PERCEPTION",
    "Front_Inspiration": "CH.INITIATIVE",
    "Front_Passive Insight": "CH.PASSIVE_INVESTIGATION",
    "Front_Str Mo": "CH.STR_MOD",
    "Front_Str Score": "CH.STR",
    "Front_Dex Mod": "CH.DEX_MOD",
    "Front_Dex Score": "CH.DEX",
    "Front_Con Mod": "CH.CON_MOD",
    "Front_Con Score": "CH.CON",
    "Front_Int Mod": "CH.INT_MOD",
    "Front_Int Score": "CH.INT",
    "Front_Wis Mod": "CH.WIS_MOD",
    "Front_Wis Score": "CH.WIS",
    "Front_Cha Mod": "CH.CHA_MOD",
    "Front_Cha Score": "CH.CHA",
    "Front_Save Str": "CH.STR_ST_PROF",
    "Front_Str Save Throw": "CH.STR_ST_MOD",
}


class PDFExporter:
    def __init__(self, player_controller):
        self.player_controller = player_controller

    def export(self):
        dir_to_search = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation)
        dir_to_search = os.path.join(dir_to_search, "exporters")
        file_to_export_to = os.path.join(
            dir_to_search, "Character Sheet_FIGHTER-BM_FILLABLE.pdf"
        )

        form_fields = {}
        doc = fitz.open(file_to_export_to)
        for page_number in range(doc.pageCount):
            page = doc.loadPage(page_number)
            for field in page.widgets():
                if field.field_name in conversion_key.keys():
                    ch = CH(conversion_key[field.field_name])
                    field.field_value = getattr(
                        self.player_controller.player_model, ch.name
                    )
                    field.update()

        doc.save("test.pdf")

        with open("dict_out.csv", "w", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            for key, value in form_fields.items():
                writer.writerow([key, value])
