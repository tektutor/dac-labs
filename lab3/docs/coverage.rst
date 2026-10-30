Coverage Gaps
=============

Requirements without any test case
----------------------------------

.. needtable::
   :filter: type == "req" and not verifies_back
   :columns: id; title; issue as "Issue"
   :style: table

Requirements without a specification
------------------------------------

.. needtable::
   :filter: type == "req" and not satisfies_back
   :columns: id, title
   :style: table

Test coverage of requirements
-----------------------------

.. needpie:: Requirements with and without tests
   :labels: Covered, Not covered

   type == "req" and len(verifies_back) > 0
   type == "req" and len(verifies_back) == 0
