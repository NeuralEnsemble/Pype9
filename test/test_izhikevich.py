simulator = 'neuron'
import nineml
if simulator == 'neuron':
    from pype9.cells.neuron import CellMetaClass  # @UnusedImport
else:
    from pype9.cells.nest import CellMetaClass  # @Reimport
import os.path
import quantities as pq
from matplotlib import pyplot as plt
import neo
import numpy


izhi = nineml.read(os.path.join(
    os.environ['HOME'], 'git', 'nineml_catalog', 'neurons',
    'Izhikevich2003.xml'))['Izhikevich2003Properties']


Izhikevich = CellMetaClass(izhi)

izhi = Izhikevich()
izhi.record('v')
izhi.update_state({'v': -65.0 * pq.ms})
current = neo.AnalogSignal(
    numpy.concatenate((numpy.zeros(300), numpy.ones(700))) * 10,
    units=pq.nA, sampling_period=1.0 * pq.ms)
izhi.play('iExt', current)
izhi.run(1000 * pq.ms)
v = izhi.recording('v')
plt.plot(v.times, v)
plt.plot(current.times, current)
plt.show()