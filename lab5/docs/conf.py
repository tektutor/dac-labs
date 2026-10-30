"""Sphinx configuration for the Docs-as-Code lab project."""

project = "Battery Monitor"
author = "TekTutor"
copyright = "2026, TekTutor"
release = "1.0"

extensions = []
exclude_patterns = ["_build"]

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

latex_engine = "pdflatex"
latex_documents = [
    ("index", "battery-monitor.tex", "Battery Monitor", author, "manual"),
]
latex_elements = {"papersize": "a4paper", "pointsize": "10pt"}

# -- Lab 2: Sphinx-Needs ------------------------------------------------------
extensions += ["sphinx_needs", "sphinx.ext.graphviz"]

needs_types = [
    {"directive": "req", "title": "Requirement", "prefix": "REQ_",
     "color": "#BFD8D2", "style": "node"},
    {"directive": "spec", "title": "Specification", "prefix": "SPEC_",
     "color": "#FEDCD2", "style": "node"},
    {"directive": "impl", "title": "Implementation", "prefix": "IMPL_",
     "color": "#DF744A", "style": "node"},
    {"directive": "test", "title": "Test Case", "prefix": "TC_",
     "color": "#DCB239", "style": "node"},
]
needs_id_required = True
needs_id_regex = r"^[A-Z]+_[A-Z0-9_]+$"

needs_links = {
  "satisfies": {"incoming": "satisfied by", "outgoing": "satisfies"},
  "verifies": {"incoming": "verified by", "outgoing": "verifies"},
}

needs_flow_engine = "graphviz"
needs_flow_show_links = True

# Sphinx-Needs 9.1 calls an API that Sphinx 8.2 marks as deprecated. The
# Python warning it prints does not affect the build, so hide it.
import warnings
warnings.filterwarnings(
    "ignore", message="Sphinx 9 will drop support for representing paths"
)
# -- Lab 3: fields for issue IDs and source files ----------------------------
import os

needs_fields = {
    "issue": {
            "description": "Issue tracker ID, for example BMS-101.",
            "schema": {"type": "string", "pattern": "^[A-Z]+-[0-9]+$"},
    },
    "source": {
        "description": "Repository path of the implementing file.",
        "schema": {"type": "string"},
    },
}

# CI can set REPO_URL. On your machine the default applies.
REPO_URL = os.environ.get("REPO_URL", "https://github.com/your-org/dac-labs")

needs_string_links = {
    "issue_link": {
        "regex": r"^(?P<value>[A-Z]+-\d+)$",
        "link_url": "https://issues.example.com/browse/{{value}}",
        "link_name": "{{value}}",
        "options": ["issue"],
    },
    "source_link": {
        "regex": r"^(?P<value>(src|tests)/.+)$",
        "link_url": REPO_URL + "/blob/main/{{value}}",
        "link_name": "{{value}}",
        "options": ["source"],
    },
}

# -- Lab 4: quality checks ---------------------------------------------------
extensions += ["sphinxcontrib.spelling"]

# Treat every unresolved cross-reference as a warning.
nitpicky = True

spelling_lang = "en_US"
spelling_word_list_filename = "spelling_wordlist.txt"

spelling_show_suggestions = True
spelling_warning = True
# Skip the "git log" contributor scan. It fails in a clone without history.
spelling_ignore_contributor_names = False

linkcheck_ignore = [
    r"https://issues\.example\.com/.*",
    r"https://github\.com/your-org/.*",
]
linkcheck_timeout = 15
linkcheck_retries = 2

def _quiet_needflow(app):
    """Spelling and linkcheck builders do not draw diagrams, so silence
    the "needflow is only supported for HTML" warning for them."""
    if app.builder.name in ("spelling", "linkcheck"):
        app.config.suppress_warnings = [
        *app.config.suppress_warnings, "needs.needflow"
]

def setup(app):
    app.connect("builder-inited", _quiet_needflow)
# -- Lab 5: custom type, fields and links ------------------------------------
needs_types.append(
    {"directive": "risk", "title": "Risk", "prefix": "RISK_",
     "color": "#F4A6A6", "style": "node"}
)

needs_fields.update({
    "status": {
        "description": "Life-cycle state of a need.",
        "schema": {
            "type": "string",
            "enum": ["draft", "open", "in_progress", "verified",
                     "failed", "untested", "accepted", "closed"],
        },
    },
    "asil": {
        "description": "ISO 26262 integrity level.",
        "schema": {"type": "string", "enum": ["QM", "A", "B", "C", "D"]},
    },
    "result": {
        "description": "Last test result.",
        "schema": {"type": "string", "enum": ["pass", "fail", "not_run"]},
    },
    "severity": {
        "description": "Risk severity.",
        "schema": {"type": "string", "enum": ["low", "medium", "high"]},
    },
})

needs_links.update({
    "implements": {"incoming": "implemented by", "outgoing": "implements"},
    "mitigates": {"incoming": "mitigated by", "outgoing": "mitigates",
                  "color": "#C0392B", "style": "dashed"},
})

# -- Lab 5: requirement status computed from linked test results -------------
def req_status(app, need, needs, *args, **kwargs):
    """Roll the results of all tests that verify this need into one status."""
    my_id = need["id"]
    results = [
        other.get("result")
        for other in needs.values()
        if other["type"] == "test" and my_id in other["verifies"]
    ]      
    if not results:
        return "untested"
    if "fail" in results:
        return "failed"
    if all(result == "pass" for result in results):
        return "verified"
    return "in_progress"

# -- Lab 5: custom layout ----------------------------------------------------
needs_layouts = {
    "bms": {
        "grid": "simple",
        "layout": {
            "head": [
            '<<meta("type_name")>>: **<<meta("title")>>** <<meta_id()>>'
            ],
            "meta": [
                '<<meta("status")>>',
                '<<meta("asil", prefix="ASIL: ")>>',
                '<<meta("severity", prefix="Severity: ")>>',
                '<<meta("result", prefix="Result: ")>>',
                '<<meta("issue", prefix="Issue: ")>>',
                '<<meta("source", prefix="Source: ")>>',
                "<<meta_links_all()>>",
            ],
        },
    },
}
needs_default_layout = "bms"

# This setup() replaces the one from Lab 4. Python keeps the last definition.
# Registering the function here, instead of listing it in needs_functions,
# avoids a "cannot cache unpickleable configuration value" warning.
def setup(app):
    from sphinx_needs.api import add_dynamic_function
    
    add_dynamic_function(app, req_status)
    app.connect("builder-inited", _quiet_needflow)
