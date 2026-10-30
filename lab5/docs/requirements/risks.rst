Risk Register
=============

.. risk:: Deep discharge damages the pack
   :id: RISK_DEEP_DISCHARGE
   :severity: high
   :status: open

   If the driver gets no warning, the pack can discharge below 10.5 V
   and lose capacity for good.

.. risk:: Voltage sensor drift
   :id: RISK_SENSOR_DRIFT
   :severity: medium
   :status: open

   An aging sensor can read 100 mV high and delay the low warning.

Risks without mitigation
------------------------

.. needtable::
   :filter: type == "risk" and not mitigates_back
   :columns: id, title, severity, status
   :style: table
