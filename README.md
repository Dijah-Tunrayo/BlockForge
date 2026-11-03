# BlockForge

A coding environment where program elements (functions, classes, loops,
conditionals) are colour-coded blocks, backed by an AI-assisted syntax
fixer that detects the language, locates errors and suggests validated
fixes with cited community sources. Blocks are reassembled into ordinary
source code, so the output works with normal compilers and editors.

**Status:** early development (Week 1 of a 12-week plan)

## First milestone
A command-line tool that takes a file, detects its language, locates a
syntax error and prints one suggested fix, starting with Python.

## Planned components
- Language detection (own classifier)
- Error localization (Tree-sitter)
- Rule-based and model-based fixes, with a validator
- Cited suggestions from Stack Exchange and official docs
- Block editor (VS Code extension prototype)

## Licensing and attribution
Code is licensed under Apache-2.0 (see `LICENSE`). Datasets, pretrained
models and community content (for example, Stack Overflow, which is
CC BY-SA) keep their own licenses, listed in `data/README.md` as they
are added.

BlockForge
Copyright 2026 Khadijah Mahrouf Yusif

This product includes software developed by Khadijah Mahrouf Yusif
