# Virtual Stage Competition Guide 🪧 <!-- omit in toc -->

Welcome to the Virtual Stage of the competition! Follow the below document for:

- [Virtual Stage Objective](#virtual-stage-objective)
- [Virtual Stage Submission Requirements](#virtual-stage-submission-requirements)
- [Core-Principles of Self-Driving](#core-principles-of-self-driving)
- [Coordinate System](#coordinate-system)

## Virtual Stage Objective

The objective of the Virtual Stage is to create a video that highlights the performance and high-level details of your team's Self-Driving Car Algorithm. The video submission will be created using Quanser Interactive Labs (QLabs), which will be made available to all teams that register for the competition.

Teams are provided with a [detailed scenario](../Rules_and_Objectives/Virtual_Detailed_Scenario.md) to guide their Self-Driving algorithms and for what to show in their video submission. Please try to create a video showing the sequence of events described in the scenario. This detailed scenario will serve as a good indicator whether a team's algorithm is ready, and it is encouraged that teams make the scenario more complex to fully showcase all aspects of their algorithm. The scenario can be made more complex by spawning in different actors within QLabs to create different traffic scenarios.

[DETAILED SCENARIO (for above section)](../Rules_and_Objectives/Virtual_Detailed_Scenario.md)

Teams will be ranked using the following criteria:

1. Readiness of a Self-Driving algorithm based on the core principles as stated in the Core Principles of Self-Driving section.

2. Accuracy of driving (staying within the lanes).

3. Timely reaction to road signage and traffic controls while adhering to traffic laws.

4. Clear and concise communication of Self-Driving concepts demonstrated in the video.

The last criteria is one of the most important because it will show the judges how well a team understands the principles of self-driving. 

From the 2025 ACC Competition the Czech Technical University submitted the following video and were invited to the Physical Stage of the competition. The judges found this video to contain all of the key elements listed above: [Czech Virtual Stage Submission](https://www.youtube.com/watch?v=JXOI1RtLTbs)

## Virtual Stage Submission Requirements

1. Controlling the QCar or gathering data via the qvl library functions will invalidate any submission.

2. You must adhere to the Software Requirements for the competition you are participating in. This is on the [Competition Page](https://quanser.github.io/student-competitions/) for your competition.

3. Maximum 3-minute video demonstration of the Self-Driving capabilities and explanations.

4. The submission must provide the following:

    - Software: GitHub link to the repository with your team’s submission. The code may be reviewed.

    - Video:  YouTube link demonstrating your code.


## Core-Principles of Self-Driving

**Data Collection:**

A Self-Driving algorithm must be able to collect and filter information from interoceptive and exteroceptive sensors. Demonstrating the conversion of raw data to meaningful information is critical for Self-Driving cars to make higher-level decisions during an autonomous task.

**Interpretation:**

Using system-relevant data, a Self-Driving car must correlate the gathered information to factors happening internally or externally in the environment. Examples of external factors include the identification of traffic signs, traffic lights, pedestrians, and other cars. Examples of internal data include battery monitoring and system state identification.

**Control Systems:**

From the set of viable options determined in the interpretation of the world, the car must be able to execute accurately on the chosen option. This includes staying within lanes, executing turns, stopping at traffic controls, altering a path based on an obstacle, and maintaining a desired speed.

**Localization and Path Planning:**

For a car to arrive at pick-up and drop-off locations, it must understand where it is within the roadmap. This may involve storing a global or local map of the environment in memory. A successful driving algorithm should be able to determine where it is in space and how to get to another location on the competition roadmap. It must also be able to adjust the selected route based on information obtained on its trip such as vehicles on the road, road obstructions, and pedestrians entering/leaving the roadway.

## Coordinate System

Throughout the competition the following coordinate system will be used. The same coordinate system will be used for both the virtual and physical portions of the competition since QLabs contains 1:1 representations of the Quanser Roadmaps.

[0,0,0] and the orientation of the coordinate tool in QLabs will define the base frame that all coordinates are determined from.

![OriginOfTheBaseCoordinateFrame](../Pictures/OriginOfTheMap.png)

Figure 2: Base Frame of the Coordinate System in the Competition Roadmap

Also note that the CityScape maps within QLabs are full scale versions of the Physical Quanser Roapmaps.
