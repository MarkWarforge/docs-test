# Git Flow and Branching Strategy

Our source control workflow is designed to maintain a stable, releasable `production` branch while collaborating on features.

## Branch Naming & Types

All branches and PR titles should follow the `type/branch-name` format. The branch name should align with the PR title format (e.g., `feature/short-description`). 

Supported types:

- **feature**: New features or mechanics (e.g., `feature/player-movement`).

- **fix**: Bug fixes (e.g., `fix/inventory-crash`).

- **hotfix**: Urgent production bug fixes directly branch off the release/main branch.

- **release**: Release preparation branches (e.g., `release/v1.2.0`).

- **content**: New Unity assets, prefabs, levels, or data that don't involve code changes.

- **art**: Art asset integration (models, textures, animations).

- **chore**: Maintenance tasks, dependency updates, or documentation (e.g., `chore/update-readme`).

- **enhance**: Improvements to existing features that are not necessarily brand new features or bug fixes.


## Pull Requests

- Keep PRs scoped and reviewable.

- PR Titles **must** follow the `type/branch-name` convention. This is enforced by our review tools and CI.

- All code changes require at least one approval before merging.

- **Draft PRs**: Use draft PRs for early feedback (CodeRabbit auto-review ignores drafts).


## Merging
- Squash and merge is preferred for small features to keep the commit history clean.

- Ensure the build is green before merging.
