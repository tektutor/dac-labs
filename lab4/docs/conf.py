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
