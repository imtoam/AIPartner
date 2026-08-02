# WF-COMMUNICATION — Language, terminology, and translation

AIPartner framework workflow module. Module ID: `WF-COMMUNICATION` (stable).

- Spine, activation checkbox, and module routing: [PROJECT_WORKFLOW.md](../../PROJECT_WORKFLOW.md)
- Core module: always active in every project.
- Sole normative owner of: the communication contract, six language responsibilities, terminology registry rules, and translation boundaries

Framework invariant: this module file is retained framework content. Tailoring changes only its
activation checkbox in the spine; it never edits, renames, or deletes this file.

---

## WF-COMMUNICATION: Language, terminology, and translation

Every project records a compact communication contract during initialization. Ask for one bundled
decision with a recommended default rather than presenting a language questionnaire.

Recommended default:

- the Product Owner and AI converse in the Product Owner's preferred language.
- maintained code identifiers, schemas, typed values, technical documentation, configuration names,
  and version-control records use one engineering language of record, normally English.
- human-facing views may use one or more approved presentation locales.
- externally sourced evidence preserves its original text, source language when known, time, URL,
  hash, and lineage.
- translation is a derived presentation artifact. It does not replace source evidence, add claims,
  change typed values, or turn unknown, stale, or insufficient data into a conclusion.

Record conversation languages, the engineering language of record, the language of code identifiers
and typed values, human-view locales, source-evidence treatment, and the translation policy as
separate facts. Do not use one field called merely `language` for all of these responsibilities.

Create a terminology registry only when domain language, multiple locales, external contracts, or
observed ambiguity justify it. The normal path is `docs/terminology.md`. Each governed term records
a stable term ID, canonical engineering term, definition, code or schema form, approved
translations, and deprecated or ambiguous aliases. A semantic change receives a new version or
term ID; do not silently redefine a term already present in code, data, decisions, or history.

Conversation and human-view translation may be flexible in style, but engineering terms and typed
semantics remain exact. Historical material without a versioned language or terminology marker is
unknown under that contract; do not infer, translate, backfill, re-embed, re-index, or rewrite it as
if missing provenance were known.
