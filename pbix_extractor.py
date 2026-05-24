import zipfile
import os

class PBIXExtractor:

    def __init__(self, pbix_path):
        self.pbix_path = pbix_path

    def extract(self, output_dir="temp"):

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        with zipfile.ZipFile(self.pbix_path, 'r') as zip_ref:
            zip_ref.extractall(output_dir)

        return output_dir
