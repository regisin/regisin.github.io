from .people import colaborators, me
from .publications import publications

research = {}
research['title'] = 'Research'
research['projects'] = [
    {
        'name': '3D Obstacle Compliant Mobility Models for UAV networks in ns-3',
        'slug' : '3d-obstacle-compliant-mobility-models-for-uav-networks-in-ns3',
        'excerpt' : 'UAV networks are envisioned to play a crucial role in the future generations of wireless networks. Due to the high cost of failures in system-based tests, initial analysis and refinement of designs and algorithms for UAV applications are performed through rigorous simulations. To facilitate such ...',
        'thumbnail': '/images/3d-obstacle-compliant-mobility-models-for-uav-networks-in-ns3.svg',
        'description': 'UAV networks are envisioned to play a crucial role in the future generations of wireless networks. Due to the high cost of failures in system-based tests, initial analysis and refinement of designs and algorithms for UAV applications are performed through rigorous simulations. To facilitate such simulations for UAV systems, we present different mobility models for emulation of a UAV’s movement. We further extend these models by considering the effect of large obstacles on movement patterns following the three models. The mobility models are prepared as open-source add-ons for ns-3 network simulator. There are currently three mobility models with the adaptations implemented: Random Walk, Random Direction, and Gauss-Markov',
        'people': [
            colaborators['shamik'],
            colaborators['suman'],
            me,
        ],
        'publications': {
            'regis2016implementation': publications['regis2016implementation'],
        },
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
        'thumbnail': '/images/energy-aware-routing-in-multi-radio-multi-channel-heterogeneous-networks.png',
        'description': 'The concept of mesh networks brings many challenges to the research community when designing such system. In addition, allowing the physical mobility of the nodes in the network makes matter even more complicated. The nature of the limited resources that each node has makes a more efficient communication of prime importance. In this research we explore new ideas to expand the lifetime of the network, while maintaining acceptable network performance. First we explore the notion of a centralized network, where a server has information regarding the state of the network. This can be compared to the functionality of current Software Defined Networks, which collect this information and updates parameters in each node of the network. Another line of thought is to have a distributed routing protocol, in which each node has only limited amount of information, and decides by itself the best path to send a packet. The protocol uses a novel link-metric designed to account for both link utilization, as well as the battery charge of the nodes.',
        'people': [
            colaborators['shamik'],
            colaborators['suman'],
            me,
        ],
        'publications': {},
    },
    {
        'name': 'Jamming Attack Mitigation Using Adaptive Beamforming Antenna',
        'slug': 'jamming-attack-mitigation-using-adaptive-beamforming-antenna',
        'excerpt' : 'In multihop ad hoc networks, a jammer can drastically disrupt the flow of information by intentionally interfering with links between a subset of nodes. The impact of such attacks can escalate when the jammer is moving. As a countermeasure for such attacks, adaptive beam-forming techniques can be...',
        'thumbnail': '/images/jamming-attack-mitigation-using-adaptive-beamforming-antenna.png',
        'description': 'In multihop ad hoc networks, a jammer can drastically disrupt the flow of information by intentionally interfering with links between a subset of nodes. The impact of such attacks can escalate when the jammer is moving. As a countermeasure for such attacks, adaptive beam-forming techniques can be employed for spatial filtering of the jamming signal. Considering a moving jammer, a distributed beam nulling framework is proposed. The framework uses periodic measurements of the RF environment to detect direction of arrival (DoA) of jamming signal and suppresses the signals arriving from the current and predicted locations of the jammer. Also, in the calculation of the nulled region, this framework considers and counters the effects of randomness in the mobility of the jammer, as well as errors in beam nulling and DoA measurements. Survivability of links and connectivity in such scenarios are studied by simulating various node distributions and different mobility patterns of the attacker. Also, the impact of errors in the estimation of DoA and beam-forming on the overall network performance is also examined.',
        'people': [
            colaborators['shamik'],
            colaborators['suman'],
            me,
            colaborators['vahid'],
        ],
        'publications': {},
    },
]