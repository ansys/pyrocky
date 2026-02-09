FROM rockylinux/rockylinux:8.10

# Add metadata
LABEL description="Ansys FreeFlow 2026 R1"

# Set environment variables
ENV INSTALL_DIR=/ansys_inc/v261
ENV AWP_ROOT261=$INSTALL_DIR
ENV LD_LIBRARY_PATH=$INSTALL_DIR/freeflow/bin/lib

# Install runtime dependencies
RUN dnf install -y \
    libgomp \
    expat \
    openssl-libs \
    libxml2 \
    zlib \
    libffi \
    freetype \
    libpng \
    fontconfig \
    cairo \
    pango \
    libglvnd-glx \
    libglvnd-opengl \
    libXrender \
    libX11 \
    libXcursor \
    libglvnd \
    && dnf clean all

# Create a non-root user
RUN useradd -m -s /bin/bash freeflow

# Copy the contents of the build context directory to the image.
COPY --chown=freeflow:freeflow freeflow/ $INSTALL_DIR/freeflow
COPY --chown=freeflow:freeflow licensingclient/ $INSTALL_DIR/licensingclient

# Switch to non-root user
USER freeflow

# Set working directory
WORKDIR /Projects

# Run Freeflow
ENTRYPOINT ["/ansys_inc/v261/freeflow/bin/FreeFlow"]