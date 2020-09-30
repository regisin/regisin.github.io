from pathlib import Path
import shutil
from jinja2 import Environment, FileSystemLoader

from store import gen, about, teaching, research, publications

CURRENT_PATH = Path.cwd()
BUILD_DIR = '_site'

"""After building, run to serve:
python -m http.server --directory ./_site/
"""
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

def author_me_filter(author):
    s = author_name_filter(author['name'])
    if author == gen['me']:
        s = '<strong>' + s + '</strong>'
    return s
def author_name_filter(name):
    s = name.split(" ")[0][0].upper()
    if len(name.split(" ")) > 2:
        for w in name.split(" ")[1:-1]:
            s += w[0].upper()
    s += " " + name.split(" ")[-1]
    return s
def month_name_filter(month):
    if month == 1:
        return 'January'
    elif month == 2:
        return 'February'
    elif month == 3:
        return 'March'
    elif month == 4:
        return 'April'
    elif month == 5:
        return 'May'
    elif month == 6:
        return 'June'
    elif month == 7:
        return 'July'
    elif month == 8:
        return 'August'
    elif month == 9:
        return 'September'
    elif month == 10:
        return 'October'
    elif month == 11:
        return 'November'
    elif month == 12:
        return 'December'
    else:
        return 'Badeya'

env.filters['author_filter'] = author_me_filter
env.filters['month_name_filter'] = month_name_filter

"""
Pre build
"""
# remove current build
try:
    shutil.rmtree(CURRENT_PATH / Path(BUILD_DIR))
except FileNotFoundError:
    print("Build dir does not exist (yet).")
# create folder structure
path = CURRENT_PATH / Path(BUILD_DIR)
path.mkdir(parents=True, exist_ok=True)
file_path = path / Path("files")
img_path = path / Path("images")
# copy static files
src_file_path = CURRENT_PATH / Path('static/files')
shutil.copytree(src_file_path, file_path)
src_img_path = CURRENT_PATH / Path('static/images')
shutil.copytree(src_img_path, img_path)

cname = path / 'CNAME'
with open(cname,'w') as fh:
    fh.write(gen['site'])

"""
Index
"""
# /
template = env.get_template('about.html')
output = template.render(
    general=gen,
    title=about['title'],
    about=about
)
o = path
o.mkdir(parents=True, exist_ok=True)
o = o / Path('index.html')
with o.open(mode='w') as fh:
    fh.write(output)

"""
About
"""
# /about
template = env.get_template('about.html')
output = template.render(
    general=gen,
    title=about['title'],
    about=about
)
o = path / Path("about")
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
    general=gen,
    title=teaching['title'],
    universities=teaching['universities']
)
o = path / Path("teaching")
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
    general=gen,
    title=research['title'],
    projects=research['projects']
)
o = path / Path("research")
o.mkdir(parents=True, exist_ok=True)
o = o / Path('index.html')
with o.open(mode='w') as fh:
    fh.write(output)

# /research/*
template = env.get_template('research_detail.html')
for r in research['projects']:
    output = template.render(
        general=gen,
        project=r
    )
    o = path / Path("research/"+r['slug'])
    o.mkdir(parents=True, exist_ok=True)
    o = o / Path('index.html')
    with o.open(mode='w') as fh:
        fh.write(output)


"""
Publications
"""
# /publications
template = env.get_template('publications.html')
output = template.render(
    general=gen,
    title=publications['title'],
    conferences=publications['conferences'],
    journals=publications['journals']
)
o = path / Path("publications")
o.mkdir(parents=True, exist_ok=True)
o = o / Path('index.html')
with o.open(mode='w') as fh:
    fh.write(output)

# /publications/*
template = env.get_template('publication_detail.html')
for k,pub in publications['conferences'].items():
    output = template.render(
        general=gen,
        pub_id=k,
        publication=pub
    )
    o = path / Path("publications/"+k)
    o.mkdir(parents=True, exist_ok=True)
    o = o / Path('index.html')
    with o.open(mode='w') as fh:
        fh.write(output)
for k,pub in publications['journals'].items():
    output = template.render(
        general=gen,
        pub_id=k,
        publication=pub
    )
    o = path / Path("publications/"+k)
    o.mkdir(parents=True, exist_ok=True)
    o = o / Path('index.html')
    with o.open(mode='w') as fh:
        fh.write(output)