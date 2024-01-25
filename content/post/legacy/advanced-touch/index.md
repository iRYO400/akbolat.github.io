---
title: Advanced Touch in UnrealEngine4 (Swipe, Double Tap…)
summary: Archived tutorial for UnrealEngine 4
date: 2016-05-10
authors:
  - admin
tags:
  - Legacy
  - UnrealEngine4
  - Control
---

### Overview

Hey there!

In this post I would like to share with you with plugin that extends functionality of mobile UE4.
This plugin includes implementation of Swipe, Double Tap and Single Tap.
P.S. I’m not an author of it.

Link to download –> [Github](https://github.com/getsetgames/Swipe)

{{< figure src="swipe1.png" >}}

Works on **4.9**, **4.10**, **4.11** versions of UE4.

### Installing

In first, make sure that you’ve installed **Visual Studio 2015**. Then download an archive from the link above

Now in your project. If you use only Blueprints. You need to create an empty C++ class.

To do that, go to **File** and click **New C++ class…**

{{< figure src="swipe2.png" >}}

There select **None** and click **Next**

{{< figure src="swipe3.png" >}}

Then **Create Class**

{{< figure src="swipe4.png" >}}

It will take some time, after that Visual Studio will be opened. When it done compiling close it and project.

{{< figure src="swipe5.gif" >}}

Now find where your project is placed. In project folder create a new folder “**Plugins**” and move there **Swipe-master** folder from archive. Rename Swipe-master to **Swipe**.

Open project. And it will ask you next:

{{< figure src="swipe5.png" >}}

Click **Yes**. It will take a while.

Open **Project Settings**, on the left side find **General Settings**. Then change value of **Game Viewport Client Class** to **SwipeViewportClass** inside **Default Classes**.

{{< figure src="swipe6.png" >}}

We’ve done installing.

### Using

To use Swipe, Tap, etc. nodes you need add Swipe component, in Components panel inside your Blueprint.

{{< figure src="swipe7.png" >}}

In MyBlueprint panel select Swipe and in Details panel you’ll be able to use event-nodes.

{{< figure src="swipe8.png" >}}

Some of events have 2d Vector(Start Location, Trigger Location, End Location) and Integer(Handle) parameters.

{{< figure src="swipe9.png" >}}

Also you can configure Swipe sensitivity.

{{< figure src="swipe10.png" >}}

That’s all. If you have a question, feel free to ask!

Thanks!

---
It's a mirror from [WebArchive](https://web.archive.org/web/20190330205258/http://iryos-workshop.com/en/swipe-ue4/)