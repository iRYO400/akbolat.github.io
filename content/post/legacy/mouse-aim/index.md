---
title: Mouse Aiming in UE4/ MP Top-Down
summary: Archived tutorial for UnrealEngine 4
date: 2016-05-21
authors:
  - admin
tags:
  - Legacy
  - UnrealEngine4
  - Top-Down
  - Control
---
Hi-hi!

In this tutorial, I’ll show you how to implement mouse aiming in Top-Down games. In one of the previous tuts I showed a version for [gamepad sticks](/post/legacy/advanced-joystics-mp-top-down/).

P.S. It’s easier to implement than sticks.

{{< youtube id="4iMHOTGkXRg" >}}

Before starting, take a look at this post([Advanced Joystick in UE4 / Multiplayer Top-Down]((/post/legacy/advanced-joystics-mp-top-down/))) until “Setting up Left Stick” item inclusive. Others isn’t necessary if your project doesn’t support gamepad.

In first, create a function in TopDownController. And set next:

{{< figure src="mouseStart1-1.png" >}}

We cast to **TopDownCharacter** through **GetControlledPawn**. Then we call **SetControlRotation**. It has an input named New Rotation. A value for this input we get from our actor’s (**GetActorLocation**) and mouse’s coordinates(**GetHitUnderCursorByChannel**), which connected to **FindLookAtRotation**.

Now in the **EventGraph**, connect our function to **AddMovementInput**.

{{< figure src="mouseStart2.png" >}}

The last step we need to do is – open **TopDownCharacter**, set true UseControllerRotationYaw checkbox in ClassDefaults and set false **OrientRotationToMovement** checkbox in CharacterMovementController.

{{< figure src="mouseStart3.png" >}}

And works in MP. Feel free to ask.

~~Link to project –> Google Drive~~

---
It's a mirror from [WebArchive](https://web.archive.org/web/20190402122855/http://iryos-workshop.com/en/mouse-ue4-mp-top-down)