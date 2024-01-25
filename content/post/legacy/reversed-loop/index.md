---
title: Reversed Loops in UE4
summary: Archived tutorial for UnrealEngine 4
date: 2016-05-23
authors:
  - admin
tags:
  - Legacy
  - UnrealEngine4
  - Utility
---


Hi-hi!
In previous post I showed how to add Delay support in loops. In this we’ll go further and will add reverse mode to ForLoop and ForEachLoop.

As I wrote [here](/post/legacy/forloop-withdelay), we create any loop, double click on it and UE4 opens **StandartMacros** blueprint.
Then, copy everything inside EventGraph and paste it into Macro inside your blueprint.

***Keep in mind**, that modified loop, works only inside blueprint, where its created.*

Settings for **ForLoop**:

{{< figure src="reverseLoops1.png" caption="Replaced condition from “<=” to “>=” and instead “+1” set “-1″" >}}

{{< figure src="reverseLoops2.png" caption="Named as ReversedForLoop" >}}

And now **ForEachLoop**:

{{< figure src="reverseLoops3.png" caption="We use **ForLoop** inside of it, it means, that we can **replace** it with [ForLoopWithDelay](/post/legacy/forloop-withdelay/)" >}}

{{< figure src="reverseLoops4.png" caption="ReversedForEachLoop" >}}
