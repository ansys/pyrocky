FROM rockylinux/rockylinux:8.10

# Add metadata
LABEL description="Ansys Rocky 2026 R1"

# Set environment variables
ENV INSTALL_DIR=/ansys_inc/v261
ENV AWP_ROOT261=$INSTALL_DIR
ENV LD_LIBRARY_PATH=$INSTALL_DIR/rocky/bin/lib

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
RUN useradd -m -s /bin/bash rocky

# Copy the contents of the build context directory to the image.
COPY --chown=rocky:rocky rocky/ $INSTALL_DIR/rocky
COPY --chown=rocky:rocky licensingclient/ $INSTALL_DIR/licensingclient

# Switch to non-root user
USER rocky

# Set working directory
WORKDIR /Projects

# Run Rocky
ENTRYPOINT ["/ansys_inc/v261/rocky/bin/Rocky"]