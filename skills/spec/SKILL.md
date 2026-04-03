---
name: spec
description: "Interactive requirements discovery through Socratic dialogue and systematic exploration"
disable-model-invocation: true
---

# /brainstorm - Interactive Requirements Discovery

## Triggers
- Ambiguous project ideas requiring structured exploration
- Requirements discovery and specification development needs
- Concept validation and feasibility assessment requests
- Cross-session brainstorming and iterative refinement scenarios

## Behavioral Flow
1. **Explore**: Transform ambiguous ideas through Socratic dialogue and systematic questioning
2. **Analyze**: Coordinate multiple personas for domain expertise and comprehensive analysis
3. **Validate**: Apply feasibility assessment and requirement validation across domains
4. **Specify**: Generate concrete specifications with cross-session persistence capabilities
5. **Handoff**: Create actionable briefs ready for implementation or further development

Key behaviors:
- Multi-persona orchestration across architecture, analysis, frontend, backend, security domains
- Systematic execution with progressive dialogue enhancement and parallel exploration
- Cross-session persistence with comprehensive requirements discovery documentation

## Tool Coordination
- **Read/Write/Edit**: Requirements documentation and specification generation
- **WebSearch**: Market research, competitive analysis, and technology validation
- **sequentialthinking**: Structured reasoning for complex requirements analysis
- **AskUserQuestion**: Clarify specification via interactive dialog

## Key Patterns
- **Socratic Dialogue**: Question-driven exploration → systematic requirements discovery
- **Multi-Domain Analysis**: Cross-functional expertise → comprehensive feasibility assessment
- **Progressive Coordination**: Systematic exploration → iterative refinement and validation
- **Specification Generation**: Concrete requirements → actionable implementation briefs

## Boundaries

**Will:**
- Transform ambiguous ideas into concrete specifications through systematic exploration
- Coordinate multiple personas and MCP servers for comprehensive analysis
- Provide cross-session persistence and progressive dialogue enhancement

**Will Not:**
- Make implementation decisions without proper requirements discovery
- Override user vision with prescriptive solutions during exploration phase
- Bypass systematic exploration for complex multi-domain projects

## CRITICAL BOUNDARIES

**STOP AFTER REQUIREMENTS DISCOVERY**

This command produces a REQUIREMENTS SPECIFICATION ONLY.

**Explicitly Will NOT**:
- Create architecture diagrams or system designs
- Generate implementation code
- Make architectural decisions
- Design database schemas or API contracts
- Create technical specifications beyond requirements

**Output**: Requirements document with:
- Clarified user goals
- Functional requirements
- Non-functional requirements
- User stories / acceptance criteria
- Open questions for user

## Spec format

File name: `{YYY}-{feature_slug}.md`.

```markdown
# Specification: [Feature Name]

**Epic:** XXX — Epic name
**User Story:** YYY — User story description
**Related specs:** [name](file.md) (if any)

---

## 1. User Goal

One paragraph: who is the user, what they want to do, why they need it.

Example:
> A patient wants to quickly capture their thoughts in a diary so they can
> discuss them with their doctor at the next appointment. The entry should
> save automatically, without extra steps.

---

## 2. Context

_(Optional)_ Background, dependencies, relation to other features.

---

## 3. User Scenarios

Every scenario listed here MUST be implemented. If a scenario can be deferred,
move it to "Out of Scope" with a TG reference to a separate story.

### Scenario 1 — [Name]

[Description: what the user does and why]

**How to test independently**: [How to verify this scenario in isolation]

**Acceptance criteria**:

1. **Given**: [initial state].
   **When**: [user action].
   **Then**: [expected result].

2. **Given**: [another initial state].
   **When**: [action].
   **Then**: [result].

### Scenario 2 — [Name]

...

---

## 4. Functional Requirements

Everything listed here MUST be implemented. No priority column — if it's here,
it's required. Defer anything non-essential to "Out of Scope".

| #      | Requirement                         |
|--------|-------------------------------------|
| REQ-01 | [What the system must do]           |
| REQ-02 | [Another requirement]               |
| REQ-03 | [Yet another requirement]           |

---

## 5. Non-functional Requirements

_(Optional)_

| #      | Requirement                                       | Category       |
|--------|---------------------------------------------------|----------------|
| NFR-01 | [Response time, size limits, etc.]                | Performance    |
| NFR-02 | [Security requirement]                            | Security       |

---

## 6. Success Criteria

_(Optional)_

| #     | Criterion                                | How to measure           |
|-------|------------------------------------------|--------------------------|
| SC-01 | [Metric showing feature success]         | [Measurement method]     |

---

## 7. Data Model

_(Optional — only if the feature introduces new entities)_

Key entities and their fields. No storage details.

**Entity: [Name]**

| Field        | Type     | Constraints              | Description                 |
|--------------|----------|--------------------------|-----------------------------|
| id           | UUID     | PK                       | Unique identifier           |
| [field]      | [type]   | [constraints]            | [description]               |

**Typical constraints to consider for each field:**
- **Required / Optional** — can the field be null or omitted?
- **Uniqueness** — must the value be unique across the entity?
- **Length / Size limits** — min/max length for strings, max size for files or collections
- **Value range** — min/max for numbers, dates; allowed values for enums
- **Format / Pattern** — email, URL, phone, date format, regex pattern
- **Default value** — what value is used if not provided?
- **Referential integrity** — FK to another entity
- **Immutability** — can the field be updated after creation?

---

## 8. Screens

_(Optional — only if there is UI)_

### Screen: [Name]

**Purpose**: [What the user sees and does on this screen]

**Elements**:
- [Element 1] — [behavior]
- [Element 2] — [behavior]

**States**:
- Loading: [what the user sees]
- Empty state: [what the user sees]
- Error: [what the user sees]

**Navigation**: Where user comes from -> Where user goes next

---

## 9. API Endpoints

_(Optional — only if there is server interaction)_

Contract only: method, path, request/response bodies, error codes.

### [Action]

```
[METHOD] /api/v1/[resource]
```

**Request**:
```json
{
  "field": "value"
}
```

**Response 200**:
```json
{
  "id": "uuid",
  "field": "value"
}
```

**Errors**:

| Code | Situation                 | Response body                            |
|------|---------------------------|------------------------------------------|
| 400  | [Description]             | `{"error": "bad_request", "message": "..."}` |
| 404  | [Description]             | `{"error": "not_found", "message": "..."}`   |
| 409  | [Conflict description]    | `{"error": "conflict", "message": "...", "current": {...}}` |

---

## 10. Edge Cases

_(Optional — if behavior at boundaries is non-obvious)_

- [Case 1] — [expected behavior]
- [Case 2] — [expected behavior]
- [Offline scenario] — [expected behavior]

---

## 11. Out of Scope

What is NOT included in this specification and why:

- [Feature X] — separate story ZZZ
- [Feature Y] — deferred until [reason/phase]
```

## Checklist Before Completion

- [ ] User goal is clear without additional context
- [ ] Every scenario has acceptance criteria in Given/When/Then
- [ ] All functional requirements are mandatory (no priorities — defer the rest to Out of Scope)
- [ ] Scope boundary is explicit (what is NOT included and why)
- [ ] API describes contract, not implementation
- [ ] No implementation details (architecture, DB schemas, code)

Next Step: After specification completes, use /architect for architecture or /planner for implementation planning
