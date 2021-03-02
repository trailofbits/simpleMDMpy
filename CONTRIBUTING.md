# Contributing TO macadmins/simpleMDMpy

## Getting in contact

If you're interested in contributing or just have a question,
we'd love to chat.

You can find us in [#simplemdm](https://macadmins.slack.com/archives/C4HJ6U742) in the [MacAdmins Slack](https://www.macadmins.org/).

## Submitting Issues

At this point in time there is no restriction for submitting issue, there is also to established labeling system. Feel free to create issues that seem pertinent to the project. 

## Contribution Process

We have a 3 step process for contributions:

1. An issue is created, and changes are committed via a git branch,
named after a relating issue (Issue-2, for example).
2. Create a GitHub Pull Request for your change, please see [Pull Request Requirements](#pull-request-requirements),
3. Code owners will perform a [Code Review](#code-review-process) on the pull request.

### Pull Request Requirements

We strive to ensure high quality throughout the experience. In order to ensure this, all pull requests must meet these specifications:

1. **Linting:** To ensure high-quality code and protect against future regressions, we require all code to be linted against pylint.

2. **CHANGELOG.md:** We use the CHANGELOG for tracking changes to semver tagged releases of the code, so ensure it matches the changelog syntax. Feel free to reference [Keep a CHANGELOG](https://keepachangelog.com/en/0.3.0/) if you have any questions. 


### CODE REVIEW PROCESS

Code review takes place in GitHub pull requests. Issues will be used for more general discussion around the topic or issue.

Once you open a pull request, cookbook owners will review your code using the built-in code review process in Github PRs. We leverage the CODEOWNERS file to assist with this.

The process at this point is as follows:

1. A cookbook maintainer will review your code and merge it if no changes are
necessary.

2. If a maintainer has feedback or questions on your changes they they will
set `request changes` in the review and provide an explanation.

Please see TESTING.md for system requirements.

### Branches and Commits

You should submit your patch as a git branch named after the Github issue, such as Issue-11. This is called a _topic branch_ and allows users to associate a branch of code with the Issue.

It is a best practice to have your commit message have mimic the CHANGELOG, whenever possible.

This also helps other contributors understand the purpose of changes to the code.

```text
    v1.0.6

    Issue

    - Closes #11

    Changed

    - updated data processor to process the data
```
