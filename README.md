# Docker support
This repo is used for developing base docker images that can be used for further development of code.

We are providing these to promote the development of code/container templates to reduce the cost of adding functionality to the processing pipeline.

## Contributing
We welcome the addition of other base docker images to this repo.
Please be sure to clearly label your folders for the environment you are targetting; starting folder names with 'aws', 'clowder', or 'cyverse' for example.

Folder beinging with 'base' are reserved to those images that are not particular to any single environment.

Be sure to read the [organization documentation](https://github.com/AgPipeline/Organization-info) on how to contribute.

## Documenting
Every folder in this repo must have a README.md clearly explaining the interface for derived images, how to create a derived image, and other information on how to use the images created.
Providing a quick start guide with links to more detailed information a good approach for some situations.
The goal is to provide documentation for users of these base images that makes it easy for them to be used.
