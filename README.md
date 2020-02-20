# AirBnB clone - The console
Repository for the AirBnB clone project! (The Holberton B&amp;B)

![HBnB][]

## Description
### The console

  The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine

- Create your data model
- Manage (create, update, destroy, etc) objects via a console / command interpreter
- Store and persist objects to a file (JSON file)

## Requirements
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- Your code should use the PEP 8 style (version 1.7 or more)
- All your files must be executable
- All your modules should have a documentation
- All your classes should have a documentation
- All your functions (inside and outside a class) should have a documentation

### Files and Directories
- `console.py` file is the entry point of our command interpreter.
- `models` directory will contain all classes used for the entire project.
  - `base_model.py` file is the base class of all our models. It contains common elements:
  - `user.py`
  - `state.py`
  - `city.py`
  - `place.py`
  - `review.py`
  - `amenity.py`
  - `engine` directory contain all storage classes (using the same prototype).
    - `file_storage.py` serializes instances to a JSON file and deserializes JSON file to instances
- `tests` directory will contain all unit tests.
``

## Authors and Contributors
- Juan Marcos Cabezas [@juanmarcoscabezas]
- Jose Luis Saldarriaga [@asoka904]

<!-- links -->
[@juanmarcoscabezas]: https://github.com/juanmarcoscabezas/
[@asoka904]: https://github.com/asoka904/
[HBnB]: https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUZGDONYM4%2F20200220%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20200220T044837Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=bc5561cb44402ddd771921134721135f4c17320418f27a6967f6a854aff19bce
