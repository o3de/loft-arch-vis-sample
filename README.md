<u>Supported o3de versions</u> : **23.10**

# Loft ArchVis

![gameplay](doc/gameplay.gif?raw=true)

Loft Architectural Visualization is a set of multiple indoor scene. This project can be used to test direct and indirect lighting setup.

## Prerequisites

You need to build or [install O3DE engine](https://o3de.org/download/).

You need to [install git with lfs support](https://git-scm.com/downloads), and [setup a token on your github account](https://www.docs.o3de.org/docs/welcome-guide/setup/setup-from-github/#configure-credentials-for-git-lfs). Needed as the repository uses Git LFS, the "Download ZIP" button will not download assets.

## How to run

1. Clone the github repository (`git clone https://github.com/o3de/loft-arch-vis-sample.git`). When prompted to authenticate, use your github username and the token as password.
2. Launch O3DE. It will open the Project manager. Click on the **New Project** button then **Open Existing Project** option.
3. Navigate to your repository. Open the **Project** folder. The project should now be registered.

![project](doc/cover.png?raw=true)

4. Click on the **Build Project** button, located on the **O3DE Loft Sample** image.
5. Once the project has been built successfully, use the **Open Editor** button.
6. The asset pre-processor will run for a bit. Once it is over you will be welcomed with the **Open a Level** window, simply pick the first one.

## Project Highlights

- **Benchmarking**, this scene was made to test rendering performances of O3DE.
- **Realistic environment**, the scene uses many assets all in realistic style.

### Screenshots

![screenshot](doc/screenshot-1.png?raw=true)

![screenshot](doc/screenshot-2.png?raw=true)

![screenshot](doc/screenshot-3.png?raw=true)

## License

For terms please see the LICENSE*.TXT files within this distribution.
