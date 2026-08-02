# AIPartner
<!-- AIPartner framework file · protocol 0.9.0 · source: https://github.com/imtoam/AIPartner · licence: CC BY-SA 4.0 -->

Protocol version: 0.9.0

Human entry: open [index.html](index.html). This guide remains the human entrance after
initialization.

AI entry before initialization: read [START_HERE.md](START_HERE.md) in full and follow its
greenfield initialization protocol.

AI entry after initialization is complete: read [AGENTS.md](AGENTS.md), project_profile.yaml, and
[PROJECT_WORKFLOW.md](PROJECT_WORKFLOW.md) together with the `framework/workflow/` module files it
routes to. Do not repeat the initial interview.

Default overview renderer: `python3 tools/render_project_overview.py .`

Layout: [PROJECT_WORKFLOW.md](PROJECT_WORKFLOW.md) and
[PROJECT_STRUCTURE_REFERENCE.md](PROJECT_STRUCTURE_REFERENCE.md) are spines. Topic modules live
under `framework/workflow/` and catalog files under `framework/structure/`; each concept has one
normative owner listed in the spine's concept ownership registry.

Generated project status belongs in project-overview.html. Initialization must not overwrite
index.html. The overview is a required control surface from the start; its four mandatory
perspectives and honest unavailable states are owned by
[framework/workflow/WF-VIEWS.md](framework/workflow/WF-VIEWS.md).

Tailoring is the first rule: the framework is a menu, and the project activates or creates only
what current evidence requires. Tailoring changes activation and project configuration; it does not
delete inactive framework rules.

Maintained Markdown is the authoritative project-document layer; human-facing HTML and any local
HTTP portal are derived views (owned by
[framework/workflow/WF-VIEWS.md](framework/workflow/WF-VIEWS.md)).

When several work units require coordinated delivery, pass the delivery sequencing gate owned by
[framework/workflow/WF-PLANNING.md](framework/workflow/WF-PLANNING.md) — including its mandatory
check order and a current validated `pass` receipt — before implementation begins.

The published AIPartner framework guide is
[https://imtoam.github.io/AIPartner/](https://imtoam.github.io/AIPartner/).
