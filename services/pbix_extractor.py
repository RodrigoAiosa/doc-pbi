import os
import json


class PBIXParser:

    def __init__(self, extracted_folder):
        self.extracted_folder = extracted_folder

    def parse(self):

        report_data = {
            "tables": [],
            "measures": [],
            "pages": []
        }

        layout_path = os.path.join(
            self.extracted_folder,
            "Report",
            "Layout"
        )

        if os.path.exists(layout_path):
            report_data["pages"].append("Relatório Encontrado")

        datamodel_path = os.path.join(
            self.extracted_folder,
            "DataModelSchema"
        )

        if os.path.exists(datamodel_path):
            report_data["tables"].append("Modelo de Dados Encontrado")

        return report_data
