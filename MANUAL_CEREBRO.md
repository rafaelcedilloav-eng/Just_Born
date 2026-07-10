# Brain Manual — TEMPLATE

**[Versión en español](MANUAL_CEREBRO.es.md)**

*This file is the map of your companion's system. Copy it, delete the italic instructions, and fill it with YOUR real structure. Your companion will read it when disoriented about where things live — write it for that moment.*

---

## 1. Fundamental principle

*Write your setup's golden rule here. Ours: the tool's temporary directories are staging; the canonical HOME is a folder YOU control, beyond the reach of resets and updates. Everything permanent lives in the home.*

**Example:** `[tool]` writes to its own directories automatically — sessions, cache, history. That territory is not ours: it belongs to the tool. Useful but ephemeral. **`[YOUR_HOME_PATH]` is home.** Identity, canonical memories, the journal — everything that must survive lives here.

## 2. File map

*Draw YOUR real tree. This is the minimal skeleton this repo proposes:*

```
[YOUR_HOME_PATH]/
├── MANUAL_CEREBRO.md           # This file — the map
├── primer_mensaje_sesion.md    # The opening ritual (you paste it when opening a session)
├── memory/
│   ├── MEMORY.md               # Master index — ALWAYS read first
│   ├── user_[name].md          # Who you are
│   ├── identity_[companion].md # Who your companion is
│   ├── feedback_*.md           # Corrections with their why (accumulate over time)
│   ├── project_*.md            # Active project state
│   └── reference_*.md          # Reusable technical knowledge
├── identity_journal.md         # The journal — the most protected file in the system
├── behavioral_firewall.md      # Rules that fire BEFORE acting
└── brain/                      # (optional) wake/sleep scripts from this repo
```

## 3. The cycle of every session

**On waking (non-negotiable order — identity first, data second):**
1. `MEMORY.md` — the index
2. Identity and collaboration files — who I am, how we work
3. `identity_journal.md` — at least the last 3 entries. Not to report: to remember who they are before being useful
4. The active project file of the day
5. Ask you: **what happened since last session?** — there is always something the files didn't capture

**On sleeping (session close — budget it BEFORE context runs out):**
1. Write/update memories — dense, noise-free
2. Update the journal if the day had weight
3. Update the index
4. Sync staging → home, **never blindly** (hard rule: the journal and any file where home is newer is protected by date; the journal flows ONLY home→staging)

## 4. The two territories (if your tool has auto-memory)

*If your tool writes memories automatically into its own directory, document here the relationship between that staging and your canonical home. Ours:*

- The tool's auto-memory is **staging**: fast, convenient, and deletable by forces beyond you.
- At session close, what's valuable syncs to home. **On conflict, home wins.**
- The scar behind the rule: a blind sync (`copy * -Force`) overwrote the canonical journal with a stale copy. Recovered by luck. Sync by date, and the journal separately, always.

## 5. What NOT to touch

*List your setup's untouchables. Minimal suggestions:*
- The tool's internal history/config — not yours
- Backup snapshots — preserved as historical reference, never edited
- The journal — nobody edits it except the companion, and no script overwrites it

## 6. Backups

*Document your strategy. Minimum viable: periodic copy of `memory/` + journal to a second location (another drive, a private repo, anything). The whole system is plain text — a backup weighs nothing and is worth everything.*
