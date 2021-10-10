
from jinja2 import Environment, PackageLoader, select_autoescape

from reader.XmlReader import XmlReader
import os
import pathlib

current_path = pathlib.Path(__file__).parent.resolve()

env = Environment(
    loader=PackageLoader("html"),
    autoescape=select_autoescape()
)

reader = XmlReader(os.path.join(current_path, "input", "books.xml"))

books = reader.read()

template = env.get_template("html.j2")
rendered = template.render(books=books)
with open("./output.html", "w") as file:
    file.write(rendered)