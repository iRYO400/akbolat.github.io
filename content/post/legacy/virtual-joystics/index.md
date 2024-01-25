---
title: Virtual Joysticks in Unreal Engine 4/ UE4
summary: Archived tutorial for UnrealEngine 4
date: 2016-05-15
authors:
  - admin
tags:
  - Legacy
  - UnrealEngine4
  - Control
---

Hi folks!

In this post I will cover about a built-in element in Unreal Engine 4 – Virtual Joysticks, sticks or analogs. In particular how to configure them and how to interact with via Blueprints.

### Beginning

We can create Virtual Joysticks via Content Browser:

{{< figure src="joystick1.png" >}}

Or use default from Engine’s content. To use it, need open **View Options** at the bottom right of Content Browser. And check Show **Engine Content**. After that two folders will appear in CB **Engine Content** and **Engine Content C++**.

{{< figure src="joystick3-3.png" >}}

In path EngineContent/MobileResourсes/HUD we’ll find **DefaultVirtualJoysticks**. Explanation for other settings below based on default joysticks.

### Setting up

When you open it, you’ll see next:

{{< figure src="joystick4.1.png" >}}

Let’s start with “external” parametrs:

1. Active Opacity – joysticks’ opacity, when it active. From 0.0 to 1.0.
2. Inactive Opacity – opacity, when it inactive. From 0.0 to 1.0.
3. Time Until Deactive – time until it deactivates. Measures in seconds.
4. Time Until Reset – time until joystick returns to initial positions. Measures in seconds. When 0.0 it’s disabled.
5. Activation Delay – delay before using it. Looks like lagging effect, annoying even  when 0.1. Measures in seconds. When 0.0 it’s disabled.
6. Prevent Recenter – binds it to initial position. Firts gif checked, second unchecked.

{{< figure src="joystick5.gif" >}}

{{< figure src="joystick6.gif.gif" >}}

7. Startup Delay – delay before draw it on screen. In seconds.

Now let’s take a look to “internal” settings. By default there are 2 analogs, 0-element is for left, 1-element is for right stick. Btw, UE4 doesn’t have a limit.

{{< figure src="joystick5.png" >}}

They’re both has the same settings. So we’ll look only at 0-element.

{{< figure src="joystick6.png" >}}

1. Image 1 – inner circle.
2. Image 2 – an external.
3. Center – location coordinates. If <= 1.0, it’s relative to screen. It means I.e. 0.0 – for X is left edge of screen, for Y is top; 1.0 – for X is right edge, for Y is bottom. If > 1.0, it’s absolute to screen, i.e. 135 means shifted by 135 pixels.(Not recommended for mobiles).
4. Visual Size – size of external circle.
5. Thumb Size – size of inner.
6. Interaction Size – area of interaction.
7. Input Scale – max value, when it shifts.
8. Main Input Key – “action”, which is responsible for horizontal shifting.
9. Alt Input Key – “action”, which is responsible for vertical shifting.

### Turn on/off

To turn on sticks, we need to identify them in Project Settings.

Project Settings –> Input –> Mobile –> Default Touch Interface.

{{< figure src="joystick7.1.png" >}}

So it will be always visible. To turn on/off in-game UE4 gives function SetVirtualJoystickVisibility. Look at the blueprint example below, by pressing Tab it turns on/off.

{{< figure src="joystick8.png" >}}

That’s all. Feel free to ask questions.

Thanks for your attention!

---
It's a mirror from [WebArchive](https://web.archive.org/web/20190402201311/http://iryos-workshop.com/en/virtual-joysticks-in-ue4)