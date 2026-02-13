# LLM skills

List of skills/agents/rules I use with Claude Code.

Most of the skills are copy-pasted from other great repos. Some of them are changed or created via Claude itself.

## Prerequisites

### Terminal

- [kitty](https://sw.kovidgoyal.net/kitty/). I use [this configs](./kitty.conf).
- Or [ghostty](https://ghostty.org/)

For kitty I recommend:
- [fzf](https://github.com/junegunn/fzf) - fuzzy search
- [bat](https://github.com/sharkdp/bat) - cat with syntax highlighting

### CLI tools

Add instructions ([rules/CLI.md](./rules/CLI.md)) to use these tools:

- [jq](https://jqlang.org/) - command-line JSON processor
- [ripgrep](https://github.com/BurntSushi/ripgrep) - recursively searches directories for a regex pattern while respecting your gitignore
- [fd](https://github.com/sharkdp/fd) - a simple, fast and user-friendly alternative to 'find'
- [ast-grep](https://github.com/ast-grep/ast-grep) - is an abstract syntax tree based tool to search code by pattern code
- [shellcheck](https://github.com/koalaman/shellcheck) - ShellCheck, a static analysis tool for shell scripts
- [shfmt](https://github.com/mvdan/sh) - A shell parser, formatter, and interpreter with bash support
- [wt](https://github.com/max-sixty/worktrunk) - a CLI for git worktree management, designed for running AI agents in parallel
- [tmux](https://github.com/tmux/tmux) - terminal multiplexer: it enables a number of terminals to be created, accessed, and controlled from a single screen
- [agent-browser](https://github.com/vercel-labs/agent-browser) - Browser automation CLI for AI agents

```shell
brew install jq ripgrep fd ast-grep shellcheck shfmt worktrunk tmux

brew install agent-browser
agent-browser install  # Download Chromium
```

#### agent browser

Read full documentation [here](https://agent-browser.dev/cdp-mode). It uses Playwright.

```shell
agent-browser open <url>        # Navigate
agent-browser snapshot -i       # Get element refs (@e1, @e2)
agent-browser click @e1         # Click element
agent-browser fill @e2 "text"   # Fill input
agent-browser screenshot        # Capture screenshot
```

Install skills for claude:

```
/plugin marketplace add vercel-labs/agent-browser
/plugin install agent-browser@agent-browser
```

## References

- https://github.com/obra/superpowers
- https://github.com/trailofbits/claude-code-config/tree/main
- https://github.com/SuperClaude-Org/SuperClaude_Framework/tree/master
