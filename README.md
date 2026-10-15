# Task Manager API

## Project Overview

The Task Manager API is a simple web application developed using Python and FastAPI. It allows users to create tasks, retrieve existing tasks, and check the completion status of a specific task.

The purpose of this project is to demonstrate version control and continuous integration (CI) practices using Git and GitHub Actions. The repository uses feature branches, pull requests, automated testing, and branch protection rules to ensure that changes are validated and reviewed before being merged into the main branch.

## Technologies Used

- **Python 3.12:** Programming language used to develop the application.
- **FastAPI:** Framework used to create the REST API.
- **Pydantic:** Validates incoming task data.
- **Pytest:** Runs automated tests.
- **HTTPX2:** Installed dependency used in the project's testing environment.
- **Git and GitHub:** Manage version control and collaboration.
- **GitHub Actions:** Automates build validation and testing.
- **Uvicorn:** Runs the FastAPI application locally.

## Installation and Setup

1. Clone the repository:

   `git clone https://github.com/criscastillo-art/task-manager-ci.git`

2. Navigate to the project directory:

   `cd task-manager-ci`

3. Install the required dependencies:

   `python3 -m pip install -r requirements.txt`

4. Start the application:

   `python3 -m uvicorn app:app --reload`

5. Open the interactive API documentation:

   `http://127.0.0.1:8000/docs`

## API Endpoints

The application provides the following endpoints:

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Returns a welcome message. |
| GET | `/tasks` | Retrieves all existing tasks. |
| POST | `/tasks` | Creates a new task. |
| GET | `/tasks/{task_id}/status` | Retrieves the completion status of a task. |

When a requested task does not exist, the task-status endpoint returns an HTTP 404 error.

Tasks are stored in memory and will reset when the application restarts.

## Continuous Integration Pipeline

The repository uses GitHub Actions to automate code validation and testing.

The CI pipeline is configured in `.github/workflows/ci.yml` and runs automatically when:

- Code is pushed to the `main` branch.
- A pull request is opened or updated against the `main` branch.

The pipeline performs the following operations:

1. Checks out the repository using `actions/checkout`.
2. Sets up Python 3.12 using `actions/setup-python`.
3. Installs dependencies from `requirements.txt`.
4. Validates Python compilation using `python -m compileall -q app.py`.
5. Executes automated tests using `python -m pytest -v`.

A successful workflow confirms that the application passes compilation validation and its automated tests.

## Branching Strategy

The project uses a feature-branch workflow to organize development and protect the main branch.

- **`main`:** Contains the stable version of the application.
- **`feature/*`:** Used to develop new features independently before merging into `main`.

Developers create feature branches from `main`, make changes, and open pull requests when their work is ready for review.

For example, the `feature/check-task-status` branch was created to implement the task-status endpoint and its associated tests.

## Commit and Pull Request Standards

The repository uses descriptive commit messages to explain code changes.

Commit messages follow a conventional format, such as:

`feat: add task status endpoint and tests`

The `feat:` prefix identifies changes that introduce new functionality.

Pull requests are required before changes can be merged into the `main` branch. Each pull request should include:

- A clear title describing the changes.
- A description of the functionality added or modified.
- Relevant test information.
- A completed pull request checklist.

The repository includes a pull request template in `.github/pull_request_template.md` to maintain consistent documentation.

## Code Review and Branch Protection

Branch protection rules are configured for the `main` branch to enforce the project's review process.

Before merging a pull request:

1. At least one approving review is required.
2. The GitHub Actions `build-and-test` status check must pass.
3. The changes must satisfy the repository's merge requirements.

These rules help prevent unreviewed or failing code from being merged into the main branch.

## Running Tests Locally

Developers can run the automated tests before committing changes using:

`python3 -m pytest -v`

The tests verify:

- The home endpoint returns the expected welcome message.
- The task-status endpoint retrieves the completion status of an existing task.
- The task-status endpoint returns a 404 error when a task does not exist.

## References

Axolo. (n.d.). *A list of pull request templates* [GitHub repository]. GitHub. https://github.com/axolo-co/pull_request_template

The pull request template used in this project was adapted from Example 1 in Axolo's collection of GitHub pull request templates.