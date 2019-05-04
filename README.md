# phish-setlist-prediction
A project to model the song choice of the band Phish during live shows on tour

### Create Conda environment

To replicate the development environment, run the following command in your terminal:
```bash
conda create --name phish --file requirements.txt
```

### Create Python kernel

Next, we need to add a new iPython kernel to jupyter based off of our conda environment if we want that environment to match our scripts. We can do this as follows:
```bash
conda activate phish
conda install nb_conda --yes
python -m ipykernel install --user --name phish --display-name "phish"
```

### Storing environment variables

We need to store our API/AWS access credentials so they're not publicly accessible, but also in a way that ensures we can access them in our Conda environment. The following steps will set up a process for automatically setting/unsetting environment variables when our environment is activated: 

1. Activate the Conda environment by running `conda activate phish`. 
2. Locate the directory for the conda environment by running `echo $CONDA_PREFIX`.
3. Enter that directory and create these subdirectories and files:
```bash
cd $CONDA_PREFIX
mkdir -p ./etc/conda/activate.d
mkdir -p ./etc/conda/deactivate.d
touch ./etc/conda/activate.d/env_vars.sh
touch ./etc/conda/deactivate.d/env_vars.sh
```
4. Edit `./etc/conda/activate.d/env_vars.sh` as follows:
```bash
#!/bin/sh
export PHISH_API_KEY='your-secret-key'
```
5. Edit `./etc/conda/deactivate.d/env_vars.sh` as follows:
```bash
#!/bin/sh
unset PHISH_API_KEY
```

Now when you run `conda activate phish`, the environment variables you specify in `./etc/conda/activate.d/env_vars.sh` such as `PHISH_API_KEY` are set to the values you wrote into the file. When you run `conda deactivate`, those variables are erased.

For more info, reference the [Conda documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#saving-environment-variables) for saving environment variables. 

