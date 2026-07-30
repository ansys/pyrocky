# Copyright (C) 2023 - 2024 ANSYS, Inc. and/or its affiliates.
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

""".. _ref_particle_wall_interaction_with_motion:

Particle simulation with moving wall interaction
------------------------------------------------
This example sets up and solves a simulation of particles interacting with a rotating
L-shape tube wall.

"""
###############################################################################
# .. image:: /_static/Lshape_tube_result.png
#   :width: 400pt
#   :align: center

###############################################################################
# Perform imports and create a project
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Perform the required imports and create an empty project.

import os.path
import tempfile

import ansys.rocky.core as pyrocky
from ansys.rocky.core import examples

# Create a temp directory to save the project.
project_dir = tempfile.mkdtemp(prefix="pyrocky_")

# Launch Rocky and open a project.
rocky = pyrocky.launch_rocky()
project = rocky.api.CreateProject()
project.SaveProject(os.path.join(project_dir, "rocky-testing.rocky"))

###############################################################################
# Configure the study
# ~~~~~~~~~~~~~~~~~~~
study = project.GetStudy()

# Download the STL file that was imported into Rocky to represent a wall.
file_name = "Lshape_tube.stl"
file_path = examples.download_file(project_dir, file_name, "pyrocky/geometries")
wall = study.ImportWall(file_path)[0]

# Create a particle with the default shape (sphere) and size distribution (single
# distribution with a sieve size of 0.1 m).
particle = study.CreateParticle()

# Create a circular surface to used as the inlet.
circular_surface = study.CreateCircularSurface()
circular_surface.SetMaxRadius(0.8, unit="m")

# Create a rectangular surface to use as the outlet.
rectangular_surface = study.CreateRectangularSurface()
rectangular_surface.SetLength(3, unit="m")
rectangular_surface.SetWidth(3, unit="m")
rectangular_surface.SetCenter((5, -7.5, 0), unit="m")

# Set the inlet and outlet.
particle_inlet = study.CreateParticleInlet(circular_surface, particle)
input_property_list = particle_inlet.GetInputPropertiesList()
input_property_list[0].SetMassFlowRate(1000)
outlet = study.CreateOutlet(rectangular_surface)

# Set the motion rotation over the Y axis and apply it on the wall and the
# rectagular surface used as the outlet.
motion_frame_source = study.GetMotionFrameSource()
motion_frame = motion_frame_source.NewFrame()
motion_frame.AddRotationMotion(angular_velocity=((0.0, 0.5, 0.0), "rad/s"))
motion_frame.ApplyTo(rectangular_surface)
motion_frame.ApplyTo(wall)

# The domain settings define the domain limits where the particles are enabled to be
# computed in the simulation.
domain = study.GetDomainSettings()
domain.DisableUseBoundaryLimits()
domain.SetCoordinateLimitsMaxValues((10, 1, 10), unit="m")

###############################################################################
# Set up the solver and run the simulation
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

solver = study.GetSolver()
solver.SetSimulationDuration(5, unit="s")
study.StartSimulation()

###############################################################################
# Postprocess
# ~~~~~~~~~~~
# Obtain the in and out mass flows of the particles.

particles = study.GetParticles()

times, mass_flow_in = particles.GetNumpyCurve("Particles Mass Flow In", unit="t/h")
times, mass_flow_out = particles.GetNumpyCurve("Particles Mass Flow Out", unit="t/h")


#################################################################################
# Plot curves
# +++++++++++

import matplotlib.pyplot as plt

fig, ax = plt.subplots(1)

ax.plot(times, mass_flow_in, "b", label="Mass Flow In")
ax.plot(times, mass_flow_out, "r", label="Mass Flow Out")
ax.set_xlabel("Time [s]")
ax.set_ylabel("Mass Flow [t/h]")
ax.legend(loc="upper left")

plt.draw()

rocky.close()
