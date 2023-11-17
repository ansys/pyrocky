""".. _ref_minimal:

Simple Particle Simulation
--------------------------
This example sets up and solves a simple particle simulation workflow.

"""

###############################################################################
# Perform imports and create a project
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Perform the required imports and create an empty project.

import os.path
import tempfile
import ansys.rocky.prepost as pyrocky

# Create a temp directory to save the project.
project_dir = tempfile.mkdtemp(prefix="pyrocky_")

# Launch Rocky and open a project.
rocky = pyrocky.launch_rocky()
project = rocky.api.CreateProject()

###############################################################################
# Configure the study
# ~~~~~~~~~~~~~~~~~~~
# Create a particle entity that will be injected through a circular surface.

study = project.GetStudy()

# The default particle entity has a spherical shape and just one size distribution with 
# the sieve size of 0.1 m. 
particle = study.CreateParticle()

# The default circular surface is defined in the XZ plane and has a max radius of 1.0 m
# and center in the cartesian coordinates of (0.0, 0.0, 0.0).
circular_surface = study.CreateCircularSurface()
study.CreateParticleInlet(entry_point=circular_surface, particle=particle)

# The domain settings define the domain limits where the particles are enabled to be 
# computed in the simulation.
domain = study.GetDomainSettings()
domain.DisableUseBoundaryLimits()
domain.SetCoordinateLimitsMaxValues((10, 1, 10))


###############################################################################
# Setup the solver and run the simulation
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

solver = study.GetSolver()
solver.SetSimulationDuration(2)  # Simulate for 2 sec.

project.SaveProject(os.path.join(project_dir, "rocky-testing.rocky"))
study.StartSimulation()

###############################################################################
# Post-processing
# ~~~~~~~~~~~~~~~

# Get the particles count curve that shows the number of particles inside the domain at 
# each time step of the simulation.
times, particles_count = study.GetParticles().GetNumpyCurve("Particles Count")
for time, count in zip(times, particles_count):
    print(f"Time: {time}s, Count: {count}")

rocky.close()
