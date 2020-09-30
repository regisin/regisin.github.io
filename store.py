from data.people import colaborators, me
from data.publications import publications as pubs
"""
Global variables
"""
gen = {}
gen['site'] = 'pregis.me'
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
about['biography'] = "I’m an Assistant Professor in the Department of Computer Science at Southeastern Louisiana University. I was a member of the Networks Lab (former CNL) since 2014 when joining the doctoral program, working under the supervision of Dr. Shamik Sengupta, until my graduation in 2019. Previously, I obtained my Bachelor’s degree in Telecommunications Engineering from Regional University of Blumenau, Brazil in 2011."
about['interests'] = [
    "Longevity of Mobile Ad-hoc Networks",
    "3D Mobility Models",
    "Communication in 3D mesh network",
    "Survivability against Jamming Attacks",
]

"""
Teaching
"""
teaching = {}
teaching['title'] = 'Teaching'
teaching['universities'] = [
    {
        'name': 'Southeastern Louisiana University',
        'courses': [
            "Algorithm Design and Implementation II (CMPS 280) Spring 2020",
            "Special Topics in Information Technology (CMPS 494/594) Spring 2020",
            "Advanced Computer Networks (CMPS 161) Fall 2019",
            "Introduction to Applied Networking (CMPS 209) Fall 2019",
            "Algorithm Design and Implementation I (CMPS 161) Fall 2019",
        ]
    },
    {
        'name': 'University of Nevada, Reno',
        'courses': [
            "Computer Communication Networks (CPE 400/600) Spring 2019",
        ]
    },
    {
        'name': 'Teaching assistant',
        'courses': [
            "Introduction to Engineering Design (ENGR 100) Fall 2017, Fall 2018",
            "Computer Communication Networks (CPE 400/600) Fall 2017, Fall 2018",
        ]
    },
    {
        'name': 'Research Experience Mentor',
        'courses': [
            "RET: Cyber Security Initiative for Nevada Teachers Summer 2017, Summer 2018",
            "REU: Collaborative Human-Robot Interaction Summer 2018",
        ]
    }
]
"""
Research
"""
research = {}
research['title'] = 'Research'
research['projects'] = [
    {
        'name': '3D Obstacle Compliant Mobility Models for UAV networks in ns-3',
        'slug' : '3d-obstacle-compliant-mobility-models-for-uav-networks-in-ns3',
        'excerpt' : 'UAV networks are envisioned to play a crucial role in the future generations of wireless networks. Due to the high cost of failures in system-based tests, initial analysis and refinement of designs and algorithms for UAV applications are performed through rigorous simulations. To facilitate such ...',
        'thumbnail': '../images/3d-obstacle-compliant-mobility-models-for-uav-networks-in-ns3.svg',
        'description': 'UAV networks are envisioned to play a crucial role in the future generations of wireless networks. Due to the high cost of failures in system-based tests, initial analysis and refinement of designs and algorithms for UAV applications are performed through rigorous simulations. To facilitate such simulations for UAV systems, we present different mobility models for emulation of a UAV’s movement. We further extend these models by considering the effect of large obstacles on movement patterns following the three models. The mobility models are prepared as open-source add-ons for ns-3 network simulator. There are currently three mobility models with the adaptations implemented: Random Walk, Random Direction, and Gauss-Markov',
        'people': [
            colaborators['shamik'],
            colaborators['suman'],
            me,
        ],
        'publications': [
            pubs['regis2016implementation']
        ],
        'embed': [
            '<iframe width="560" height="315" src="https://www.youtube.com/embed/ACmmxe3vPjo" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
            '<iframe width="560" height="315" src="https://www.youtube.com/embed/zJocofWmodg" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
            '<iframe width="560" height="315" src="https://www.youtube.com/embed/1m8X7NGdP3w" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
            '<iframe width="560" height="315" src="https://www.youtube.com/embed/MFCymLmYj6U" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
        ],
        'support': None
    },
    {
        'name': 'Energy Aware Routing in Multi-radio Multi-channel Heterogeneous Networks',
        'slug': 'energy-aware-routing-in-multi-radio-multi-channel-heterogeneous-networks',
        'excerpt' : 'UAV networks are envisioned to play a crucial role in the future generations of wireless networks. Due to the high cost of failures in system-based tests, initial analysis and refinement of designs and algorithms for UAV applications are performed through rigorous simulations. To facilitate such ...',
        'thumbnail': '../images/energy-aware-routing-in-multi-radio-multi-channel-heterogeneous-networks.png',
        'description': 'The concept of mesh networks brings many challenges to the research community when designing such system. In addition, allowing the physical mobility of the nodes in the network makes matter even more complicated. The nature of the limited resources that each node has makes a more efficient communication of prime importance. In this research we explore new ideas to expand the lifetime of the network, while maintaining acceptable network performance. First we explore the notion of a centralized network, where a server has information regarding the state of the network. This can be compared to the functionality of current Software Defined Networks, which collect this information and updates parameters in each node of the network. Another line of thought is to have a distributed routing protocol, in which each node has only limited amount of information, and decides by itself the best path to send a packet. The protocol uses a novel link-metric designed to account for both link utilization, as well as the battery charge of the nodes.',
        'people': [
            colaborators['shamik'],
            colaborators['suman'],
            me,
        ],
    },
    {
        'name': 'Jamming Attack Mitigation Using Adaptive Beamforming Antenna',
        'slug': 'jamming-attack-mitigation-using-adaptive-beamforming-antenna',
        'excerpt' : 'In multihop ad hoc networks, a jammer can drastically disrupt the flow of information by intentionally interfering with links between a subset of nodes. The impact of such attacks can escalate when the jammer is moving. As a countermeasure for such attacks, adaptive beam-forming techniques can be...',
        'thumbnail': '../images/jamming-attack-mitigation-using-adaptive-beamforming-antenna.png',
        'description': 'In multihop ad hoc networks, a jammer can drastically disrupt the flow of information by intentionally interfering with links between a subset of nodes. The impact of such attacks can escalate when the jammer is moving. As a countermeasure for such attacks, adaptive beam-forming techniques can be employed for spatial filtering of the jamming signal. Considering a moving jammer, a distributed beam nulling framework is proposed. The framework uses periodic measurements of the RF environment to detect direction of arrival (DoA) of jamming signal and suppresses the signals arriving from the current and predicted locations of the jammer. Also, in the calculation of the nulled region, this framework considers and counters the effects of randomness in the mobility of the jammer, as well as errors in beam nulling and DoA measurements. Survivability of links and connectivity in such scenarios are studied by simulating various node distributions and different mobility patterns of the attacker. Also, the impact of errors in the estimation of DoA and beam-forming on the overall network performance is also examined.',
        'people': [
            colaborators['shamik'],
            colaborators['suman'],
            me,
            colaborators['vahid'],
        ],
    },
]

# research['3d-obstacle-compliant-mobility-models-for-uav-networks-in-ns3-research'] = {

# }
"""
Publications
"""
publications = {}
publications['title'] = 'Publications'
publications['conferences'] = {k:v for k,v in pubs.items() if v['type'] == 'conf'}
publications['journals'] = {k:v for k,v in pubs.items() if v['type'] == 'jour'}