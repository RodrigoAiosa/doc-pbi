from jinja2 import Environment, FileSystemLoader
import os


class DocumentationGenerator:

    def __init__(self):
        self.env = Environment(
            loader=FileSystemLoader("templates")
        )

    def generate_html(self, data, output_file="outputs/documentation.html"):

        template = self.env.get_template("report_template.html")

        html_content = template.render(data=data)

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(html_content)

        return output_file
