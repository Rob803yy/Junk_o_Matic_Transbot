# Contributing Guidelines

Thank you for considering contributing to this project. This document
outlines the preferred workflow for making changes.

## Commit Style
- Write short, present-tense commit messages (e.g. "Add feature" instead of
  "Added feature").
- Provide a brief summary in the first line (50 characters or less) and add
  further details in the following lines if necessary.
- Group related changes into a single commit.

## Pull Request Flow
1. Fork the repository and create a feature branch.
2. Make your changes and ensure the project still builds or functions.
3. Run any available tests if present.
4. Open a pull request against the `main` branch with a clear description of
   your changes.
5. One of the code owners will review your PR. Please be responsive to review
   feedback.

## Large Files
If you need to add large binary assets, please use
[Git LFS](https://git-lfs.github.com/) to store them. This keeps the repository
size manageable.

## Project Board
The [project board](docs/project_board.md) lists open issues and labels such as
`phase1`, `phase2`, `doc`, `infra`, and `good-first-issue`. Check the board to
claim tasks or see what's planned for upcoming milestones.

