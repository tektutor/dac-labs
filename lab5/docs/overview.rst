Overview
========

The battery monitor reads the pack voltage, converts it into a state of
charge and warns the driver when the pack runs low.

Voltage to state of charge
--------------------------

.. list-table::
   :header-rows: 1
   :widths: 40 30 30

   * - Pack voltage
     - State of charge
     - Low warning
   * - 12700 mV
     - 100 %
     - No
   * - 12250 mV
     - 50 %
     - No
   * - 11999 mV
     - 22 %
     - Yes
   * - 11800 mV
     - 0 %
     - Yes

Sphinx is published at https://pypi.org/project/Sphinx/ and
Sphinx-Needs at https://pypi.org/project/sphinx-needs/.
