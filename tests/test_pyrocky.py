import pytest

import ansys.rocky.core as pyrocky


@pytest.fixture()
def rocky_session():
    rocky = pyrocky.launch_rocky()
    yield rocky
    rocky.close()


def test_minimal_simulation(rocky_session, tmp_path):
    rocky = pyrocky.connect_to_rocky()
    project = rocky.api.CreateProject()
    assert project, "No project created"

    study = project.GetStudy()
    particle = study.CreateParticle()

    inlet_surface = study.CreateCircularSurface()
    study.CreateParticleInlet(entry_point=inlet_surface, particle=particle)

    domain = study.GetDomainSettings()
    domain.DisableUseBoundaryLimits()
    domain.SetCoordinateLimitsMaxValues((10, 1, 10))

    solver = study.GetSolver()
    solver.SetSimulationDuration(2)  # Simulate for 2 sec.

    project.SaveProject(str(tmp_path / "rocky-testing.rocky"))
    study.StartSimulation()

    particles_count = study.GetParticles().GetNumpyCurve("Particles Count")

    # Just check that simulation results are at a reasonable ballpark
    assert particles_count[1][-1] > 20, "Too few particles generated"
