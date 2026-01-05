# chris simulator

Build container using

```bash
docker build -t renpy-game .
```

Will take around 2-3 minutes.

Run using

```bash
docker run --rm -it \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  renpy-game
```
