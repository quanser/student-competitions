# Virtual Stage Competition Organizer Guide 🪧 <!-- omit in toc -->

This document covers the information necessary to run the virtual stage of the competition as a competition organizer. It will contain Quanser's experience and lessons learned throughout our attempts to manage the competition.

## Topics <!-- omit in toc -->

This document will cover the following:

- [Overall Competition Goal](#overall-competition-goal)
- [Competition Organizer's Goal for the Virtual Stage](#competition-organizers-goal-for-the-virtual-stage)
- [Communications with Teams](#communications-with-teams)
- [General Sequence of Events](#general-sequence-of-events)
  - [Registration](#registration)
  - [Team Development Time](#team-development-time)
  - [Video Submission and Evaluation](#video-submission-and-evaluation)
- [What Resources are Available to the Teams](#what-resources-are-available-to-the-teams)
- [How to Evaluate Team Video Submissions](#how-to-evaluate-team-video-submissions)

## Overall Competition Goal

All resources and competition objectives are intended for a student team to develop a self-driving algorithm that can navigate through the Quanser City Roadmap and stop at specific coordinates. Quanser frames the competition as teams acting as an autonomous taxi service because it is relevant to today's society, but different variations of the competition can be spun off from this one. The important thing is that teams are required to navigate through the map and perform complex decision making during their driving, depending on how the map is configured. Quanser always reserves the right to add complexity to the roadmap by adding things like; buildings, other QCars, obstacles, ect. Quanser generally bases these decisions off of what we believe will allow the teams to showcase their skills the best, while still keeping the competition exciting and approachable.

## Competition Organizer's Goal for the Virtual Stage

As a competition organizer, the goal of the Virtual Stage is to evaluate the readiness of the competing teams for the in-person event based on the video submissions.

While QLabs is an accurate and realistic platform to develop on, it is not an equal playing field for all teams due to the influence of hardware. Better hardware can improve the rate of communication with QLabs, which can increase the rate that QLabs is sending QCar data. A faster processor can also provide a higher ceiling for the amount of computation that can be performed in a control loop. Quanser wants this competition to be approachable even if the team does not have access to a high-end machine. This is why it is sometimes **more important** to evaluate the team's description of the methods used within their self-driving algorithm than the acutal performance being observed on the screen. The hardware limitations can force teams to drive slower than what they can achieve on actual hardware. Once they get to the physical stage, everybody will be using the same hardware. All this should be kept in mind for when the teams are evaluated.

If desired, a fully virtual competition can also be run using the resources, but again, the uneveness of the playing field due to hardware should be kept in mind.

## Communications with Teams

A defined method of communications is needed to convey important information to the student teams. The following is what Quanser uses to communicate:

- Email: The main mode of communications to teams. It is used for, but not limited to, the following:
  - Notifications of important deadlines (registration, submissions, etc.)
  - Sending important links
  - Notifications of changes to the timeline
  - Answering questions  from participants (Quanser provides an email that students can ask non-technical questions on)
- LinkedIn: To raise awareness of the competition publicly
- Website: A landing page for people interested in the competition

## General Sequence of Events

It is important to first understand how the progression of events typically happens during a standard competition. Please see the below timeline:

| Event      | Duration/Time  | Description                   |
|:-------:  |:-----:     | :--------                     |
| Registration Opens |   Available until the submission of the virtual stage   |  The link to register opens where teams will submit details about their team members, student emails, institution info, ect.   |
| Team Development Time | 3-5 Months  | Teams gain access to QLabs (Quanser's Simulation Environement) where they can develop and test their algoirthms. |
| Video Submission Deadline | End of Development Time | Teams must submit a video according to the [Virtual Stage Submission Guidelines](../Rules_and_Objectives/Virtual_Stage_Competition_Guide.md#virtual-stage-submission-requirements). |
| Video Evaluations | 1 Week | Competition Organizers will rank the teams based on their video according to the [Virtual Stage Objective](../Rules_and_Objectives/Virtual_Stage_Competition_Guide.md#virtual-stage-objective). |
| Results Announcement | End of Video Evaluations | If there is a physical stage to the competition, then the top teams will be invited to the in-person competition. |

### Registration

The following information is typically gathered during registration:

- School name
- Team Captain + Email (this person will be used to communicate to the rest of their team)
- Faculty advisor + Email
- Team Member Names + Emails
- Can they travel to the in-person event (get visa's, ect.)
- Do they have access to the software they need

To give teams access to QLabs, you will need to add their emails to your QLabs session.

### Team Development Time

During this time, teams will be utilizing the technical resources provided by Quanser. These resources are hosted on Github and will be monitored for issues constantly.

It is good to also maintain a line of contact with each of the teams if they have any questions about the competition itself.

### Video Submission and Evaluation

It is important to communicate the video submission deadline multiple times throughout the competition as a reminder to the teams of the objective and deadline for the virtual stage of the competition.

Additional details on [How to Evaluate Team Video Submissions](#how-to-evaluate-team-video-submissions) are provided.

It is important to try and perform the evaluation as quick as possible to give teams the most amount of time to prepare to travel to the venue. Keep in mind that some teams may need to obtain visas to the destination country, which can be challenging for some.

## What Resources are Available to the Teams

It is important for competition organizers to be aware of the resources that are provided so that the organizers can communicate essential information to the participants. Each stage has the following resources at a minimum:

- Rules and Objectives
- Technical Resources
  - Software Setup: Teaches the students how to setup a computer to use the language necessary for the competition.
  - Development Guide: Teaches the students some basics for developing within the technical resources that are provided

These resources are hosted on the Quanser Github Pages site and our public Github repositories. Here is the list of relevant links:

- [Current Student Competitions](https://quanser.github.io/student-competitions/)

- [ROS Technical Resources](https://github.com/quanser/student-competition-resources-ros)

- [MATLAB Technical Resources](https://github.com/quanser/student-competition-resources-matlab)

## How to Evaluate Team Video Submissions

It is generally up to the competition organizers to determine how they would like to score the video submissions, but Quanser follows the below guidelines:

Referring to the [Virtual Stage Objectives](../Rules_and_Objectives/Virtual_Stage_Competition_Guide.md#virtual-stage-objective), there are the following 4 criteria that are considered for each video submission:

- Readiness of a Self-Driving algorithm based on the core principles as stated in the Core Principles of Self-Driving section.

- Accuracy of driving (staying within the lanes).

- Timely reaction to road signage and traffic controls while adhering to traffic laws as stated in the Traffic Controls Rules section.

- Clear and concise communication of Self-Driving concepts demonstrated in the video.

The judging engineers will give each submission video a score out of 10 for each of these criteria. To calibrate how the videos should be scored, the judge will view the first few videos without giving it a score. Then they go back and give each a score based on how they felt the performance was.

The scores are then tallied up at the end and the rankings between the different videos are discussed and argued amongst the judges.
