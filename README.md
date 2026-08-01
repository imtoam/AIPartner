# AIPartner

Protocol version: 0.6.0

Human entry: open [index.html](index.html). This guide remains the human entrance after
initialization.

AI entry before initialization: read [START_HERE.md](START_HERE.md) in full and follow its
greenfield initialization protocol.

AI entry after initialization is complete: read [AGENTS.md](AGENTS.md), project_profile.yaml, and
[PROJECT_WORKFLOW.md](PROJECT_WORKFLOW.md). Do not repeat the initial interview.

Default overview renderer: `python3 tools/render_project_overview.py .`

Generated project status belongs in project-overview.html. Initialization must not overwrite
index.html. The overview is a required control surface from the start and always contains four
perspectives: management consultation, business/domain operations, system operations, and
architecture/delivery. Missing evidence is shown as an explicit source state and trigger, never as
an omitted or healthy section; the state also names its reason and accountable owner.

Tailoring is the first rule: the framework is a menu, and the project activates or creates only
what current evidence requires. Tailoring changes activation and project configuration; it does not
delete inactive framework rules.

Maintained Markdown is the authoritative project-document layer. Human-facing HTML and any local
HTTP portal are derived views with explicit sources, generation time, and stale-state handling;
they never become an independent source of project truth.

The published AIPartner framework guide is
[https://imtoam.github.io/AIPartner/](https://imtoam.github.io/AIPartner/).
