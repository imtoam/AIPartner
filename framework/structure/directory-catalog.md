# Structure catalog — Source, test, and runtime directories

AIPartner framework structure-reference catalog file.

- Spine, selection principles, and tailoring protocol: [PROJECT_STRUCTURE_REFERENCE.md](../../PROJECT_STRUCTURE_REFERENCE.md)
- This catalog is a menu, not project truth. Tailoring selects from it; it never edits this file.
- Sole normative owner of: maintained source profiles, shared categories, test structure, and generated/runtime directory treatment

Original section numbering is preserved so existing references remain valid.

---

## 5. Maintained source directories

Choose a compact profile or a layered profile. Do not create both without an explicit mapping.

### 5.1 Compact application profile

Use this profile when one application can remain understandable without top-level architecture
layers.

| Path | Responsibility |
|---|---|
| app/ or src/ | Maintained application code |
| app/domain/ | Business rules and typed domain concepts when separation becomes useful |
| app/services/ | Application use cases and orchestration |
| app/adapters/ | Database, provider, network, and platform integrations |
| app/entrypoints/ | CLI, API, worker, scheduler, and composition roots |

Only create the internal subdirectories that the project needs.

### 5.2 Layered application profile

Use this profile when several pipelines, providers, data stores, or delivery surfaces require hard
dependency boundaries.

| Path | Responsibility | Dependency rule |
|---|---|---|
| domain/ | Provider-independent rules, contracts, value objects, and states | Depends on no infrastructure SDK |
| application/ | Use cases, orchestration, and transaction boundaries | Depends on domain and ports |
| ports/ | Interfaces for storage, providers, clocks, models, brokers, and delivery | Defines boundaries, not implementations |
| infrastructure/ | Database, queue, provider, scheduler, model, and external-system adapters | Implements ports |
| entrypoints/ | CLI, API, worker, scheduled job, and composition roots | Wires application and infrastructure |

The normal dependency direction is entrypoints to application to domain and ports, with
infrastructure implementing ports. Application and domain do not import entrypoints.

### 5.3 Shared maintained categories

| Path | Responsibility | Version-control policy |
|---|---|---|
| config/ | Non-secret configuration, registries, policy files, and schemas | Include maintained configuration |
| dashboard/ or web/ | Maintained generators and optional human-facing control, status, or observation service | Include maintained source; generated HTML remains derived |
| db/schema/ | Canonical database schema definitions | Include |
| db/migrations/ | Ordered, reversible where practical, schema and data migrations | Include |
| db/fixtures/ | Small synthetic or development-only fixtures | Include when safe |
| tools/ | Human-invoked validation, inspection, maintenance, migration, and recovery utilities | Include |
| setup/ | Installation, deployment, service, scheduler, and environment setup | Include |
| assets/ | Maintained static images, styles, templates, or other packaged assets | Include |

Live database files do not become source merely because they are stored under db/. Their authority,
backup, recovery, sensitivity, and version-control policy must be explicit.

A local project service is not selected merely because `dashboard/` or `web/` exists. Static HTML
remains the default. When HTTP is justified, bind to loopback and expose read-only projections unless
the Product Owner separately approves network exposure or a write control plane with security,
identity, audit, and recovery evidence.

## 6. Test structure

Create test categories according to actual risk and system boundaries.

| Path | Responsibility |
|---|---|
| tests/unit/ | Isolated rules, calculations, validation, and edge cases |
| tests/integration/ | Components working with storage, providers, processes, or runtime wiring |
| tests/contract/ | Interfaces, schemas, events, compatibility, and dependency-direction contracts |
| tests/end_to_end/ | Critical user or operator journeys across the running system |
| tests/replay/ | Historical decisions, events, or workflows reproduced deterministically |
| tests/migration/ | Schema, data, configuration, or compatibility migrations |
| tests/fixtures/ | Synthetic, immutable, and clearly non-production test inputs |

Do not create a test directory merely to claim a test layer exists. Create it when a real test owns
that responsibility.

## 7. Generated and runtime directories

These paths normally exist outside maintained source history. Their retention and backup rules may
differ because some contain evidence or authoritative operational state.

| Path | Responsibility | Normal treatment |
|---|---|---|
| logs/ | Append-only or rotating execution and diagnostic logs | Exclude; define retention |
| reports/ | Generated analysis, test, audit, or user reports | Exclude unless curated as a release artifact |
| state/status/ | Current health, readiness, and job-status projections | Exclude; usually reconstructible |
| state/cache/ | Disposable provider, query, or computation cache | Exclude; reconstructible |
| state/snapshots/ | Point-in-time operational or recovery snapshots | Exclude; govern retention and integrity |
| state/receipts/ | Backup, restore, migration, retention, release, or approval evidence | Preserve according to audit policy |
| state/tracking/ | Runtime checkpoints, cursors, claims, and progress state | Exclude; define recovery semantics |
| state/locks/ | Process and occurrence locks | Exclude; disposable with safe stale-lock handling |
| archive/ | Immutable large objects or retired runtime material | Govern authority, retention, and checksums |
| backups/ | Verified recovery copies | Keep outside the working repository when practical |

Do not assume every state file is disposable. Classify each as authoritative, reconstructible,
evidence, or cache before defining deletion and backup rules.
