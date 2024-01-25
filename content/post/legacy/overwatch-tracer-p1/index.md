---
title: Overwatch Tracer's blink ability in UE4, p.1
summary: Archived tutorial for UnrealEngine 4 of Tracers's blink ability, p.1
date: 2016-06-01
authors:
  - admin
tags:
  - Legacy
  - Overwatch
  - UnrealEngine4
---

### Prologue

Overwatch released. I was not interested in this game until OBT. I heard about it in 2015 and I saw comments like “Another TF2 killer”, “Blizzard attacks to Valve”, etc. Then hype with Tracer’s pose, it didn’t a reason to interest game. But OBT changed my mind. This game is AWESOME and FUN to PLAY. I couldn’t stop playing after 10th match. Overwatch isn’t a breakthrough in CG, not a new gameplay mechanics or anything else, it’s 100% GAME. [There must be](https://dictionary.cambridge.org/dictionary/english/game) a screenshot from Overwatch.

Recommend to play, who plays UTournament.

### Blueprints

{{< youtube id="u79msvio8lI" >}}

Tutorial based on **FirstPersonTemplate**. UE4 version is **4.11.2**.

How it works according to Wiki:

{{< figure src="wiki.png" >}}

In first, we need to create a few variables in FirstPersonCharacter:

{{< figure src="tracerFirst1.png" >}}

- Float “Range” – blink’s range.
- Vector “Direction” – calculated direction, where she is moving.
- Integer “BlinksCount” – charges, equal 3.
- Integer “MaxBlinksCount” – max charges, too 3.

Next, in case when Tracer is moving, blink direction depends on WASD, we assign a calculated value to “**Direction**” in EventGraph/MovementInput.

{{< figure src="tracerFirst5.png" >}}

First two multiplications determine the direction(left, forward …); then adds it(right-forward, left-back…); multiply by Range( blink’s range); add resulting with character’s location coordinates and assign to **Direction**.

Create a few functions:

{{< figure src="tracerFirst1.1.png" >}}

- CanBlink? – check current charges.
- ReloadingBlink – reloading charges.
- Decrement – minus one charge.
- Moving – blink, when Character is moving.
- NoMoving – when standing still.

CanBlink?:

{{< figure src="tracerFirst2.png" >}}

ReloadingBlink:

{{< figure src="tracerFirst3.png" >}}

Decrement:

{{< figure src="tracerFirst4.png" >}}

Moving:

{{< figure src="tracerFirst4.png" caption="Teleport function integrated in Editor" class="image-caption" >}}

Shoot line-trace(**LineTraceByChannel**), that starts from character’s location(**GetActorLocation**) and ends at **Direction** value. Use **Branch** to check if line-trace hits, if true DestLocation of function Teleport is “Location” from HitResult, if False DestLocation is TraceEnd.

Moving

{{< figure src="upd2.png" >}}

Same as **Moving**-function, but instead **Direction** var, calculate end of trace-line.

Now composing all function in Event Graph:

{{< figure src="tracerFirst9.png" >}}

Ability activates by pressing LeftShift. Function **CanBlink?** checks charges count, if greater than 0, **Decrement** reduces by one, then call function **SetTimerByFunctionName**, that calls **Reloading**-func every 3.5 seconds and before teleport, checks if character is moving.

### Second skill and VFXs

Check [second ability here](/post/legacy/overwatch-tracer-p2/)