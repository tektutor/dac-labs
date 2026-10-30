Requirements
============

.. req:: Report state of charge
   :id: REQ_SOC
   :status: open
   :tags: soc; display

   The system shall report the state of charge of the 12 V pack as a
   whole percentage from 0 to 100.

.. req:: Warn on low battery
   :id: REQ_LOW_WARN
   :status: open
   :tags: warning; driver

   The system shall warn the driver when the pack voltage falls below
   the low threshold.

.. req:: Log voltage samples
   :id: REQ_LOG
   :status: draft
   :tags: diagnostics

   The system shall store every voltage sample with a timestamp for
   workshop diagnostics.
