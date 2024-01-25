---
title: Advanced Joystick in UE4 / Multiplayer Top-Down
summary: Archived tutorial for UnrealEngine 4
date: 2016-05-09
authors:
  - admin
tags:
  - Legacy
  - UnrealEngine4
  - Top-Down
  - Control
---

### Overview

    Hey there! This is my first tutorial for UE4. And it associated with first task, which needed be solve, when I started making my first game( less than month ago 😀 ). You can find similar tutorials with mouse implementation. But it couldn’t be adapted for gamepads. So I solved it by myself.

In this tutorial I will teach you to make a thing like this:

{{< youtube id="FXpoiVEUakM" >}}

Using Gamepad’s sticks in Top-Down games. Left stick is for moving, and right is for aiming.

With network replication.

Before we start, I assume that you know these:

- open/create projects UE4
- using Content Browser
- create blueprints/nodes
- functions and variables.

~~Link to project at the end of post~~. Version **4.11.2**.

### Preparing our project

1. In first, create a new Blueprint project with Top-Down template.
2. Find and open two blueprints TopDownCharacter and TopDownController in TopDownBP/Blueprints/ path.
3. Delete all nodes in the Event Graph.

### Set your inputs

Just follow the path Settings–> ProjectSettings–> Inputs

{{< figure src="1.gif" >}}

Set it as in the picture below:

{{< figure src="10.png" >}}

    **MoveForward** and **MoveRight** – are for implementing character’s movement with Left stick, and WASD for debugging.

    **LookRight** и **LookForward** – are for implementing aiming with Right Stick, and ←, →, ↑, ↓ for debugging.

### Setting up Left Stick

Now open TopDownController and make a chain like in the picture below.

{{< figure src="2.png" >}}

    **InputAxis MoveForward** и **MoveRight** – are movement events, that we set in Inputs settings. For Left Stick and WASD.
    **AddMovementInput** – is a replicated by default Pawn’s functions, that responsible for Character’s movement.
    **GetControlledPawn** – gets reference for controlled Character.
    **isValid** – in that case, using for multiplayer debugging.
    **GetForwardVector** и **GetRightVector** – gets directions. We can delete them, and add “90” to X in first AddMovementInput, and “90” to Y in second AddMovementInput.

### Setting up Right Stick

Now the hardest one.

In first, we need create two variables.

{{< figure src="4.png" >}}

    **FaceRotation** – is a Rotator type var with RepNotify replication.
    **isCovered?** – bool that check Right Stick’s changes.

{{< figure src="3.png" >}}

    InputAxis **LookForward** и **LookRight** – are aiming events, that we set in Inputs settings. For Right Stick and ←, →, ↑, ↓.

    **StickRotatorServer** – custom event with Float params( values change between -1.0 and 1.0) and Reliable RunOnServer replication. It calls another custom event that has Multicast replication.

{{< figure src="7.1.png" caption="Click to open" >}}

    **StickRotatorAll** (**1**) – a custom event with Float-parameters and Multicast replication.
Next we cast to our character **CastToTopDownCharacter** (**2**), a reference for character gets from **GetControlledPawn** (**3**). From this link get the coordinates of our character – **GetActorLocation** (**4**).
Float values we convert to Vector – **MakeVector** (**5**). Then sum two vectors (**6**).
Node **FindLookAtRotation** (**7**) – defines where actor is looking, it has two vector inputs **Start** (initial coordinates of the actor, in this case, our character),
**Target** (coordinates of where actor is looking), and output **Rotator**, which rotates actor to Target’s location.
The resulting Rotator and the current face direction of character (**GetActorRotation** (**8b**)) connect to **Lerp**(**Rotator**) (**8a**) in order to smooth rotation.
The result of Lerp write to **FaceRotation** (**9**) var. **VectorLength** (**11a**) gives us the length of the vector from the 5th.
If vector is more than “**0.03**” (**11b**), boolean **isCovered?** (**11c**) sets True and via **Branch** (**12a**) calls a custom event **Covered** (**12b**).
If less than “0.03”, set to **FaceRotation** (**12c**) current direction of our character, then call **NotCovered** (**12d**) event.
Custom events Covered and NotCovered receive references to TopDownCharacter (2) and **CharacterMovementComponent** (**13**).

{{< figure src="6.png" >}}

    **Covered** и **NotCovered** events, which change two inherited bools, then call custom event **RotateNow** (**10**).

    **OrientRotationToMovement** – if True, look first gif. If False second gif.

{{< figure src="two.gif" >}}

{{< figure src="third.gif" >}}

    **UseControllRotationYaw** – if True, Character’s Yaw will be updated to match Controller’s ControllerRotation yaw.
Also when **OrientRotationToMovement** and **UseControllRotationYaw** set True, character on client side begin to tremble.

{{< figure src="5.gif" >}}

Last part is rotating our character.

**FaceRotation** variable has **RepNotify** replication. It means that **OnRep_FaceRotation**(creates in function tab) function calls every time, when FaceRotation changes.

{{< figure src="9.png" >}}

There we cast to TopDownCharacter and call SetControlRotation.


It's a mirror from [WebArchive](https://web.archive.org/web/20190401172509/http://iryos-workshop.com/en/joysticks-mp-top-down-ue4)