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
source activate phish
conda install nb_conda --yes
python -m ipykernel install --user --name phish --display-name "phish"
```

### Create .env file for API credentials

We'll need to store our API credentials so they're not publicly accessible, but we can both reference them in our code in the same way. To do this, we must create a `.env` file for our project and make sure to add to our `.gitignore`:
```bash
touch .env
```

Now we must save our keys as environment variables by adding the following in the `.env` file: 
```bash
export PHISH_API_KEY="YourSecretKey"
```
and `source` the file so your changes take effect: 
```bash
source .env
```

*Note: At the moment, you'll have to run `source .env` everytime you want to work on this but we should add it to our activate script for the conda env in the future so this is done as we activate the conda environment.*

