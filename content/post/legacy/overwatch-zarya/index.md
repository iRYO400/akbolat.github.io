---
title: Overwatch Zarya’s Ultimate in UE4
summary: Archived tutorial for UnrealEngine 4 of Zarya's ultimate  
date: 2016-07-04
authors:
  - admin
tags:
  - Legacy
  - Overwatch
  - UnrealEngine4
---

Hi everyone!

Welcome to another tutorial about abilities of Overwatch heroes, in this we will make [Zarya’s ultimate](https://overwatch.wikia.com/wiki/Zarya).

### image

Tutorial based on **FirstPersonTemplate**.
UE4 version **4.12.3**

### Logic

Her ultimate, as written above is Graviton Surge(or Bomb), as we know from previous tutorial, bombs are [Projectile](/post/legacy/overwatch-genjii). So instead of creating new Blueprint, we’ll just duplicate existing, in this template FirstPersonProjectile, and name it **UltimateProjectile**.

{{< figure src="2.png" width="50%" height="50%" >}}

In short, we launch gravi-bomb, when it hits to anything we create Sphere-Trace, everything that is inside of sphere is written to the array, and every element of array we move to center of sphere.

Open UltimateProjectile, in Components select **Projectile**(or Projectile Movement), in Details/Projectile Bounces uncheck **Should Bounce**. Now let’s create blueprints.

In EventGraph delete all nodes, except **EventHit** and create a custom event ***Blackhole***.

Create variables:
- boolean **isHit?** – collision test,
- Vector **Height** – is height at which Blackhole spawns. Equal *{0;0;100}*
- Array Actor **ActorsInBlackhole** – actors, that will be "pulled".

### image 3

Gravi-bomb explodes in two cases,

- first(starts from BeginPlay), if there was no collision, is set life span for 3 seconds, then it immediately blows up.
- second(from EventHit), if collision triggered, we set isHit to True, increase scale(**SetRelativeScale**) and lift(**SetWorldLocation**)the bomb. Then, create Trace-sphere(**MultiSphereTraceByChannel**) with parameters – Start(coordinates of that blueprint – **GetActorLocation**); End( same as **Start + 1**, else it wouldn’t work), Radius(750 units) and **Draw Debug Type**(**ForDuration**). Results of Trace-sphere we write to an array **ActorsInBlackhole** using **ForEachLoop**. At the end of loop, we call Blackhole custom event.
Now let’s implement Blackhole event:

### image 5

There is we use **Sequence**, to call to **Timelines**. First is for moving objects to the center of Blackhole. We iterate an array, for every element set new coordinates(**SetActorLocation**). And second, to make circle around the center, instead of straight.

### Timelines

If you don’t know what is it Timeline, just google it or watch [YouTube](https://www.youtube.com/results?search_query=timeline+unreal+engine+4).
Then, prepare two timelines:

{{< figure src="6-2.png" title="First Timeline with Float graph">}}
{{< figure src="7-2.png" title="Second with Vector graph">}}

That’s all the logic. Now will add some cosmetics stuff. Use **M_BlackHole_Fresnel** material for sphere in UltimateProjectile blueprint, to distinguish gravi-bomb. Link to [download](https://www.dropbox.com/s/sbo40m3z703irb6/BlackHole.zip)([Source](https://www.youtube.com/watch?v=IkmDdL7b-4I), and look at comment below, written by [Yoeri -Luos- Vleer](https://www.youtube.com/user/vladderbeest))

{{< figure src="8-2.png" >}}

The last thing is binding ability to **Q** key button. In **FirstPersonCharacter** blueprint:

{{< figure src="9-1.png" title="In SpawnActor/Class set UltimateProjectile">}}

### Result
{{< youtube id="ZReOkcAClAo" >}}