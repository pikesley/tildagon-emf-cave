# EMF Cave

A reimplementation of an [ancient Palm Pilot game](https://palmdb.net/app/sfcave)

Any button _except_ `CANCEL` (`F`) to elevate the ship

> Note: pushing more than one button at once causes mayhem

Tilt the badge north, south, east or west to select a different number base for the scores

## Install it

It's on the [app store](https://apps.badge.emfcamp.org/) as "EMF Cave". Or,

## Install from your laptop

You need [`mpremote`](https://docs.micropython.org/en/latest/reference/mpremote.html), then:

```bash
make mkdir
make deploy
```

Wait while it pushes the code to the badge, then `ctrl-d`, the badge will reboot and you should see a new app called `EMF Cave`.
