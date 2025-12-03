# Copyright (C) 2023 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

""".. _ref_minimal:

Simple particle simulation
--------------------------
This example sets up and solves a simple particle simulation workflow.

"""

###############################################################################
# Perform imports and create a project
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Perform the required imports and create an empty project.

import os.path
import tempfile

import ansys.rocky.core as pyrocky

# Temporarily pin to v252 because next version is failing on Pyro connection
ROCKY_VERSION = 252

# Create a temp directory to save the project.
project_dir = tempfile.mkdtemp(prefix="pyrocky_")

# Launch Rocky and open a project.
rocky = pyrocky.launch_rocky(rocky_version=ROCKY_VERSION)
project = rocky.api.CreateProject()

###############################################################################
# Configure the study
# ~~~~~~~~~~~~~~~~~~~
# Create a particle entity and then inject it through a circular surface.

study = project.GetStudy()

# The default particle entity has a spherical shape and just one size distribution with
# the sieve size of 0.1 m.
particle = study.CreateParticle()

# The default circular surface is defined in the XZ plane and has a maximum radius
# of 1.0 m and center in the Cartesian coordinates of (0.0, 0.0, 0.0).
circular_surface = study.CreateCircularSurface()
study.CreateParticleInlet(entry_point=circular_surface, particle=particle)

# The domain settings define the domain limits where the particles are enabled to be
# computed in the simulation.
domain = study.GetDomainSettings()
domain.DisableUseBoundaryLimits()
domain.SetCoordinateLimitsMaxValues((10, 1, 10))


###############################################################################
# Set up the solver and run the simulation
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

solver = study.GetSolver()
solver.SetSimulationDuration(2)  # Simulate for 2 sec.

project.SaveProject(os.path.join(project_dir, "rocky-testing.rocky"))
study.StartSimulation()

###############################################################################
# Postprocess
# ~~~~~~~~~~~

# Get the particles count curve that shows the number of particles inside the domain at
# each time step of the simulation.
times, particles_count = study.GetParticles().GetNumpyCurve("Particles Count")
for time, count in zip(times, particles_count):
    print(f"Time: {time}s, Count: {count}")

rocky.close()
