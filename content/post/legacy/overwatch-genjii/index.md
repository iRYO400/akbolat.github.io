---
title: Overwatch Genji’s Ability in UE4
summary: Archived tutorial for UnrealEngine 4 of Genjii's deflect ability
date: 2016-06-16
authors:
  - admin
tags:
  - Legacy
  - Overwatch
  - UnrealEngine4
---

The next ability that I love in Overwatch is Genji’s Deflect, that can deflect everything in game, that wants kill you 🙂

Before we start, we need take a look at bullet types. I’ll be brief.

### Projectile vs. Instant hit.

Almost all games use two bullet types – **Projectile** and **InstantHit**. Difference between them is that first supports gravitation, velocity, direction of the wind, i.e. as in the real life, but it make its expensive from performance point of view, especially in Online games. In main case, Projectiles – are rockets, grenades, arrows, etc. IstantHit, or also named as TraceHit, is just a LineTrace, that doesn’t supports gravity, velocity, etc. It strictly shoots from muzzle of weapon. It uses, for example, in CS, CoD games. 

There is a video on YouTube, that shows What Genji can and can’t DEFLECT.

{{< youtube id="e20-xxjGTK4" >}}

### Logic

Editor version **4.11.2**.
Tutorial based on **FirstPersonTemplate**.

How did I implement it? By activation ability, we create a flat box collision in front of character, and when Projectile or IstantHit(Line-Trace) hit that box collision, we define it, then if it was Projectile spawn it, or if it was InstantHit shoot LineTrace. I’m not sure about InstantHit logic, but it works well. If you have any ideas, tell us in the comments.

Open **FirstPersonCharacter -> Viewport**, add **BoxCollision** and bind it to **FirstPersonCamera** with next Location and Scale settings. Then set **Projectile** in Collision Presets, it’ll make BoxCollision react only to projectiles.

{{< figure src="genjiiAbil1.png" title="" >}}

You should get the following:

{{< figure src="genjiiAbil2.png" title="" >}}

Let’s start with Projectile. Open EventGraph and create **OnComponentHit** event, select **BoxCollision**, in the Details/Events panel click at “+” near **OnComponentHit**. Then make the following:

{{< figure src="genjiiAbil3,1.png" title="" >}}

 **OnComponentHit** – event, that activates, when BoxCollision has been hit. Its parameter – **OtherActor**, gives an info about actor that hit BoxCollision. We convert(**GetClass**) and Spawn(SpawnActor) it with new Location and Rotation values in the direction of sight.

Now InstantHit. Create a custom event and name it – DeflectTrace:

### image 4

{{< figure src="genjiiAbil4.png" title="Multiplying by 2000, it’s the length of the trace-line. 1 unit = 1 cm." >}}

DeflectTrace shoots **LineTraceByChannel**, in Start parameter gets BoxCollision’s location coordinates, in End parameter gets coordinates of straight forward Vector(**GetForwardVector**) summed with BoxCollision’s.

### Test bot

To simulate shots in the scene, we’ll create a bot, that shoots Projectile and InstantHit. Create new Actor Blueprint, name it **AutoShootingMachine**. In the Components panel add mesh, for example Sphere, and Arrow for navigation. Turn off Sphere’s collision(Look at picture).

Place it to the scene.

{{< figure src="genjiiAbil5.png" title="Shoots in Arrow’s direction" >}}

In EventGraph, create an alternative **EventTick**,

{{< figure src="genjiiAbil6.png" title="" >}}

Sequence-**Then 1** – shoots LineTrace

{{< figure src="genjiiAbil7.1.png" title="I’m not sure about this implementation, but it works" >}}

  LineTrace with random End-coordinates. If it hits anything, we cast to FirstPersonCharacter and if cast was successful call custom event DeflectTrace.

Sequence-**Then 2** – spawns Projectile

{{< figure src="genjiiAbil8.png" title="Set FirstPersonProjectile in Class parameter" >}}

And the last thing, open **FirstPersonProjectile**

{{< figure src="genjiiAbil9.png" title="" >}}

Add **DestroyActor** to False(Branch).

That’s all implementation. Next are binding and cooldown.

### Binding to Key

In FirstPersonCharacter, create boolean **isDeflectAvailable** and function **Reloading**:

{{< figure src="genjiiAbil11.png" title="" >}}

At the beginning of the game, we’ll turn off collision

{{< figure src="genjiiAbil10.1.png" title="New Response = Ignore" >}}

And when we press “**E**“, ability activates for two seconds(New Response = **Block**), then it turns off for 16 seconds until it reloads(**SetTimerByFunctionName**) as in the original game.

{{< figure src="genjiiAbil12.2.png" >}}

In result you’ll get:

{{< youtube id="jNS9vZpTU8A" >}}

---
It's a mirror from [WebArchive](https://web.archive.org/web/20190314001105/http://iryos-workshop.com/en/genjiis-ability/)