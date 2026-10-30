Specifications
==============

.. spec:: Linear voltage to SOC mapping
   :id: SPEC_SOC_LINEAR
   :status: accepted
   :satisfies: REQ_SOC
   :tags: soc

   Map 11800 mV to 0 % and 12700 mV to 100 % on a straight line.
   Clamp every value outside that range to 0 % or 100 %.

.. spec:: Low threshold of 12000 mV
   :id: SPEC_LOW_THRESHOLD
   :status: accepted
   :satisfies: REQ_LOW_WARN
   :tags: warning

   Report the pack as low when the last sample is below 12000 mV.
   A sample of exactly 12000 mV is not low.

.. spec:: Sample log format
   :id: SPEC_LOG_FORMAT
   :status: draft
   :satisfies: REQ_LOG
   :tags: diagnostics

   Store each sample as ``<ISO 8601 timestamp>;<voltage in mV>``.
