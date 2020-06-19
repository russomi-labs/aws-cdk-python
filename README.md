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

## Quick Start

See [Your first AWS CDK app](https://docs.aws.amazon.com/cdk/latest/guide/hello_world.html) for a complete walkthrough.

1. Create the app
1. Add an Amazon S3 Bucket
1. Synthesize an AWS CloudFormation template
1. Deploying the stack
1. Modifying the app
1. Destroying the app's resources

### Create the app

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

### Add an Amazon S3 bucket

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

* `scope` : Tells the bucket that the stack is its parent: it is defined within the scope of the stack. You can define constructs inside of constructs, creating a hierarchy (tree).

* `Id` : The logical ID of the Bucket within your AWS CDK app. This (plus a hash based on the bucket's location within the stack) uniquely identifies the bucket across deployments so the AWS CDK can update it if you change how it's defined in your app. Buckets can also have a name, which is separate from this ID (it's the bucketName property).

* `props` : A bundle of values that define properties of the bucket. Here we've defined only one property: versioned, which enables versioning for the files in the bucket.
    - In `Python` , props are represented as keyword arguments.
    - In `TypeScript` and `JavaScript` , props is a single argument and you pass in an object containing the desired properties.

All constructs take these same three arguments.  And as you might expect, you can subclass any construct to extend it to suit your needs, or just to change its defaults.

> Tip: If all a construct's props are optional, you can omit the third parameter entirely.

### Synthesize an AWS CloudFormation template

``` bash
cdk synth
```

If your app contained more than one stack, you'd need to specify which stack(s) to synthesize. But since it only contains one, the Toolkit knows you must mean that one.

> Tip: If you received an error like `--app` is required..., it's probably because you are running the command from a subdirectory. Navigate to the main app directory and try again.

The cdk synth command executes your app, which causes the resources defined in it to be translated to an AWS CloudFormation template. The output of cdk synth is a YAML-format AWS CloudFormation template, which looks something like this. Even if you aren't very familiar with AWS CloudFormation, you should be able to find the definition for an AWS:: S3:: Bucket.

``` yaml
Resources:
  MyFirstBucketB8884501:
    Type: AWS::S3::Bucket
    Properties:
      VersioningConfiguration:
        Status: Enabled
    UpdateReplacePolicy: Retain
    DeletionPolicy: Retain
    Metadata:
      aws:cdk:path: HelloCdkStack/MyFirstBucket/Resource
  CDKMetadata:
    Type: AWS::CDK::Metadata
    Properties:
      Modules: aws-cdk=1.XX.X,@aws-cdk/aws-events=1.XX.X,@aws-cdk/aws-iam=1.XX.X,@aws-cdk/aws-kms=1.XX.X,@aws-cdk/aws-s3=1.XX.X,@aws-cdk/cdk-assets-schema=1.XX.X,@aws-cdk/cloud-assembly-schema=1.XX.X,@aws-cdk/core=1.XX.X,@aws-cdk/cx-api=1.XX.X,@aws-cdk/region-info=1.XX.X,jsii-runtime=node.js/vXX.XX.X
```

The output of `cdk synth` is a perfectly valid AWS CloudFormation template. You could take it and deploy it using the AWS CloudFormation console. But the AWS CDK Toolkit also has that feature built-in.

### Deploying the stack

To deploy the stack using AWS CloudFormation, issue:

``` bash
cdk deploy
```

As with cdk synth, you don't need to specify the name of the stack since there's only one in the app.

`cdk deploy` displays progress information as your stack is deployed. When it's done, the command prompt reappears. You can go to the AWS CloudFormation console and see that it now lists HelloStack. You'll also find MyFirstBucket in the Amazon S3 console.

### Modifying the app

### Destroying the app's resources

## Next steps

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## References

* [Your first AWS CDK app](https://docs.aws.amazon.com/cdk/latest/guide/hello_world.html)
* [AWS CDK User Guide](https://docs.aws.amazon.com/CDK/latest/userguide)
* [github.com/aws/aws-cdk](https://github.com/aws/aws-cdk)
* [cdk](https://aws.amazon.com/cdk/)

## License

[MIT](https://choosealicense.com/licenses/mit/)
 
