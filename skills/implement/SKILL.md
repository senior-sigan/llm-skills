---
name: implement
description: "Feature and code implementation"
disable-model-invocation: true
---

# /implement - Feature Implementation

- read specification and architecture plan
- check api schema already written
- run a team of agents to write RED tests: tdd agent, test review agent
- validate tests are aligned with architecture plan and specification
- git commit red tests
- run a team of agents to write GREEN tests following the architecture plan: manager, developers, code reviewer
- validate code with architecturer, it must be aligned with specification and plan
- run tdd agent to achieven 100% coverage
- run all tests
- git commit green test with 100% coverage and zero linter issues
