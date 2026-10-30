Requirements
============

.. req:: Report state of charge
   :id: REQ_SOC
   :issue: BMS-101
   :asil: B
   :status: [[req_status()]]
   :tags: soc; display

   The system shall report the state of charge of the 12 V pack as a
   whole percentage from 0 to 100.

.. req:: Warn on low battery
   :id: REQ_LOW_WARN
   :issue: BMS-102
   :asil: B
   :status: [[req_status()]]
   :tags: warning; driver

   The system shall warn the driver when the pack voltage falls below
   the low threshold.

.. req:: Log voltage samples
   :id: REQ_LOG
   :issue: BMS-103
   :asil: QM
   :status: [[req_status()]]
   :tags: diagnostics

   The system shall store every voltage sample with a timestamp for
   workshop diagnostics.
