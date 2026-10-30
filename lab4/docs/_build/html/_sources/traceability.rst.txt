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

Status roll-up
--------------

.. needtable::
   :filter: type in ["req", "spec"]
   :columns: id, type, status
   :sort: status
   :style: table

.. needpie:: Requirement and specification status
   :labels: Open, Draft, Accepted

   type in ["req", "spec"] and status == "open"
   type in ["req", "spec"] and status == "draft"
   type in ["req", "spec"] and status == "accepted"

Impact of REQ_LOW_WARN
----------------------

.. needflow:: Impact of REQ_LOW_WARN
   :filter: id == "REQ_LOW_WARN" or "REQ_LOW_WARN" in satisfies or "REQ_LOW_WARN" in verifies

All needs
---------

.. needtable::
   :columns: id, type, title, status, tags
   :style: table
   :sort: id

Needs tagged warning
--------------------

.. needtable::
   :tags: warning
   :columns: id, type, title
   :style: table

Traceability graph
------------------

.. needflow:: Battery monitor traceability
   :filter: type in ["req", "spec", "test"]
   :show_link_names:

Requirement list
----------------

.. needlist::
   :types: req
   :show_status:
   :show_tags:
