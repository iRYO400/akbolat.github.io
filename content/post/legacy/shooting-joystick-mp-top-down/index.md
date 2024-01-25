---
title: Shooting in Unreal Engine 4 / MP Top-Down
summary: Archived tutorial for UnrealEngine 4
date: 2016-05-20
authors:
  - admin
tags:
  - Legacy
  - UnrealEngine4
  - Top-Down
  - Control
---

Hi folks!

In my first tutorial I showed how to setup joysticks for Top-Down games – Advanced Joystick in UE4 / Multiplayer Top-Down. Now we’ll integrate firing in this. I.e. when shifting stick for a half from its center, character is aiming, and shifting for a max, character is firing.

This post based on previous, please l take a look.

Inside **TopDownController** create new Float var – **FireRate** with 1.0 value. There is a custom event **RotateNow**, that sets a new value to **FaceRotation**.

{{< figure src="firing2.png" >}}

In first, we’ll check a vector length( we did that in [prevous post](/post/legacy/advanced-joystics-mp-top-down/), **11b** and **12a** articles).
If it less than **0.8**, character doesn’t shoot, else we call FlowControl function – **DoOnce**. DoOnce executes ones and then blocks.
To unblock, it must be re-calle through the Reset (more about DoOnce can be read [here](https://docs.unrealengine.com/latest/INT/Engine/Blueprints/UserGuide/FlowControl/#doonce).)

After it we call another FlowControl – **Sequence**. Sequence performs a sequence of action, Then 0, Then1, Then2, Then3…
In our case, Then 0 calls PrintString( instead of firing), Then 1 – Delay, that calls Reset in DoOnce. Delay’s duration equals to FireRate’s value.

{{< figure src="firing3,1.png" caption="Instead of shooting, we call PrintString with “FIRE!” text" >}}

To change the rate, change the value of a FireRate var.

If you have questions, feel free to ask.

~~Link to project –> Google Drive~~

---
It's a mirror from [WebArchive](https://web.archive.org/web/20190401030238/http://iryos-workshop.com/en/joystick-firing-ue4/)