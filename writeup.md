# Reflection Tree Design

## Overview

This project builds a deterministic reflection tool that guides employees through a structured end-of-day reflection.

The system is implemented as a **decision tree** where each node represents a question, reflection, or transition.

Users select from fixed options, and each answer leads to a predefined next step.

---

## Three Reflection Axes

The conversation is organized into three psychological axes.

### Axis 1 – Locus (Victim vs Victor)

This axis explores whether the user perceives events as external circumstances or recognizes their own agency.

Questions focus on reactions to problems and personal responses to success or failure.

---

### Axis 2 – Orientation (Contribution vs Entitlement)

This axis examines whether the user focuses on what they contributed to others or what they expected to receive.

Questions explore teamwork, helping behavior, and expectations of recognition.

---

### Axis 3 – Radius (Self vs Others)

This axis widens the reflection to consider the impact of actions on others.

The user reflects on whether they focused mainly on themselves, their team, or customers.

---

## Deterministic Tree Design

The reflection system is deterministic:

- Every question has fixed options
- Each option leads to a known next node
- The same answers always produce the same path

Signals are stored during the conversation to determine which reflection branch is shown.

---

## Possible Improvements

Future improvements could include:

- a graphical interface
- richer summary generation
- daily reflection tracking

## Diagram
```mermaid
flowchart TD

START --> OPEN_Q1

OPEN_Q1 --> A1_Q1
A1_Q1 --> A1_Q2
A1_Q2 --> A1_Q3
A1_Q3 --> A1_DECISION

A1_DECISION --> A1_REF_INTERNAL
A1_DECISION --> A1_REF_EXTERNAL

A1_REF_INTERNAL --> BRIDGE_1_2
A1_REF_EXTERNAL --> BRIDGE_1_2

BRIDGE_1_2 --> A2_Q1
A2_Q1 --> A2_Q2
A2_Q2 --> A2_Q3
A2_Q3 --> A2_DECISION

A2_DECISION --> A2_REF_CONTRIBUTION
A2_DECISION --> A2_REF_ENTITLEMENT

A2_REF_CONTRIBUTION --> BRIDGE_2_3
A2_REF_ENTITLEMENT --> BRIDGE_2_3

BRIDGE_2_3 --> A3_Q1
A3_Q1 --> A3_Q2
A3_Q2 --> A3_Q3
A3_Q3 --> A3_DECISION

A3_DECISION --> A3_REF_SELF
A3_DECISION --> A3_REF_OTHERS

A3_REF_SELF --> SUMMARY
A3_REF_OTHERS --> SUMMARY

SUMMARY --> END