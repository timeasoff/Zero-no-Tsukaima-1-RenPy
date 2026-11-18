FROM python:3.14-slim-bookworm

ARG OPENCODE_VERSION=2.0.20
ARG RENPY_VERSION=8.5.2

ENV RENPY_HOME=/opt/renpy \
    LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    PYTHONUTF8=1 \
    PYTHONIOENCODING=utf-8 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

# System dependencies. HTTPS + retries make apt more resilient to transient
# connection failures when Debian mirrors are temporarily unavailable.
RUN sed -i 's|http://deb.debian.org|https://deb.debian.org|g' \
    /etc/apt/sources.list.d/debian.sources \
    && apt-get -o Acquire::Retries=5 \
    -o Acquire::https::Timeout=30 \
    update \
    && apt-get -o Acquire::Retries=5 \
    -o Acquire::https::Timeout=30 \
    install -y --no-install-recommends \
    ca-certificates \
    curl \
    bzip2 \
    git \
    ffmpeg \
    webp \
    ripgrep \
    xvfb \
    xauth \
    libgl1 \
    libglib2.0-0 \
    libx11-6 \
    libxext6 \
    libxrender1 \
    libxi6 \
    libxrandr2 \
    libxcursor1 \
    libxinerama1 \
    libxxf86vm1 \
    libasound2 \
    && rm -rf /var/lib/apt/lists/*

# Ren'Py SDK. bzip2 above is required by tar to unpack the .tar.bz2 archive.
RUN mkdir -p "${RENPY_HOME}" \
    && curl -fsSL \
    "https://www.renpy.org/dl/${RENPY_VERSION}/renpy-${RENPY_VERSION}-sdk.tar.bz2" \
    -o /tmp/renpy.tar.bz2 \
    && tar -xjf /tmp/renpy.tar.bz2 \
    --strip-components=1 \
    -C "${RENPY_HOME}" \
    && rm /tmp/renpy.tar.bz2 \
    && chmod +x "${RENPY_HOME}/renpy.sh"

ENV PATH="${RENPY_HOME}:${PATH}"

# Run Ren'Py in a virtual X display; the container does not need a desktop GUI.
RUN printf '%s\n' \
      '#!/bin/sh' \
      '# Headless RenPy SDK wrapper (devcontainer). See AGENTS.md, GUI SDK.' \
      '# Xvfb display + dummy audio; script errors exit with traceback.txt' \
      '# (RENPY_SIMPLE_EXCEPTIONS) instead of the interactive error screen,' \
      '# which waits for input forever under Xvfb; stdin from /dev/null;' \
      '# no-op editor (RENPY_EDIT_PY) so error reporting skips xdg-open.' \
      'exec xvfb-run -a env SDL_AUDIODRIVER=dummy RENPY_SIMPLE_EXCEPTIONS=1 RENPY_EDIT_PY=/workspace/tools/renpy_noop_editor.py /opt/renpy/renpy.sh "$@" </dev/null' \
    > /usr/local/bin/renpy \
    && chmod +x /usr/local/bin/renpy

# Python helper used by tools/convert_voices_soundfile.py.
RUN pip install --no-cache-dir soundfile

# Install the pinned OpenCode version. curl is installed in the system
# dependencies above.
RUN curl -fsSL https://opencode.ai/v2/install \
    | bash -s -- --version "${OPENCODE_VERSION}" --no-modify-path \
    && ln -s /root/.opencode/bin/opencode /usr/local/bin/opencode

# Fail the image build if a required tool is missing or cannot start.
RUN git --version \
    && ffmpeg -version | head -n 1 \
    && cwebp -version \
    && rg --version | head -n 1 \
    && python -c "import soundfile; print('soundfile', soundfile.__version__)" \
    && renpy --version \
    && opencode --version

# Keep the container alive and run the OpenCode server on port 4097.
CMD ["sh", "-c", "mkdir -p /workspace/.tmp && opencode serve --hostname 0.0.0.0 --port 4097 > /workspace/.tmp/oc-serve.log 2>&1 & exec sleep infinity"]
