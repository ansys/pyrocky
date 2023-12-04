""".. _ref_particle_wall_interaction:

Particle simulation with wall interaction
-----------------------------------------
This example sets up and solves a simulation of particles interacting with a cylinder
wall.

"""

###############################################################################
# .. image:: /_static/open_cylinder_result.png
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

# Download the STL file that will imported into Rocky to represent a Wall.
file_name = "open_cylinder.stl"
file_path = examples.download_file(project_dir, file_name, "pyrocky/geometries")
study.ImportWall(file_path)

# Create a sphero-cylinder shape particle with the default size distribution (single
# distribution with sieve size of 0.1 m).
particle = study.CreateParticle()
particle.SetShape("sphero_cylinder")

# Create circular surface with a max radius of 0.3 m and default center coordinates
# values (0.0, 0.0, 0.0).
circular_surface = study.CreateCircularSurface()
circular_surface.SetMaxRadius(0.3, "m")
particle_inlet = study.CreateParticleInlet(circular_surface, particle)

###############################################################################
# Setup the solver and run the simulation
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

solver = study.GetSolver()
solver.SetSimulationDuration(2, unit="s")
study.StartSimulation()

###############################################################################
# Post-processing
# ~~~~~~~~~~~~~~~
# Obtain the particle count curve over the entire particle domain and in a half-cylinder
# domain selection, as shown in the figure below.

###############################################################################
# .. image:: /_static/open_cylinder_result_selection.png
#   :width: 400pt
#   :align: center

processes = project.GetUserProcessCollection()

particles = study.GetParticles()
cylinder_selection = processes.CreateCylinderProcess(particles)
cylinder_selection.SetSize(2, 0.74, 2, unit="m")
cylinder_selection.SetCenter(0, -0.37, 0, unit="m")
cylinder_selection.SetFinalAngle(180)

times, all_particles_count = particles.GetNumpyCurve("Particles Count")
times, selection_count = cylinder_selection.GetNumpyCurve("Particles Count")

#################################################################################
# Plotting curves
# +++++++++++++++

import matplotlib.pyplot as plt

fig, ax = plt.subplots(1)

ax.plot(times, all_particles_count, "b", label="All Particles")
ax.plot(times, selection_count, "r", label="Selection Particles")
ax.set_xlabel("Time [s]")
ax.set_ylabel("Count [-]")
ax.legend(loc="upper left")

plt.draw()

rocky.close()
