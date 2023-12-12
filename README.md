# AirBnB Clone Console Project

## Project Overview

Welcome to our collaborative project where we're building the initial elements of an AirBnB clone. The primary focus right now is on creating a command-line interface (CLI) to manage AirBnB objects, setting the stage for the upcoming phases of our project.

### Meet the Team

- **Team Members:** Annabel Amondi, Fatima Zohra Ezzaidani

### Description

## What We're Building

### Project Concepts

In this journey, we're diving into key concepts like Python packages and the AirBnB clone itself.

### The Story So Far

Our project involves creating a command interpreter to handle AirBnB objects. We're establishing a parent class (BaseModel) to take care of object initialization, serialization, and deserialization. A serialization/deserialization flow is set up, classes for AirBnB objects are crafted, and the first storage engine (File storage) is implemented. Testing is crucial to validate our classes and storage engine.

### Our Command Interpreter

Think of it like the Shell, but tailored for our needs. Our CLI lets us:

- Create new objects (e.g., User, Place)
- Retrieve objects from files or databases
- Perform operations on objects (count, compute stats, etc.)
- Update object attributes
- Destroy objects

## Learning Together

### Learning Objectives

By the end of this project, we're aiming to:

- Create a Python package
- Build a command interpreter using the cmd module
- Implement unit testing in a large project
- Understand how to serialize and deserialize a class
- Write and read from a JSON file
- Manage datetime in Python
- Get comfortable with UUIDs (Universal Unique Identifiers)
- Work with \*args and \*\*kwargs in functions
- Handle named arguments in a function

### What We Need from You

#### Code Requirements

- **Editors:** vi, vim, emacs
- **Compatibility:** Ubuntu 20.04 LTS, Python 3.8.5
- **File Etiquette:** End all files with a new line
- **Shebang Love:** Start every file with `#!/usr/bin/python3`
- **README.md:** Don't forget this at the project's root!
- **Code Style:** Let's follow Pycodestyle (version 2.8.\*)
- **Executable Files:** Make sure all files are executable
- **Document Everything:** All modules, classes, and functions need proper documentation

#### Testing is Caring

- **Editors:** vi, vim, emacs
- **File Etiquette:** End all files with a new line
- **Test Nest:** Keep them cozy inside a 'tests' folder
- **Use Unittest:** The unittest module is your friend
- **Name Convention:** All test files should start with 'test\_'
- **Testing Dance:** Execute tests with `python3 -m unittest discover tests`

### GitHub Playground

- **One Repository:** One project repository per group
- **Risk Alert:** Cloning or forking a project repository with the same name before the second deadline? Risking a 0% score.

## Let's See It in Action

### Interactive Magic

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

### Silent Commands

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

Run all the tests with:

```bash
$ echo "python3 -m unittest discover tests" | bash
```

## Lights, Camera, Action!

## Copyright and Respect

We're all in this to learn and grow. Please create your own solutions and avoid plagiarism. Sharing content from this project is a no-go. Let's make this a positive and collaborative experience!

Happy coding! 🚀
