#!/usr/bin/env python3
# AIPartner framework file · protocol 0.11.0 · source: https://github.com/imtoam/AIPartner · licence: CC BY-SA 4.0
"""Render introduction/framework-scope.html from the framework's own Markdown.

The scope map is a derived view of two facts that already exist in Markdown: which modules the
framework contains, and what each one owns. Nothing on the page is authored here — module names
come from the activation checkbox blocks, the one-line summaries come from each module's
"Sole normative owner of" line, and the trigger sentences come from each module's
"Activation condition" bullets.

The renderer uses only the Python standard library, fails before writing when a source is missing
or incomplete, and replaces the output atomically.
"""

from __future__ import annotations

import html
import os
import re
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

OUTPUT_PATH = "introduction/framework-scope.html"

ROLE_BLOCK = "ROLE MODULE ACTIVATION"
WORKFLOW_BLOCK = "WORKFLOW MODULE ACTIVATION"

CHECKBOX_PATTERN = re.compile(r"^- \[([ xX])\] ([A-Z]+-[A-Z-]+): (.+)$", re.MULTILINE)
OWNER_PATTERN = re.compile(r"^- Sole normative owner of: (.+?)\.?$", re.MULTILINE)
ROUTING_PATTERN = re.compile(r"^\| ([A-Z]+-[A-Z-]+) \| \[[^\]]+\]\(([^)]+)\) \|", re.MULTILINE)
ROLE_ROUTING_PATTERN = re.compile(r"\[(framework/roles/([A-Z-]+)\.md)\]\(")
PROTOCOL_PATTERN = re.compile(r"^Protocol version: (\d+\.\d+\.\d+)$", re.MULTILINE)


class RenderError(RuntimeError):
    """A source is missing or incomplete; the existing page is left untouched."""


@dataclass(frozen=True)
class Module:
    module_id: str
    label: str
    always_active: bool
    governs: str
    trigger: str
    source: str


def read(root: Path, relative: str) -> str:
    path = root / relative
    if not path.is_file():
        raise RenderError(f"Required source is missing: {relative}")
    return path.read_text(encoding="utf-8")


def config_block(text: str, name: str, relative: str) -> str:
    match = re.search(
        rf"<!-- BEGIN PROJECT CONFIG: {name} -->(.*?)<!-- END PROJECT CONFIG: {name} -->",
        text,
        re.S,
    )
    if not match:
        raise RenderError(f"{relative} has no {name} block")
    return match.group(1)


def section(text: str, module_id: str, relative: str) -> str:
    match = re.search(rf"^## {re.escape(module_id)}:.*?(?=^## |\Z)", text, re.M | re.S)
    if not match:
        raise RenderError(f"{relative} has no section for {module_id}")
    return match.group(0)


def governs_of(text: str, module_id: str, relative: str) -> str:
    match = OWNER_PATTERN.search(text)
    if not match:
        raise RenderError(
            f"{relative} states no 'Sole normative owner of' line for {module_id}; "
            "the scope map cannot describe a module that does not describe itself"
        )
    return " ".join(match.group(1).split())


def trigger_of(text: str) -> str:
    match = re.search(r"^Activation condition:\s*\n\n((?:- .*\n(?:  .*\n)*)+)", text, re.M)
    if not match:
        return ""
    bullets = re.findall(r"^- (.*(?:\n  .*)*)$", match.group(1), re.M)
    return "; ".join(" ".join(bullet.split()) for bullet in bullets)


def collect_modules(root: Path) -> tuple[list[Module], list[Module]]:
    agents_text = read(root, "AGENTS.md")
    workflow_text = read(root, "PROJECT_WORKFLOW.md")

    routes = dict(ROUTING_PATTERN.findall(workflow_text))
    for relative, role_id in ROLE_ROUTING_PATTERN.findall(agents_text):
        routes[role_id] = relative

    collected: list[Module] = []
    for block_name, host_text, host_relative in (
        (ROLE_BLOCK, agents_text, "AGENTS.md"),
        (WORKFLOW_BLOCK, workflow_text, "PROJECT_WORKFLOW.md"),
    ):
        block = config_block(host_text, block_name, host_relative)
        for mark, module_id, label in CHECKBOX_PATTERN.findall(block):
            source = routes.get(module_id, host_relative)
            if source == host_relative:
                body = section(host_text, module_id, host_relative)
            else:
                body = read(root, source)
            collected.append(
                Module(
                    module_id=module_id,
                    label=label.strip(),
                    always_active=mark.lower() == "x",
                    governs=governs_of(body, module_id, source),
                    trigger=trigger_of(body),
                    source=source,
                )
            )

    if not collected:
        raise RenderError("No modules found in the activation blocks")

    baseline = [module for module in collected if module.always_active]
    optional = [module for module in collected if not module.always_active]
    missing = [module.module_id for module in optional if not module.trigger]
    if missing:
        raise RenderError(
            "Optional modules without an activation condition: " + ", ".join(missing)
        )
    return baseline, optional


def protocol_version(root: Path) -> str:
    match = PROTOCOL_PATTERN.search(read(root, "START_HERE.md"))
    if not match:
        raise RenderError("START_HERE.md states no 'Protocol version:' line")
    return match.group(1)


def sentence(text: str) -> str:
    text = text.strip()
    if not text:
        return ""
    return text[0].upper() + text[1:] + ("" if text.endswith(".") else ".")


def card(module: Module) -> str:
    escaped_id = html.escape(module.module_id)
    condition = (
        "Always active"
        if module.always_active
        else "Activates when " + html.escape(module.trigger)
    )
    return f"""        <a class="card" href="../{html.escape(module.source)}">
          <span class="num">{escaped_id}</span>
          <h3>{html.escape(module.label)}</h3>
          <p>{html.escape(sentence(module.governs))}</p>
          <p class="condition">{condition}</p>
          <span class="more">Open the Markdown →</span>
        </a>
"""


STYLE = """    :root {
      color-scheme: light;
      --paper: #f4f0e7;
      --paper-deep: #e9e1d3;
      --white: #fffdf8;
      --ink: #202a2a;
      --muted: #65706d;
      --line: #cdc3b3;
      --forest: #184d49;
      --forest-dark: #123a37;
      --accent: #a44d2f;
      --accent-soft: #f0d9cc;
      --glow: #e9b8a4;
      --shadow: 0 18px 55px rgba(35, 45, 42, 0.11);
      --sans: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      --serif: Iowan Old Style, Baskerville, "Times New Roman", serif;
    }

    * { box-sizing: border-box; }
    html { scroll-behavior: smooth; }

    body {
      margin: 0;
      background: var(--paper);
      color: var(--ink);
      font-family: var(--serif);
      line-height: 1.68;
      text-rendering: optimizeLegibility;
    }

    a { color: var(--forest); text-underline-offset: 0.18em; }

    .masthead {
      min-height: 320px;
      padding: 28px 32px 72px;
      position: relative;
      overflow: hidden;
      background:
        radial-gradient(
          circle at calc(100% - 90px) calc(100% - 15px),
          rgba(233, 184, 164, 0.15) 0,
          rgba(255, 253, 248, 0.04) 90px,
          transparent 190px
        ),
        var(--forest-dark);
      color: var(--white);
    }

    .masthead::before,
    .masthead::after {
      content: "";
      width: 190px;
      height: 190px;
      border: 1px solid rgba(255, 253, 248, 0.38);
      border-radius: 50%;
      position: absolute;
      right: 15px;
      bottom: -70px;
      opacity: 0;
      box-shadow:
        0 0 18px rgba(233, 184, 164, 0.24),
        inset 0 0 13px rgba(255, 253, 248, 0.09);
      pointer-events: none;
      transform: scale(0.28);
      transform-origin: center;
      animation: radiating-glow 6.4s ease-out infinite;
      will-change: transform, opacity;
    }

    .masthead::after { animation-delay: 3.2s; }

    @keyframes radiating-glow {
      0% { opacity: 0; transform: scale(0.28); }
      14% { opacity: 0.3; }
      58% { opacity: 0.13; }
      100% { opacity: 0; transform: scale(4); }
    }

    @media (prefers-reduced-motion: reduce) {
      html { scroll-behavior: auto; }
      .masthead::before,
      .masthead::after { opacity: 0.18; transform: scale(2.3); animation: none; }
    }

    .masthead-inner,
    .page { width: min(1120px, 100%); margin: 0 auto; position: relative; z-index: 1; }

    .topline {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 24px;
      color: rgba(255, 253, 248, 0.72);
      font-family: var(--sans);
      font-size: 0.76rem;
      letter-spacing: 0.13em;
      text-transform: uppercase;
    }

    .hero { max-width: 900px; margin-top: 52px; }

    .eyebrow,
    .section-label {
      margin: 0 0 17px;
      color: var(--glow);
      font-family: var(--sans);
      font-size: 0.76rem;
      font-weight: 700;
      letter-spacing: 0.14em;
      text-transform: uppercase;
    }

    h1 {
      max-width: 880px;
      margin: 0;
      font-size: clamp(2.4rem, 5.2vw, 4.2rem);
      font-weight: 500;
      letter-spacing: -0.05em;
      line-height: 0.97;
    }

    .dek {
      max-width: 720px;
      margin: 24px 0 0;
      color: rgba(255, 253, 248, 0.8);
      font-size: clamp(1.02rem, 1.6vw, 1.24rem);
      line-height: 1.52;
    }

    .masthead a { color: var(--accent-soft); }

    .page { width: min(1120px, calc(100% - 48px)); margin-top: -42px; margin-bottom: 80px; }

    .content-panel {
      border: 1px solid var(--line);
      background: var(--white);
      box-shadow: var(--shadow);
      padding: clamp(28px, 4.4vw, 50px);
    }

    .content-panel + .content-panel { margin-top: 22px; }

    .section-label { color: var(--accent); }

    h2 {
      max-width: 760px;
      margin: 0;
      font-size: clamp(1.7rem, 3.4vw, 2.7rem);
      font-weight: 500;
      letter-spacing: -0.035em;
      line-height: 1.04;
    }

    .lede { max-width: 760px; margin: 16px 0 0; color: #44504e; font-size: 1.06rem; }

    .lede .fine { color: var(--muted); font-family: var(--sans); font-size: 0.85rem; }

    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
      gap: 14px;
      margin-top: 30px;
    }

    .card {
      display: flex;
      flex-direction: column;
      gap: 6px;
      background: #faf7f0;
      border: 1px solid var(--line);
      padding: 20px 22px;
      color: inherit;
      text-decoration: none;
      overflow-wrap: anywhere;
      transition: transform 0.15s ease, box-shadow 0.15s ease, border-color 0.15s ease;
    }

    .card:hover,
    .card:focus-visible {
      transform: translateY(-3px);
      border-color: var(--accent);
      box-shadow: var(--shadow);
      background: var(--white);
    }

    .card .num {
      font-family: var(--sans);
      font-size: 0.7rem;
      font-weight: 700;
      letter-spacing: 0.08em;
      color: var(--accent);
    }

    .card h3 {
      margin: 0;
      font-family: var(--sans);
      font-size: 1rem;
      letter-spacing: -0.01em;
      line-height: 1.35;
      color: var(--forest-dark);
    }

    .card p { margin: 0; color: var(--muted); font-size: 0.93rem; line-height: 1.5; }

    .card .condition {
      margin-top: 4px;
      padding-top: 8px;
      border-top: 1px dashed var(--line);
      font-family: var(--sans);
      font-size: 0.8rem;
      color: var(--forest);
    }

    .card .more {
      margin-top: auto;
      padding-top: 8px;
      font-family: var(--sans);
      font-size: 0.74rem;
      font-weight: 700;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      color: transparent;
      transition: color 0.15s ease;
    }

    .card:hover .more,
    .card:focus-visible .more { color: var(--accent); }

    .footer {
      border-top: 1px solid var(--line);
      background: var(--paper-deep);
      padding: 22px 32px;
      font-family: var(--sans);
      font-size: 0.84rem;
      color: var(--muted);
    }

    .footer-inner {
      width: min(1120px, 100%);
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 10px;
    }

    .footer a { margin-left: 14px; }
"""


def build_html(root: Path) -> str:
    baseline, optional = collect_modules(root)
    version = protocol_version(root)
    series = ".".join(version.split(".")[:2])

    baseline_cards = "".join(card(module) for module in baseline)
    optional_cards = "".join(card(module) for module in optional)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="aipartner-page-role" content="framework-scope-map">
  <meta name="aipartner-source" content="AIPartner {version}" />
  <meta name="aipartner-source-url" content="https://github.com/imtoam/AIPartner" />
  <meta name="aipartner-licence" content="CC BY-SA 4.0" />
  <meta name="aipartner-generated-by" content="tools/render_framework_scope.py" />
  <title>AIPartner — Framework Scope Map</title>
  <style>
{STYLE}  </style>
</head>
<body>
  <header class="masthead">
    <div class="masthead-inner">
      <div class="topline">
        <span>AIPartner</span>
        <span>Protocol {series} / Framework scope map</span>
      </div>
      <div class="hero">
        <p class="eyebrow">{len(baseline)} always on · {len(optional)} on condition</p>
        <h1>What you always get, and what waits until you need it.</h1>
        <p class="dek">
          Every rule in the framework belongs to one module. This page lists them all, in the only
          two groups that matter to a new project: the baseline that every project receives, and
          the modules that stay dormant until a stated condition becomes true.
        </p>
      </div>
    </div>
  </header>

  <main class="page">
    <div class="content-panel">
      <p class="section-label">Baseline</p>
      <h2>Every project receives these {len(baseline)}</h2>
      <p class="lede">
        These are not selected, and tailoring cannot remove them. It can only make them lighter:
        a one-person weekend project and a regulated system run the same modules at different
        depths of evidence. Behind them sit the framework's own mechanisms — the initialization
        protocol, the tailoring protocol with its decision states, the machine-readable profile,
        the hash manifest and the validators — which are described in the
        <a href="framework-detail.html">scope details</a> rather than listed as choices, because
        nobody chooses them.
        <span class="fine">Derived view generated from the Markdown. Protocol {version}.</span>
      </p>

      <div class="grid">
{baseline_cards}      </div>
    </div>

    <div class="content-panel">
      <p class="section-label">On condition</p>
      <h2>These {len(optional)} activate when the project earns them</h2>
      <p class="lede">
        Each card states its own trigger, taken from the module itself. A condition that is true
        today activates the module now; a condition that is merely foreseeable is recorded as a
        deferred trigger instead. An artifact produced by activating a module is never evidence
        that the module was needed, and no module is ever activated silently — the Product Owner
        approves each one.
      </p>

      <div class="grid">
{optional_cards}      </div>
    </div>
  </main>

  <footer class="footer">
    <div class="footer-inner">
      <span>Generated by tools/render_framework_scope.py — the linked Markdown is authoritative</span>
      <nav aria-label="Footer links">
        <a href="framework-detail.html">Scope details</a>
        <a href="../index.html">Human guide</a>
        <a href="https://github.com/imtoam/AIPartner">GitHub repository</a>
      </nav>
    </div>
  </footer>
</body>
</html>
"""


def render(root: Path) -> Path:
    content = build_html(root)
    output_path = root / OUTPUT_PATH
    output_path.parent.mkdir(parents=True, exist_ok=True)
    handle = tempfile.NamedTemporaryFile(
        "w",
        encoding="utf-8",
        delete=False,
        prefix=f".{output_path.name}.",
        suffix=".tmp",
        dir=output_path.parent,
    )
    try:
        with handle:
            handle.write(content)
        os.replace(handle.name, output_path)
    except BaseException:
        Path(handle.name).unlink(missing_ok=True)
        raise
    return output_path


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    try:
        output_path = render(root)
    except RenderError as error:
        print(f"ERROR {error}", file=sys.stderr)
        return 1
    print(f"Rendered {output_path.relative_to(root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
