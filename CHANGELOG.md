# CHANGELOG

## v0.2.1 (2024-09-11)

### Chore

* chore(deps): bump cryptography from 42.0.8 to 43.0.1

Bumps [cryptography](https://github.com/pyca/cryptography) from 42.0.8 to 43.0.1.
- [Changelog](https://github.com/pyca/cryptography/blob/main/CHANGELOG.rst)
- [Commits](https://github.com/pyca/cryptography/compare/42.0.8...43.0.1)

---
updated-dependencies:
- dependency-name: cryptography
  dependency-type: indirect
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`3ee1093`](https://github.com/SMK1085/smac-fastapi-auth/commit/3ee1093d866d499eddf3a3d2a09d746f6afe8c43))

* chore(deps): bump aiohttp from 3.9.5 to 3.10.2

Bumps [aiohttp](https://github.com/aio-libs/aiohttp) from 3.9.5 to 3.10.2.
- [Release notes](https://github.com/aio-libs/aiohttp/releases)
- [Changelog](https://github.com/aio-libs/aiohttp/blob/master/CHANGES.rst)
- [Commits](https://github.com/aio-libs/aiohttp/compare/v3.9.5...v3.10.2)

---
updated-dependencies:
- dependency-name: aiohttp
  dependency-type: direct:production
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`a5496fa`](https://github.com/SMK1085/smac-fastapi-auth/commit/a5496fac299c9d9eb095876669558972de3d6992))

### Fix

* fix: bump cryptography to 43.0.1

fix: bump cryptography to 43.0.1 ([`d37dbe8`](https://github.com/SMK1085/smac-fastapi-auth/commit/d37dbe80a30c0c0e595f1c08a0c8277d0d8ba856))

* fix: bump cryptography to 43.0.1

Bump to address security vulnerability in cryptography.
Update docs to clarify where the changelog is located. ([`a86ef24`](https://github.com/SMK1085/smac-fastapi-auth/commit/a86ef24c3d97982b7c50714a12b4a5a5f1027c93))

### Unknown

* Merge pull request #10 from SMK1085/develop

fix: bump cryptography from 42.0.8 to 43.0.1 ([`bd039ee`](https://github.com/SMK1085/smac-fastapi-auth/commit/bd039eee2af51fc16aa4b7aca1370ad927df9f2e))

* Merge pull request #9 from SMK1085/dependabot/pip/cryptography-43.0.1

chore(deps): bump cryptography from 42.0.8 to 43.0.1 ([`00f1205`](https://github.com/SMK1085/smac-fastapi-auth/commit/00f12055014a3077292608163f59219420cfebc9))

* Merge pull request #8 from SMK1085/main

Merge main back to develop ([`d9057e5`](https://github.com/SMK1085/smac-fastapi-auth/commit/d9057e55c7da9745d17cd180654029d07868b21a))

* Merge pull request #7 from SMK1085/dependabot/pip/aiohttp-3.10.2

chore(deps): bump aiohttp from 3.9.5 to 3.10.2 ([`edcd97d`](https://github.com/SMK1085/smac-fastapi-auth/commit/edcd97dd5f1cf16686094e98fe79b1ea25ccdb6c))

* Merge pull request #6 from SMK1085/main

merge main back to develop ([`5002670`](https://github.com/SMK1085/smac-fastapi-auth/commit/5002670e36bf7af24a7dde6f0ac946f9c90d115f))

## v0.2.0 (2024-07-06)

### Feature

* feat: use v4 for artifact downloads

Use GH actions v4 for artifact downloads. ([`e375c66`](https://github.com/SMK1085/smac-fastapi-auth/commit/e375c66fece93a4a8706987f91ec3b2f05ff6231))

### Unknown

* Merge pull request #5 from SMK1085/develop

feat: use v4 for artifact downloads ([`0dbbc1b`](https://github.com/SMK1085/smac-fastapi-auth/commit/0dbbc1b0a4954d8f01b37064f73377576756422c))

## v0.1.0 (2024-07-06)

### Chore

* chore: do not run release on pull request

Remove the pull request trigger from the workflow. ([`783b1a2`](https://github.com/SMK1085/smac-fastapi-auth/commit/783b1a27a015c035e9571303cfec9df03b46552e))

### Feature

* feat: initial release version

Configure workflow to release initial version to PyPi. ([`229620f`](https://github.com/SMK1085/smac-fastapi-auth/commit/229620f30c2d37df699b818a8c3d1aff01b0381e))

### Unknown

* Merge pull request #4 from SMK1085/develop

feat: initial release version ([`d8a646e`](https://github.com/SMK1085/smac-fastapi-auth/commit/d8a646e9ef4ae91ac51e117b8d0fa12265d22274))

## v0.0.0 (2024-07-06)

### Chore

* chore: configure PyPi publishing

Configure publishing according to the user guide: `https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/` ([`ea13aa4`](https://github.com/SMK1085/smac-fastapi-auth/commit/ea13aa4fa9a8e65c9b54e4f94f11b06065497cbe))

* chore: customize git committer

Customize the git committer config for semantic release. ([`450223f`](https://github.com/SMK1085/smac-fastapi-auth/commit/450223f305ad8007022cdf397f2eeb0d601ae06b))

* chore: sign commits

Configure semantic release to sign commits. ([`97c65f4`](https://github.com/SMK1085/smac-fastapi-auth/commit/97c65f4fdc537f9dbc9fc404caba99f73d08e214))

* chore: add semantic release workflow

Add workflow to perform semantic release. ([`7d3000c`](https://github.com/SMK1085/smac-fastapi-auth/commit/7d3000cfef87bdb1ba31190995ff43a585e43f02))

* chore: add `python-semantic-release`

Add `python-semantic-release` as dev dependency. ([`dfeeaa6`](https://github.com/SMK1085/smac-fastapi-auth/commit/dfeeaa634fbd8d900aeeb3c27d587c3932b75af8))

* chore: add LICENSE

Add Apache-2.0 license file and update pyproject.toml. ([`bd7cd21`](https://github.com/SMK1085/smac-fastapi-auth/commit/bd7cd21d3e3c2ad28c8d8486080b1fab110c5e95))

* chore: initial commit ([`4828f6c`](https://github.com/SMK1085/smac-fastapi-auth/commit/4828f6cfe86455fa36c10e8fc44e2448faa11078))

### Unknown

* Merge pull request #3 from SMK1085/develop

chore: sign commits ([`32345c3`](https://github.com/SMK1085/smac-fastapi-auth/commit/32345c3b4439fe27d23a826d4a28536a90226862))

* Merge pull request #1 from SMK1085/develop

release: initial release ([`16994f1`](https://github.com/SMK1085/smac-fastapi-auth/commit/16994f122ebaf80b8adea4a54b46bc39082b1b55))
