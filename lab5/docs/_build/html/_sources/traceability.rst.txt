Traceability
============

Requirement to test matrix
--------------------------

.. needtable::
   :filter: type == "req"
   :columns: id; title; status;
             satisfies_back as "Specifications";
             verifies_back as "Test cases"; issue as "Issue"
   :style: table

Requirement status
------------------

.. needpie:: Requirement status
   :labels: Verified, In progress, Failed, Untested

   type == "req" and status == "verified"
   type == "req" and status == "in_progress"
   type == "req" and status == "failed"
   type == "req" and status == "untested"

Traceability graph
------------------

.. needflow:: Battery monitor traceability
   :filter: type in ["req", "spec", "impl", "test", "risk"]
   :show_link_names:

All needs
---------

.. needtable::
   :columns: id, type, title, status, tags
   :style: table
   :sort: id

Open work
---------

.. needlist::
   :filter: status in ["draft", "open", "in_progress", "untested"]
   :show_status:
   :show_tags:
