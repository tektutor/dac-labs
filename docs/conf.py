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
