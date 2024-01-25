---
title: Overwatch Winston’s “TESLA” gun in UE4
summary: Archived tutorial for UnrealEngine 4 of Winston's weapon from Overwatch
date: 2016-07-10
authors:
  - admin
tags:
  - Legacy
  - Overwatch
  - UnrealEngine4
---
Hi everyone!

3 weeks have passed since I made last tutorial, a little distracted on developing Android stuff, it’s ok, I’ll catch up.
And today we’ll build with blueprints the Winston’s **TESLA** gun, result is below

{{< youtube id="HF2VEFH_tf0" >}}

What I found in [the official wiki](https://overwatch.wikia.com/wiki/Winston):

{{< figure src="1.1.png" >}}

In addition, the gun can shoot at multiple targets simultaneously.

So an algorithm will be next, when player press LMB we create MultiSphere(to aim at multiple targets) in the front of the character, btw, we used it in the [previous tutorial](/post/). Since it’s “multi”, it stores overlapped objects to an array and that array we transfer to our. Then we “play” two cases of shooting, first is when barrages are aimed to an enemy(here we use our array) and second is when barrage shots are in idle.

Tutorial based on **FirstPersonTemplate**, UE4 version **4.12.4**,

#### Let’s start with blueprints
Open **FirstPersonCharacter** blueprint, where implemented character control. And create next variable:

(Float) **FireRate** – fire rate with value equal to **0,1**. Less means faster.
(Float) **SpreadRadius** – spread distance for electric barrage, or rather half of it, below will explain. Equal to 300.
An array (EObjectTypeQuery) **Objects** – here we store type of actors, those will be trigger MultiSphereTrace. Currently we need only one type – **Pawn**.
An array (Actor) **ActorsUnderAttack**  – an array of actors, which will take a damage by electric barrage.
(Name) **Muzzle** – is a name of bone, that placed in the weapon’s muzzle. Value is “Muzzle”

{{< figure src="2.png" >}}

 - (ParticleSystem) **ParticleMjollnir** – particle for the weapon.

Result is

{{< figure src="3.png" >}}

There is an event **InputActionFire**, that implements shooting logic in the EventGraph. We need it in this tutorial, so take it and put to another place.

In first, I would like to highlight a special block of nodes:

{{< figure src="4.png" caption="Continuous shooting by pressing button" >}}

Here we define start and end coordinates for Multi-Sphere. It creates in front of the character at distance defined by **SpreadRadius** var. The Trace-function(LineTrace, SphereTrace, etc.) will not work, if it has the same start and end coordinates, therefore we add +1

{{< figure src="5.png" >}}

Then we create the Multi-Sphere, it have inputs such as Start/End, the radius of the sphere and the array of object types, and in the output the **BreakHitResult** array, elements of which we transfer to the our array **ActorUnderAttack** by using **ForEachLoop** and **AddUnique**. AddUniqie is to exclude the case, when several electric barrages aim to a single enemy. At the of ForEachLoop call custom events.

{{< figure src="6.png" >}}

The whole scene looks like

{{< figure src="7.png" >}}

Now let’s look at the first case, when electric barrages are aimed:

{{< figure src="8.png" >}}

In first, we iterate through the **ActorUnderAttack** array, in second call **SpawnEmitterAttached** function(it creates a particle attached to component, bone and to specific coordinates), which receives to the input the particle(**ParticleMjollnir** var), **Sphere** component(placed in the Components panel) and bone’s name( **Muzzle** var). Note, **LocationType** must be ***KeepWorldPosition***. Then to define a target for electric barrage we call **SetBeamTargetPoint** function. At the end of loop clear the array.

The second case is when the shots are in idle

{{< figure src="9.1.png" caption="LocationType KeepWorldPosition">}}

Here we use **LineTraceByChannel**, to make particles react on collision. To simulate chaotic electric barrages use **RandomUnitVectorInConeWithYawAndPitch**. The we create the particles(**SpawnEmitterAttached**). And the target point defines in two cases, first is when trace-line overlapped and second, opposite to the first(End of trace-line).

At this point most of the work with blueprint has been done for 98%, now let’s get to modify particles.

#### Beam Particles

To save our time we’ll use ready-to-use particles with some modifications.

There is a map named **Effects** in the [Content Example](https://docs.unrealengine.com/latest/INT/Resources/ContentExamples/). In the corner of this map placed particle **Beam emitter with a noise module**(under 2.8). Find it in the Content Browser, right click on it –>> Asset Actions –>> Migrate… Click OK, and specify the Content folder in your project.

These particles contain two emitters, we don’t need in the second, so remove it(light_flickering). Then in the **“beam”** emitter set up next:

- In **Beam Data** – set up **InterpolationPoints** equal to “10”, to make electric barrages a bit curved.
- In **Required** – the duration of the particles – **EmitterDuration** = “0,1”. Number of loops – EmitterLoops = “1”. “0” means endless.
- In **Spawn** – spawn rate – **Rate** = “7”.
- **Lifetime** – equal to “0.01”.
- **InitialSize** – size of the particles, equal to {20;0;0}.
- **InitialColor** – color of the particles – **StartColor**, transparency of the particles – **StartAlpha** equal to”0.1″, to not be blinded.
- **Source** – the source of the particles. Method of the source – **SourceMethod** – set as **Emitter**, to attach the particles to their initial position. Then **SourceTangentMethod** set **UserSet**, to make curved particles. **SourceTangent** equal to {0;0:25}.
- **Target** – target point of the particles. As you remember we called the function SetBeamTargetPoint, i.e. independently defined the target point, therefore to make it work , set up **TargetMethod** as **UserSet**.
- **Noise** – change **NoiseRangeScale** to “1”, **NoiseLockTime** equal to “0.01” and **NoiseTessellation** = “1”.

In the preview you’ll see next

{{< figure src="1.gif" >}}

Save it, and define it in our **ParticleMjollnir** variable.

That’s all. Thank for reading!


---
It's a mirror from [WebArchive Source](https://web.archive.org/web/20180909033840/http://iryos-workshop.com/en/overwatch-winstons-gun)
