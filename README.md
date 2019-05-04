# phish-setlist-prediction
A project to model the song choice of the band Phish during live shows on tour

### Create Conda environment

To replicate the development environment, run the following command in your terminal:
```bash
conda create --name phish --file requirements.txt --yes
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
echo "export PHISH_API_KEY="YourSecretKey"" >> .env
```
and `source` the file so your changes take effect:
```bash
source .env
```

*Note: At the moment, you'll have to run `source .env` everytime you want to work on this but we should add it to our activate script for the conda env in the future so this is done as we activate the conda environment.*

### Configuring Boto for AWS management

Boto is the Amazon Web Services (AWS) SDK for Python. It enables Python developers to create, configure, and manage AWS services, such as EC2 and S3. Boto can be configured in multiple ways, but we will be using the environment variable method for credential configuration. 

Boto3 will check these environment variables for credentials:

- `AWS_ACCESS_KEY_ID`: The access key for your AWS account.
- `AWS_SECRET_ACCESS_KEY`: The secret key for your AWS account.
- `AWS_SESSION_TOKEN`: The session key for your AWS account. This is only needed when you are using temporary credentials.

Since we have permanent account credentials, we will only be storing the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`. This follows the same process as above: 
1. Edit `./etc/conda/activate.d/env_vars.sh` as follows:
```bash
export AWS_ACCESS_KEY_ID="your-access-key"
export AWS_SECRET_ACCESS_KEY="your-secret-key"
```
2. Edit `./etc/conda/deactivate.d/env_vars.sh` as follows:
```bash
unset AWS_ACCESS_KEY_ID
unset AWS_SECRET_ACCESS_KEY
```

For other methods of configuration, consult the [Boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html). 

#### Usage

For the majority of the AWS services, Boto offers *two* different ways to access the service APIs:

- *Client*: low-level service access
- *Resource*: higher-level object-oriented service access

We will mainly be using Boto to interface with S3. You can use either of the two ways to interact with S3. 

To connect to the *low-level* client interface, you must use Boto3’s `client()`. You then pass in the name of the service you want to connect to, in this case, S3:
```python 
import boto3
s3_client = boto3.client('s3')
```

To connect to the high-level interface, you’ll follow a similar approach, but use `resource()`:
```python 
import boto3
s3_resource = boto3.resource('s3')
```

*Reference: https://realpython.com/python-boto3-aws-s3/*

*Examples: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-examples.html*
