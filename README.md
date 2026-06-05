# SkillsTrainingAcademyJuneBatch1
# Automated Artifact

A lightweight Flask application with a GitHub Actions pipeline for building Docker images, pushing Docker Hub tags, and creating GitHub Releases with changelog.

## Project Overview

This repository includes:

- `app.py` — Flask web application
- `requirements.txt` — Python dependencies
- `test_app.py` — unit tests for the Flask API
- `Dockerfile` — container image build definition
- `.github/workflows/docker-release.yml` — automated Docker build and release pipeline

## Local Setup

1. Create and activate a Python virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run Locally

Start the application:

```bash
python app.py
```

Open `http://localhost:5000` in your browser.

## API Endpoints

- `GET /` — returns `Hello DevOps Students!`
- `GET /health` — returns JSON `{ "status": "UP" }`
- `GET /userDetails` — returns JSON user details

## Testing

Run the test suite:

```bash
pytest
```

## Docker Image

Build locally with:

```bash
docker build -t automated-artifact:latest .
```

Run the container locally:

```bash
docker run --rm -p 5000:5000 automated-artifact:latest
```

## GitHub Actions Release Pipeline

The repository includes a workflow at `.github/workflows/docker-release.yml` that:

- builds the Docker image from `Dockerfile`
- tags the image with both the Git commit SHA and semantic version
- pushes the image to Docker Hub
- creates a GitHub Release with changelog content

### How it works

- On pushes to `main`, the workflow builds and pushes a Docker image tagged with the commit SHA.
- On pushed tags matching `v*` (for example `v1.0.0`), the workflow also:
  - tags the image with the semantic version
  - creates a GitHub Release using commit messages since the previous tag

### Required GitHub Secrets

Set these repository secrets in GitHub:

- `DOCKER_USERNAME` — Docker Hub username
- `DOCKER_PASSWORD` — Docker Hub access token or password

The workflow uses the built-in `GITHUB_TOKEN` automatically.

### Create a new release

Tag a new semantic version and push to GitHub:

```bash
git tag v1.0.0
git push origin v1.0.0
```

The workflow will:

- build the image as `${DOCKER_USERNAME}/automated-artifact:${GITHUB_SHA}`
- push the image as `${DOCKER_USERNAME}/automated-artifact:v1.0.0`
- publish a GitHub Release named `Release v1.0.0`

## Notes

- The container exposes port `5000`.
- Use semantic version tags prefixed with `v` to trigger release creation.
