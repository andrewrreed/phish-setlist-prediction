# phish-setlist-prediction
A project to model the song choice of the band Phish during live shows on tour

### Create Conda Environment

To replicate the development environment, run the following command in your terminal:
```bash
conda create --name phish --file requirements.txt
```

### Create Python Kernel

Next, we need to add a new iPython kernel to jupyter based off of our conda environment if we want that environment to match our scripts. We can do this as follows:
```bash
source activate phish
conda install nb_conda --yes
python -m ipykernel install --user --name phish --display-name "phish"
