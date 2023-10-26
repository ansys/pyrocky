import os.path
import tempfile

import ansys.rocky.prepost as pyrocky

# Create a temp directory to save the project.
project_dir = tempfile.mkdtemp(prefix="pyrocky_")

# Launch Rocky and open a project.
# "headless=False" set for demo purposes. Change to "headless=True" for performance.
rocky = pyrocky.launch_rocky(headless=False)
project = rocky.api.CreateProject()

# Configure a minimal DEM project.
study = project.GetStudy()
particle = study.CreateParticle()

inlet_surface = study.CreateCircularSurface()
study.CreateParticleInlet(entry_point=inlet_surface, particle=particle)

domain = study.GetDomainSettings()
domain.DisableUseBoundaryLimits()
domain.SetCoordinateLimitsMaxValues((10, 1, 10))

# Setup and run the simulation
solver = study.GetSolver()
solver.SetSimulationDuration(2)  # Simulate for 2 sec.

project.SaveProject(os.path.join(project_dir, "rocky-testing.rocky"))
study.StartSimulation()

# Get Particles Count curve
times, particles_count = study.GetParticles().GetNumpyCurve("Particles Count")
print(f"{particles_count[-1]} particles injected")

rocky.close()
