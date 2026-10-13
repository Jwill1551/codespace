# Codespace

My study notes and small practice projects for the four subjects I'm learning. Larger projects live in their own repos.

## Subjects

| Subject | What's in it |
| --- | --- |
| [Backend Development](Backend_Dev/) | How the web works, APIs, and server-side code |
| [Cloud Computing](Cloud%20Computing/) | Notes on cloud concepts and services |
| [DevOps](DevOps/) | Notes on tooling, automation, and deployment |
| [IT Fundamentals](IT%20Fundamentals/) | Networking, hardware, and operating system basics |

## Layout

Each subject has its own folder. Inside it, notes and code are kept apart:

```
<Subject>/
├── Notes/       # Markdown study notes, one file per module or topic
└── Projects/    # Small scripts and exercises that go with the notes
```

Note files are named by module, e.g. `Module_1-Web-functionality.md`.

## Contents

### Backend Development

- **Notes**
  - [Module 1 - How the Web Actually Works](Backend_Dev/Notes/Module_1-Web-functionality.md): the request lifecycle (DNS, TCP + TLS, HTTP request, server, handler, HTTP response)
- **Projects**
  - [py_request.py](Backend_Dev/Projects/py_request.py): fetches posts from the JSONPlaceholder API with `requests` and prints the first five

### Cloud Computing

_No notes yet._

### DevOps

_No notes yet._

### IT Fundamentals

_No notes yet._

## Running the projects

The Python projects need Python 3 and the `requests` library:

```bash
pip install requests
python Backend_Dev/Projects/py_request.py
```
