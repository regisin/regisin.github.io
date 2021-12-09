import shutil

from jinja2 import Environment, FileSystemLoader
from pathlib import Path

from data import teaching, research


BASE_URL='http://localhost:8000'
BUILD_DIR = '_site'
STATIC_DIR = 'static'                           # Where the static assets are located
CURRENT_PATH = Path.cwd()
BUILD_PATH = CURRENT_PATH / Path(BUILD_DIR)
STATIC_PATH = CURRENT_PATH / Path(STATIC_DIR)
# clean-up build folder
try:
    shutil.rmtree(BUILD_PATH)
except FileNotFoundError:
    print("Build dir does not exist yet.")
shutil.copytree(STATIC_PATH, BUILD_PATH)        # Copy the static folder to the build dir

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

"""
Home
"""
# /
template = env.get_template('about.html')
output = template.render(
    BASE_URL=BASE_URL,
    title="Home ",
)
o = BUILD_PATH / Path('index.html')      # http://BASE_URL/
with o.open(mode='w') as fh:
    fh.write(output)

"""
About
"""
# /about
template = env.get_template('about.html')
output = template.render(
    BASE_URL=BASE_URL,
    title="About",
)
o = BUILD_PATH / Path("about")
o.mkdir(parents=True, exist_ok=True)
o = o / Path('index.html')
with o.open(mode='w') as fh:
    fh.write(output)

"""
Teaching
"""
# /teaching
template = env.get_template('teaching.html')
output = template.render(
    BASE_URL=BASE_URL,
    title="Teaching",
    universities=teaching
)
o = BUILD_PATH / Path("teaching")
o.mkdir(parents=True, exist_ok=True)
o = o / Path('index.html')
with o.open(mode='w') as fh:
    fh.write(output)

"""
Research
"""
# /research
template = env.get_template('research.html')
output = template.render(
    BASE_URL=BASE_URL,
    title="Research",
    projects=research
)
o = BUILD_PATH / Path("research")
o.mkdir(parents=True, exist_ok=True)
o = o / Path('index.html')
with o.open(mode='w') as fh:
    fh.write(output)
"""
Research project detail
"""
# /research/*
template = env.get_template('research_detail.html')
for r in research:
    output = template.render(
        BASE_URL=BASE_URL,
        title='Project details',
        project=r
    )
    o = BUILD_PATH / Path("research/"+r['slug'])
    o.mkdir(parents=True, exist_ok=True)
    o = o / Path('index.html')
    with o.open(mode='w') as fh:
        fh.write(output)