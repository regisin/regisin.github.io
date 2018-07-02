---
layout: page
title: Energy Aware Routing in Multi-radio Multi-channel Heterogeneous Networks
excerpt: UAV networks are envisioned to play a crucial role in the future generations of wireless networks. Due to the high cost of failures in system-based tests, initial analysis and refinement of designs and algorithms for UAV applications are performed through rigorous simulations. To facilitate such simulations for UAV systems, we present different mobility models for emulation of a UAV's movement. We further extend these models by considering the effect of large obstacles on movement patterns following the three models. The mobility models are prepared as open-source add-ons for ns-3 network simulator.
tags: [research]
category: research
thumbnail: energy-aware-routing-in-multi-radio-multi-channel-heterogeneous-networks.png
---
{% assign pdfsign = '<i class="fa fa-file-pdf-o"></i>'%}
{% assign pptsign = '<i class="fa fa-file-powerpoint-o"></i>'%}

### Problem Statement and Motivation

The concept of mesh networks brings many challenges to the research community when designing such system.
In addition, allowing the physical mobility of the nodes in the network makes matter even more complicated.
The nature of the limited resources that each node has makes a more efficient communication of prime importance.
In this research we explore new ideas to expand the lifetime of the network, while maintaining acceptable network performance.
First we explore the notion of a centralized network, where a server has information regarding the state of the network.
This can be compared to the functionality of current Software Defined Networks, which collect this information and updates parameters in each node of the network.
Another line of thought is to have a distributed routing protocol, in which each node has only limited amount of information, and decides by itself the best path to send a packet.
The protocol uses a novel link-metric designed to account for both link utilization, as well as the battery charge of the nodes.


### People
  - [Shamik Sengupta](https://www.cse.unr.edu/~shamik/) (University of Nevada, Reno)
  - [Suman Bhunia](http://www.sbhunia.me) (University of Nevada, Reno)
  - [Paulo Alexandre Regis](http://www.pregis.me) (University of Nevada, Reno)


### Publications
1. **PA Regis**, S Sengupta, "Distributed split-path routing strategy for multi-hop mesh networks", IEEE Military Communications Conference (MILCOM) 2017, Baltimore, MD. [{{pdfsign}}](manuscripts/milcom_17.pdf) [{{pptsign}}](manuscripts/milcom_17.pptx)

1. **PA Regis**, S Bhunia and S Sengupta, "Enhancing Performance and Longevity of Multi-radio Multi-channel HetNets through Dynamic Path-assignment", IEEE International Conference on Computing, Networking and Communications (ICNC) 2017, Silicon Valley, USA. [{{pdfsign}}](manuscripts/icnc_17.pdf) [{{pptsign}}](manuscripts/icnc_17.pptx)


<!-- ### Useful Links 
1. [Github Repository with implementations](https://github.com/regisin/ns-3-obstacles) -->