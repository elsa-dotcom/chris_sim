FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3 \
    python3-dev \
    python3-pip \
    libx11-6 \
    libxext6 \
    libxrender1 \
    libxtst6 \
    libxi6 \
    libxrandr2 \
    libxcursor1 \
    libxinerama1 \
    libgl1-mesa-dri \
    libgl1-mesa-glx \
    libsdl2-2.0-0 \
    libsdl2-image-2.0-0 \
    libsdl2-mixer-2.0-0 \
    libsdl2-ttf-2.0-0 \
    alsa-utils \
    ca-certificates \
    bzip2 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt

# Copy Ren'Py SDK
COPY renpy /opt/renpy

# Copy your game
COPY game /opt/game

ENV SDL_VIDEODRIVER=x11
ENV SDL_RENDER_DRIVER=software
ENV LIBGL_ALWAYS_SOFTWARE=1
ENV RENPY_GL_DISABLE=1
ENV SDL_AUDIODRIVER=dummy

WORKDIR /opt/renpy

CMD ["./renpy.sh", "/opt/game"]
