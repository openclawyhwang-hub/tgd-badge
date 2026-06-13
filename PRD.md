# PRD: tgd-badge

## Executive Summary

A CLI tool that generates high-quality SVG badges for tGD ecosystem projects — think shields.io but purpose-built for tGD, with zero external dependencies.

## Problem Statement

tGD projects need consistent, attractive badges for their READMEs, websites, and documentation. Existing solutions like shields.io require network access, have external dependencies, and don't provide tGD-specific badge styles. tgd-badge solves this by generating badges locally as pure SVG.

## Target Audience

- tGD project maintainers who want branded badges
- Developers embedding tGD compatibility/powered-by badges in their docs
- CI/CD pipelines that generate badges dynamically

## Key Features

- Generate SVG badges: `<label>` `<message>` `<color>`
- Three styles: `flat`, `flat-square`, `plastic`
- Named colors: `brightgreen`, `green`, `yellow`, `orange`, `red`, `blue`, `purple`, `grey`
- Custom hex color support: `--color #ff6600`
- Output to file or stdout
- Pipe-friendly (stdout mode for CI/CD)
- Validate badge input (non-empty label/message)
- List available colors with `--list-colors`

## Success Criteria

- [ ] CLI produces valid SVG output
- [ ] SVG renders correctly in browsers and GitHub README
- [ ] All three styles generate distinct, correct SVGs
- [ ] Colors map correctly to hex values
- [ ] `--output` writes to file, stdout when omitted
- [ ] Edge cases handled: empty label/message → error
- [ ] Test suite passes with 100% of planned tests
- [ ] `pip install .` works

## Out of Scope

- Web server / API mode (CLI only)
- Image formats other than SVG (PNG, WebP)
- Shields.io API compatibility
- Animated badges
- Template engine / custom layouts

## Sign-off

- [ ] **PM**: [Pending] — —  
- [ ] **DEV**: [Pending] — —  
- [ ] **QA**: [Pending] — —
