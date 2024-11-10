# CHANGELOG


## v0.3.0 (2024-11-10)

### Chores

- Update dependencies to address CVE-2024-47874
  ([`4eac712`](https://github.com/SMK1085/smac-fastapi-auth/commit/4eac7126a56116f641cb9d984f51e2af01d37ca4))

Update the dependencies to address the starlette DoS vulnerability.

### Features

- Clarify minor release reasons
  ([`0f97fee`](https://github.com/SMK1085/smac-fastapi-auth/commit/0f97feed5ebc62a900cf3c30b25c11a4a91effb5))

Clarify minor release reasons and bump the version number on next release.


## v0.2.1 (2024-09-11)

### Bug Fixes

- Bump cryptography to 43.0.1
  ([`d37dbe8`](https://github.com/SMK1085/smac-fastapi-auth/commit/d37dbe80a30c0c0e595f1c08a0c8277d0d8ba856))

fix: bump cryptography to 43.0.1

- Bump cryptography to 43.0.1
  ([`a86ef24`](https://github.com/SMK1085/smac-fastapi-auth/commit/a86ef24c3d97982b7c50714a12b4a5a5f1027c93))

Bump to address security vulnerability in cryptography. Update docs to clarify where the changelog
  is located.

### Chores

- Bump cryptography from 42.0.8 to 43.0.1
  ([`3ee1093`](https://github.com/SMK1085/smac-fastapi-auth/commit/3ee1093d866d499eddf3a3d2a09d746f6afe8c43))

Bumps [cryptography](https://github.com/pyca/cryptography) from 42.0.8 to 43.0.1. -
  [Changelog](https://github.com/pyca/cryptography/blob/main/CHANGELOG.rst) -
  [Commits](https://github.com/pyca/cryptography/compare/42.0.8...43.0.1)

--- updated-dependencies: - dependency-name: cryptography dependency-type: indirect ...

Signed-off-by: dependabot[bot] <support@github.com>

- Bump aiohttp from 3.9.5 to 3.10.2
  ([`a5496fa`](https://github.com/SMK1085/smac-fastapi-auth/commit/a5496fac299c9d9eb095876669558972de3d6992))

Bumps [aiohttp](https://github.com/aio-libs/aiohttp) from 3.9.5 to 3.10.2. - [Release
  notes](https://github.com/aio-libs/aiohttp/releases) -
  [Changelog](https://github.com/aio-libs/aiohttp/blob/master/CHANGES.rst) -
  [Commits](https://github.com/aio-libs/aiohttp/compare/v3.9.5...v3.10.2)

--- updated-dependencies: - dependency-name: aiohttp dependency-type: direct:production ...

Signed-off-by: dependabot[bot] <support@github.com>


## v0.2.0 (2024-07-06)

### Features

- Use v4 for artifact downloads
  ([`e375c66`](https://github.com/SMK1085/smac-fastapi-auth/commit/e375c66fece93a4a8706987f91ec3b2f05ff6231))

Use GH actions v4 for artifact downloads.


## v0.1.0 (2024-07-06)

### Chores

- Do not run release on pull request
  ([`783b1a2`](https://github.com/SMK1085/smac-fastapi-auth/commit/783b1a27a015c035e9571303cfec9df03b46552e))

Remove the pull request trigger from the workflow.

### Features

- Initial release version
  ([`229620f`](https://github.com/SMK1085/smac-fastapi-auth/commit/229620f30c2d37df699b818a8c3d1aff01b0381e))

Configure workflow to release initial version to PyPi.


## v0.0.0 (2024-07-06)

### Chores

- Configure PyPi publishing
  ([`ea13aa4`](https://github.com/SMK1085/smac-fastapi-auth/commit/ea13aa4fa9a8e65c9b54e4f94f11b06065497cbe))

Configure publishing according to the user guide:
  `https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/`

- Customize git committer
  ([`450223f`](https://github.com/SMK1085/smac-fastapi-auth/commit/450223f305ad8007022cdf397f2eeb0d601ae06b))

Customize the git committer config for semantic release.

- Sign commits
  ([`97c65f4`](https://github.com/SMK1085/smac-fastapi-auth/commit/97c65f4fdc537f9dbc9fc404caba99f73d08e214))

Configure semantic release to sign commits.

- Add semantic release workflow
  ([`7d3000c`](https://github.com/SMK1085/smac-fastapi-auth/commit/7d3000cfef87bdb1ba31190995ff43a585e43f02))

Add workflow to perform semantic release.

- Add `python-semantic-release`
  ([`dfeeaa6`](https://github.com/SMK1085/smac-fastapi-auth/commit/dfeeaa634fbd8d900aeeb3c27d587c3932b75af8))

Add `python-semantic-release` as dev dependency.

- Add LICENSE
  ([`bd7cd21`](https://github.com/SMK1085/smac-fastapi-auth/commit/bd7cd21d3e3c2ad28c8d8486080b1fab110c5e95))

Add Apache-2.0 license file and update pyproject.toml.

- Initial commit
  ([`4828f6c`](https://github.com/SMK1085/smac-fastapi-auth/commit/4828f6cfe86455fa36c10e8fc44e2448faa11078))
