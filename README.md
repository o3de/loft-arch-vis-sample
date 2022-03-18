# Loft Scene Sample

## Download and Install

This repository uses Git LFS for storing large binary files.  You will need to create a Github personal access token to authenticate with the LFS service.


### Create a Git Personal Access Token

You will need your personal access token credentials to authenticate when you clone the repository.

[Create a personal access token with the 'repo' scope.](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token)


### (Recommended) Verify you have a credential manager installed to store your credentials 

Recent versions of Git install a credential manager to store your credentials so you don't have to put in the credentials for every request.  
It is highly recommended you check that you have a [credential manager installed and configured](https://github.com/microsoft/Git-Credential-Manager-Core)


### Step 1. Clone the repository 

You can clone the gems to any folder locally, including inside the engine folder. If you clone to a folder inside an existing Git repository (e.g. o3de) you should add the folder to the Git exclude file for the existing repository.

#### Option #1 (Recommended) - cloning into a folder outside the engine repository folder

```shell
# clone into a folder outside your engine repository folder
> git clone https://github.com/aws-lumberyard/loft-arch-vis-sample.git
Cloning into 'o3de-samples-project-gems'...
```

#### Option #2 - cloning into the engine repository folder

```shell
# clone the project into a folder named 'o3de-samples-project-gems' in your existing engine repository folder
> git clone https://github.com/aws-lumberyard/loft-arch-vis-sample.git c:/path/to/o3de/loft-arch-vis-sample
Cloning into 'o3de-samples-project-gems'...

# modify the local engine git exclude file to ignore the project folder
> echo loft-arch-vis-sample > c:/path/to/o3de/.git/info/exclude
```

If you have a Git credential helper configured, you should not be prompted for your credentials anymore.

### Step 2. Register the engine and gems 

```shell
# register the engine (only need to do this once)
> c:/path/to/o3de/scripts/o3de register --this-engine

# register the gems 
> c:/path/to/o3de/scripts/o3de register -g c:/path/to/loft-arch-vis-sample
```

You are now setup to use these gems in your projects.

## License

For terms please see the LICENSE*.TXT file at the root of this distribution.


