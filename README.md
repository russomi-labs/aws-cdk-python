![https://cdkworkshop.com/images/cdk-logo.png](https://cdkworkshop.com/images/cdk-logo.png)

# aws-cdk-python

A repo based on the `python` workshop from https://cdkworkshop.com/ 

## Installation

See the [Getting Started](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html) for complete details.

### Install Node.js

Install [Node.js 10.3.0](https://nodejs.org/en/download/) or later.

``` bash
brew install node
npm install -g aws-cdk
cdk --version

brew tap aws/tap
brew install aws-sam-cli
sam --version
brew upgrade aws-sam-cli
```

### AWS Toolkit for Visual Studio

Install the [AWS Toolkit for Visual Studio Code](https://aws.amazon.com/visualstudiocode/) which is an open-source plug-in for Visual Studio Code that makes it easier to create, debug, and deploy applications on AWS. The toolkit provides an integrated experience for developing AWS CDK applications, including the AWS CDK Explorer feature to list your AWS CDK projects and browse the various components of the CDK application.

## Usage

See [Your first AWS CDK app](https://docs.aws.amazon.com/cdk/latest/guide/hello_world.html) for a complete walkthrough.

``` bash

# create a directory for the app
mkdir hello-cdk
cd hello-cdk

# Note: The AWS CDK project template uses the directory name to name things in the generated code.

# cdk init TEMPLATE --language LANGUAGE
cdk init app --language python

# activate the virtualenv
source env/bin/activate

# install the packages from requirements.txt
pip install -r requirements.txt

# list the stacks
cdk ls

# install the aws-s3 module
pip install aws-cdk.aws-s3

```

`hello_cdk_stack.py` 

``` python

from aws_cdk import (
    aws_s3 as s3,
    core
)
bucket = s3.Bucket(self, 
    "MyFirstBucket", 
    versioned=True,)

```

The `Bucket` class is a `Construct` and takes three parameters:

* scope: Tells the bucket that the stack is its parent: it is defined within the scope of the stack. You can define constructs inside of constructs, creating a hierarchy (tree).

* Id: The logical ID of the Bucket within your AWS CDK app. This (plus a hash based on the bucket's location within the stack) uniquely identifies the bucket across deployments so the AWS CDK can update it if you change how it's defined in your app. Buckets can also have a name, which is separate from this ID (it's the bucketName property).

* props: A bundle of values that define properties of the bucket. Here we've defined only one property: versioned, which enables versioning for the files in the bucket.

All constructs take these same three arguments.  And as you might expect, you can subclass any construct to extend it to suit your needs, or just to change its defaults.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## References

* [AWS CDK User Guide](https://docs.aws.amazon.com/CDK/latest/userguide)
* [github.com/aws/aws-cdk](https://github.com/aws/aws-cdk)
* [cdk](https://aws.amazon.com/cdk/)

## License

[MIT](https://choosealicense.com/licenses/mit/)
 