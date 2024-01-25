---
title: Overwatch Tracer's blink ability in UE4, p.2
summary: Archived tutorial for UnrealEngine 4 of Tracers's blink ability, p.2
date: 2016-06-12
authors:
  - admin
tags:
  - Legacy
  - Overwatch
  - UnrealEngine4
---

We’ve done with first ability in the [previous post](/post/legacy/overwatch-tracer-p1), now let’s take a look at second.

### Blueprints

{{< figure src="abilityTracer14.png" caption="Instead of 3 seconds, I made 5([Wiki](https://overwatch.wikia.com/wiki/Tracer))">}}

In this tutorial we’ll return only our position. Ammo and health are the same.

First we need variables.

{{< figure src="abilityTracer1,1.png" >}}

1. Integer **BacktrackCount** – current number of “jumps”. Equal 1.
2. Integer **MaxBacktrackCount** – maximum number. Too equal 1.
3. Array Transform **Positions** – an array, where we’ll store out Location, Rotation and Scale( it doesn’t need in this case).

{{< figure src="abilityTracer1.png" >}}

And functions:
- **CanBacktrack?** – check, if it’s available.

{{< figure src="abilityTracer1.1.png" >}}

- **DecrementBacktrack**

{{< figure src="abilityTracer1.2.png" >}}

- **ReloadingBack**

{{< figure src="abilityTracer1.3.png" >}}

Tracer can use second ability at any time, except when it’s reloading, it means that we need to store Character’s location and rotation every miliseconds.

{{< figure src="abilityTracer2.png" >}}

For this purpose instead of **EventTick**, make following trick – **BeginPlay**, **Sequence** and **Delay**.
These triple nodes the same as EventTick, but we can control its triggering(Delay’s param called **Duration**), set it equal **0.04**.
So the picture above means, that we call a sequence of nodes every 0.04 seconds – store Character’s Vector coords (**GetActorLocation**)
and Rotator coords(**GetControlRotation**) to our array **Positions**.
Then check count of elements in array, if it’s more that **125**(I wrote below), we remove an element at 0 index.
When it removes other elements shifts to “-1” position, i.e. element at 1 index shifts to 0; at 2 shifts to 1, etc.

Why did I take 125 in condition?
Because these nodes triggers every 0.04 seconds and in 1.0 second it can write 25 values to array.
Therefore 125 values in 5 seconds.

Now bind all logic to **E** key.

{{< figure src="abilityTracer3FULL.png" >}}

In first, check condition **CanBacktrack?**, if True decrement charges **DecrementBacktrack**,
then set timer to call **ReloadingBacktrack** function with 8 sec Loop.
Second we extract stored values from custom Loop, every element disassemble via BreakTransform to Location/Rotation
and connect it to **SetActorLocation**/**SetControlRotation**. Third clear an array.

There is custom Loop, that supports Delay and iterates in reverse order.
More about it you can read [here](post/legacy/forloop-withdelay/) and [here](post/legacy/reversed-loop/). How it looks inside:

{{< figure src="abilityTracer5.png" >}}

At this point, you’ve done with Second Ability.

### Visual FX.
To make it a bit similar as in Overwatch, will add HUD with charges for first skill and effect with **PostProcess** for second skill.

#### Blink

Create a **Widget Blueprint**, name it as **WD_Blink**:

{{< figure src="abilityTracer9.png" >}}

Open it and create three **Image** widget at the center

{{< figure src="abilityTracer10.png" >}}

In Details/Appearance, ***for each of widget(starting from the top)***,
on line **Color and Opacity** open drop-down menu **Bind** and click **Create Binding**.

{{< figure src="abilityTracer11.png" caption="To be sure, that each of widgets set at the center, place it Anchor to the center too" >}}

Once you click CreateBinding, will opened usual EventGraph and functions named **GetColorAndOpacity_0**

For each of function make next logic with some difference

{{< figure src="abilityTracer12.png" caption="Green mark for each function" >}}

To attach widget, open **FirstPersonHUD**(Blueprints folder) and add next:

{{< figure src="abilityTracer13.png" >}}

Set WD_Blink in **Class** param.

#### Backtrack

Open **Viewport** and add PostProcess in Components:

{{< figure src="abilityTracer6.png" >}}

In Details, set settings as in the picture in **PostProcessVolume** tab

{{< figure src="abilityTracer7.png" caption="Click to open pic. There is **checkbox Enabled** – make it **unchecked**">}}

Place PostProcess to EventGraph and set its boolean SetEnabled in two places:

{{< figure src="abilityTracer8.png" caption="After **SetTimerByFunctionName** and Clear. Look at checkboxes">}}

Now test it. Cheers!

{{< youtube id="u79msvio8lI" >}}

---
It's a mirror from [WebArchive](https://web.archive.org/web/20190314001105/http://iryos-workshop.com/en/overwatch-tracer-skills-p2-ue4//)