# Contributing

## Branches
- main: production, tagged releases only
- staging: release candidate
- dev: integration of finished work
- feat/<name>: new features and pipeline changes
- data/<name>: dataset updates tracked with DVC
- exp/<member>-<idea>: experiments (may never merge)
- fix/<name>: urgent fixes to production

Nobody pushes directly to dev, staging or main. Use pull requests.

## Commit messages
We use Conventional Commits, for example:
- feat: add scaling step
- data: remove duplicate rows
- exp: try max_depth=8
- chore: add pre-commit hooks

## Merge strategy
PRs into dev are squash-merged.

## DVC rule
Always run dvc push before git push when data or models change.
