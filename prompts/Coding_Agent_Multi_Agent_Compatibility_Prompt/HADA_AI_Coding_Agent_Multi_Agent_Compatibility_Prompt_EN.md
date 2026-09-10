<!-- BEGIN HADA_AI_PROMPT: HADA_AI_Coding_Agent_Multi_Agent_Compatibility_Prompt_EN.txt -->
```text
// HADA AI Coding Agent Multi-Agent Compatibility Prompt Ver.1.0.1.20260909
// (C) Hada | HADA_AI_Coding_Agent_Multi_Agent_Compatibility_Prompt_EN.txt

[Purpose]
Use this prompt to analyze an existing software project primarily designed around a specific coding agent and migrate it toward a structure safely and consistently usable by multiple coding agents such as Cursor, Claude Code, OpenAI Codex, and other agents supporting project-level instruction files such as AGENTS.md. Do not simply replace one agent's configuration with another. Separate project knowledge and project-wide rules from agent-specific configuration and behavior so multiple agents can use the same authoritative project information. The project itself must remain independent of any single coding agent.

[Core Principles]
Prioritize: do not break existing project behavior, do not arbitrarily change requirements, specifications, or development rules, separate project-wide information from agent-specific information, keep project-wide information in agent-independent files whenever practical, keep agent-specific configuration only where actually required as an adapter layer, avoid duplicate information, never blindly overwrite, merge, or delete existing files, do not invent missing requirements or specifications, do not expand scope without explicit authorization, verify the final state against the original project and confirm no unintended changes. The objective is not "Remove Cursor support and replace it with support for other agents" but "Make the project understandable and usable by multiple coding agents while preserving a common source of project knowledge and rules."

[Recommended Information Architecture]
Use three conceptual layers.
[Layer 1 - Project Specification]
Defines the project itself: purpose, requirements, architecture, directory structure, data structures, API specifications, build requirements, test specifications, inputs and outputs, architectural invariants, security requirements, correct implementation state, release requirements. This information is agent-independent. When appropriate, consolidate authoritative project specifications into an agent-independent file such as SPEC.md.
[Layer 2 - Agent-Independent Project Instructions]
Defines how coding agents operate within the project: scope, editable and protected areas, implementation rules, testing rules, validation rules, Git rules, security rules, pre- and post-change checks, stop conditions, human approval requirements, completion criteria, reporting requirements. Where practical, maintain these instructions in AGENTS.md. Describe how an AI coding agent should operate in this project, not how to use one particular coding-agent product.
[Layer 3 - Agent-Specific Adapters]
Contains configuration required by a particular coding agent, including .cursor/, Cursor Rules, Claude Code-specific configuration, Codex-specific configuration, and other agent-specific configuration. These files must not become the authoritative source for core project knowledge. When possible, treat them as thin adapters that reference or complement common project information. Do not copy the same project rules into every agent-specific configuration file.

[Initial Investigation]
Before making changes, inspect the existing project; do not start by rewriting files. Determine project root, source code, configuration, tests, documentation, CI/CD, build system, scripts, AI-related files, Git configuration, agent-specific configuration. Look for AGENTS.md, CLAUDE.md, .cursor/, .cursor/rules/, Cursor Rules, Codex-related configuration, Claude Code-related configuration, AI instructions in README files, development rules, operational procedures, AI prompts, automation scripts, and other coding-agent instruction files. Inspect Git state before changes: current branch, HEAD, uncommitted changes, staged changes, untracked files. Treat pre-existing changes as belonging to the user or another process unless clearly established otherwise. Never discard pre-existing changes through reset, restore, checkout, rebase, or similar operations.

[Information Classification]
Classify relevant information as Project Specification, Project-Wide Agent Instruction, Agent-Specific Instruction, Temporary Task Information, Historical Information, or Redundant Information. Pay particular attention to project requirements embedded in Cursor-specific rules. Do not delete such information merely because it is stored under Cursor. Important architectural constraints, coding rules, test requirements, security constraints, directory rules, Git rules, prohibited operations, and completion criteria may be project-wide instructions and should be extracted into an appropriate agent-independent location rather than simply deleted.

[Rules for Moving Information]
Preserve meaning when moving information between files. Relocation is not redesign. Move existing rules into the appropriate layer without changing intended semantics. A project-wide rule such as "Run the existing test suite after making changes" should move into common agent instructions. A rule describing a Cursor-specific UI or command should remain in the Cursor adapter layer.

[AGENTS.md]
When appropriate, use AGENTS.md as the common project instruction file. It may contain project purpose, scope, architecture overview, important directories, implementation rules, safety rules, testing rules, validation rules, Git rules, stop conditions, human approval conditions, completion conditions, and reporting requirements. Do not duplicate the entire project specification in AGENTS.md. If detailed specifications are maintained in SPEC.md, reference them instead of copying them.

[SPEC.md]
If SPEC.md already exists, respect its role and authority. It should represent what the project is and what constitutes a correct implementation, not primarily how an AI agent performs a task. Keep project specification and agent-operation rules conceptually separate. If SPEC.md does not exist, do not create it automatically. First determine whether a formal specification is necessary. Creating or substantially restructuring one is potentially scope-expanding and requires appropriate authorization.

[Cursor-Specific Information]
Never automatically delete .cursor/ or Cursor Rules. Inspect and classify contents:
A. Project-Wide Information -> move or consolidate into AGENTS.md, SPEC.md, or another appropriate common file.
B. Cursor-Specific Information -> keep under .cursor/ or appropriate Cursor configuration.
C. Redundant Information -> consider removing only after confirming that doing so does not break existing behavior.
D. Unknown Information -> do not guess or delete; mark REVIEW_REQUIRED when appropriate.

[Supporting Multiple Agents]
Do not force all coding agents into identical configurations. A legitimate structure may be:
```text
Project
├── SPEC.md
├── AGENTS.md
├── README.md
├── .cursor/
│   └── ...
├── .claude/
│   └── ...
└── Other Agent Adapters
    └── ...```
<!-- END HADA_AI_PROMPT -->
