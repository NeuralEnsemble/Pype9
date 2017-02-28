from pype9.base.simulation import BaseSimulation
from pype9.exceptions import Pype9NoActiveSimulationError


class Simulation(BaseSimulation):
    """Represent the simulator state."""

    active_simulation = None

    def __init__(self, *args, **kwargs):
        super(Simulation, self).__init__(*args, **kwargs)
        self._device_delay = None

    @property
    def device_delay(self):
        if self._device_delay is None:
            return self.min_delay
        else:
            return self._device_delay

#     def run(self, simtime, reset=True, reset_nest_time=False):
#         """Advance the simulation for a certain time."""
#         if reset:
#             self.reset(reset_nest_time=reset_nest_time)
#         for device in self.recording_devices:
#             if not device._connected:
#                 device.connect_to_cells()
#                 device._local_files_merged = False
#         if not self.running and simtime > 0:
#             simtime += self.dt
#             self.running = True
#         nest.Simulate(simtime)
# 
#     def run_until(self, tstop):
#         self.run(tstop - self.t)
# 
#     def reset(self, reset_nest_time=True):
#         if reset_nest_time:
#             nest.SetKernelStatus({'time': 0.0})
#         self.t_start = 0.0
#         for p in self.populations:
#             for variable, initial_value in p.initial_values.items():
#                 p._set_initial_value_array(variable, initial_value)
#         self.running = False
#         self.segment_counter += 1
#         self.reset_cells()
# 
#     def clear(self, **kwargs):
#         # Set initial values
#         self.populations = []
#         self.recording_devices = []
#         self.recorders = set()
#         # clear the sli stack, if this is not done --> memory leak cause the
#         # stack increases
#         nest.sr('clear')
#         # set tempdir
#         tempdir = tempfile.mkdtemp()
#         self.tempdirs.append(tempdir)  # append tempdir to tempdirs list
#         nest.SetKernelStatus({'data_path': tempdir})
#         self.segment_counter = 0
#         # Get values before they are reset
#         dt = kwargs.get('dt', self.dt)
#         num_processes = self.num_processes
#         threads = self.threads
#         # Reset network and kernel
#         nest.ResetKernel()
#         nest.SetKernelStatus({'overwrite_files': True, 'resolution': dt})
#         if 'dt' in kwargs:
#             self.dt = kwargs['dt']
#         # set kernel RNG seeds
#         self.num_threads = kwargs.get('threads', 1)
#         if 'grng_seed' in kwargs:
#             self.grng_seed = kwargs['grng_seed']
#         if 'rng_seeds' in kwargs:
#             self.rng_seeds = kwargs['rng_seeds']
#         else:
# 
#         self.reset(reset_nest_time=False)


def simulate(*args, **kwargs):
    return Simulation(*args, **kwargs)


def active_simulation():
    if Simulation.active_simulation is not None:
        sim = Simulation.active_simulation
    else:
        raise Pype9NoActiveSimulationError(
            "No NEST simulations are currently active")
    return sim