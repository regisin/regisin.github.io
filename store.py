import os

from data.people import colaborators, me
from data.publications import publications as pubs
from data.teaching import teaching as teach
from data.research import research as res
# from data.blog import blog as blog_

"""
Global variables
"""
gen = {}
gen['site'] = 'regisin.github.io'
if os.environ.get('BUILD_ENV') == 'production':
    gen['build_env'] = 'production'
    gen['base_url'] = 'https://' + gen['site']
else:
    gen['build_env'] = 'dev'
    gen['base_url'] = 'http://127.0.0.1:8000'
gen['me'] = me
gen['menu'] = [
    { 'label': gen['site'], 'url': '/' },
    { 'label': 'Teaching', 'url': '/teaching' },
    { 'label': 'Research', 'url': '/research' },
    { 'label': 'Publications', 'url': '/publications' },
]
gen['footer'] = [
    { 'label': 'GitHub', 'url': 'https://github.com/regisin' },
    { 'label': 'stackoverflow', 'url': 'https://stackoverflow.com/users/2962392/regisin' },
    { 'label': 'Google Scholar', 'url': 'https://scholar.google.com/citations?user=IKSrj8wAAAAJ' },
    { 'label': 'LinkedIn', 'url': 'https://www.linkedin.com/in/regisin/' },
]

"""
About
"""
about = {}
about['title'] = 'About'
about['biography'] = "I’m an Assistant Professor in the Department of Computer Science at Southeastern Louisiana University. I was a member of the Networks Lab (former CNL) since 2014 when joining the doctoral program, working under the supervision of Dr. Shamik Sengupta, until my graduation in 2019. Previously, I obtained my Bachelor’s degree in Telecommunications Engineering from Regional University of Blumenau, Brazil in 2011. :)"
about['interests'] = [
    "Longevity of Mobile Ad-hoc Networks",
    "3D Mobility Models",
    "Communication in 3D mesh network",
    "Survivability against Jamming Attacks",
]

"""
Teaching
"""
teaching = teach

"""
Research
"""
research = res

"""
Publications
"""
publications = {}
publications['title'] = 'Publications'
publications['conferences'] = {k:v for k,v in pubs.items() if v['type'] == 'conf'}
publications['journals'] = {k:v for k,v in pubs.items() if v['type'] == 'jour'}

"""
Blog posts
"""
# blog = blog_
