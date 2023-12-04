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


def test_sequences_interface(rocky_session):
    """Ensure that API objects that are sequences have their dunder methods exposed."""
    rocky = pyrocky.connect_to_rocky()
    project = rocky.api.CreateProject()

    study = project.GetStudy()

    inlets_outlets = study.GetInletsOutletsCollection()
    inlet = inlets_outlets.AddParticleInlet()
    inlet.SetName("Inlet1")
    inlet = inlets_outlets.AddVolumetricInlet()
    inlet.SetName("Inlet2")

    # Test __len__
    assert len(inlets_outlets) == 2
    # Test __getitem__
    assert inlets_outlets[1].GetName() == "Inlet2"
    # Test __iter__
    assert {e.GetName() for e in inlets_outlets} == {"Inlet1", "Inlet2"}
    # Test __del__
    del inlets_outlets[0]
    assert {e.GetName() for e in inlets_outlets} == {"Inlet2"}
