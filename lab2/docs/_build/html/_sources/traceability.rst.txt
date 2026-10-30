Traceability
============

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

Open or draft needs
-------------------

.. needtable::
   :filter: status in ["open", "draft"] and type != "test"
   :columns: id, type, title, status
   :style: table

Traceability graph
------------------

.. needflow:: Battery monitor traceability
   :filter: type in ["req", "spec", "test"]
   :show_link_names:

Test status
-----------

.. needpie:: Test case status
   :labels: Passed, Open

   type == "test" and status == "passed"
   type == "test" and status == "open"

Requirement list
----------------

.. needlist::
   :types: req
   :show_status:
   :show_tags:
