Test Cases
==========

Each test case below has a matching function in ``tests/test_monitor.py``.

.. test:: SOC at mid range
   :id: TC_SOC_RANGE
   :status: passed
   :verifies: REQ_SOC
   :source: tests/test_monitor.py

   Feed 12250 mV. Expect 50 %.

.. test:: SOC clamps outside range
   :id: TC_SOC_CLAMP
   :status: passed
   :verifies: REQ_SOC
   :source: tests/test_monitor.py

   Feed 13500 mV and expect 100 %. Feed 10000 mV and expect 0 %.

.. test:: Low warning below threshold
   :id: TC_LOW_BELOW
   :status: passed
   :verifies: REQ_LOW_WARN
   :source: tests/test_monitor.py

   Feed 11999 mV. Expect the low warning.

.. test:: No warning at threshold
   :id: TC_LOW_EDGE
   :status: open
   :verifies: REQ_LOW_WARN
   :source: tests/test_monitor.py

   Feed exactly 12000 mV. Expect no low warning.
