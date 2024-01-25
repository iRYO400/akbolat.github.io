---
title: ForLoop with Delay in UE4
summary: Archived tutorial for UnrealEngine 4
date: 2016-05-22
authors:
  - admin
tags:
  - Legacy
  - UnrealEngine4
  - Utility
---

### Overview 
Hi-hi!

If you tried to use loop with Delay node, you know that Delay doesn’t work.
Or if you didn’t, in example below, instead of printing with 1 second delay, PrintString prints immediately.

{{< figure src="forLoopDelay.png" >}}

{{< figure src="gif2.gif" >}}

### How to “fix”

I’ll show how to “fix” it for ForLoop.
In your blueprint where you need modified loop, create a ForLoop.
Then open it by double click on it. UE4 will open another blueprint, named StandartMacros.
Inside of it, you’ll see next:

{{< figure src="forLoopDelay2.png" caption="ForLoop's mechanism" >}}

Now open again your blueprint and create a new Macro with **ForLoopWithDelay** name.

{{< figure src="forLoopDelay3.png" >}}

Copy and set all the same, as in the original ForLoop from StandartMacros to your Macro. Then, most important, add **Delay** and connect its Duration param to Inputs, as in the pic below:

{{< figure src="forLoopDelay5.png" >}}

At this point you’ve done with modifing ForLoop. Let’s change the logic that was in beginning.

{{< figure src="forLoopDelay6.png" >}}

{{< figure src="gi1.gif" >}}

**Keep in mind**, that modified loop, works only inside blueprint, where its created.

Similarly with other loops. In StandartMacros you can find other loops. Copy them, create Macro and add Delay.

For example, While loop:

{{< figure src="forLoopDelay7.png" >}}

---
It's a mirror from [WebArchive](https://web.archive.org/web/20190402122855/http://iryos-workshop.com/en/forloop-withdelay-ue4/)