![https://cdkworkshop.com/images/cdk-logo.png](https://cdkworkshop.com/images/cdk-logo.png)

# aws-cdk-python

A repo based on the `python` workshop from https://cdkworkshop.com/ 

## Background

The AWS Cloud Development Kit (AWS CDK) lets you define your cloud infrastructure as code in one of five supported programming languages. It is intended for moderately to highly experienced AWS users.

Developers can use one of the supported programming languages to define reusable cloud components known as Constructs. You compose these together into Stacks and Apps.

![https://docs.aws.amazon.com/cdk/latest/guide/images/AppStacks.png](https://docs.aws.amazon.com/cdk/latest/guide/images/AppStacks.png)

## Key Concepts

The AWS CDK is designed around a handful of important concepts. We will introduce a few of these here briefly. Follow the links to learn more, or see the Concepts topics in this guide's Table of Contents.

An AWS CDK app is an application written in TypeScript, JavaScript, Python, Java, or C# that uses the AWS CDK to define AWS infrastructure. 

* `App` - An app defines one or more `stacks` 
    - `Stacks` (equivalent to AWS CloudFormation stacks) contain `constructs` 
        * `Construct` - defines one or more concrete `AWS resources` 
            * `AWS Resource` - concrete resource defined in `construct` 

The AWS CDK includes a library of AWS constructs called the AWS Construct Library. 

Each AWS service has at least one corresponding module in the library containing the constructs that represent that service's resources.

Constructs come in three fundamental flavors:

* **AWS CloudFormation-only or L1 (short for "level 1").** These constructs correspond directly to resource types defined by AWS CloudFormation. In fact, these constructs are automatically generated from the AWS CloudFormation specification, so when a new AWS service is launched, the AWS CDK supports it as soon as AWS CloudFormation does.

    AWS CloudFormation resources always have names that begin with `Cfn` . For example, in the Amazon S3 module, `CfnBucket` is the L1 module for an Amazon S3 bucket.

* **Curated or L2.** These constructs are carefully developed by the AWS CDK team to address specific use cases and simplify infrastructure development. For the most part, they encapsulate L1 modules, providing sensible defaults and best-practice security policies. For example, in the Amazon S3 module, `Bucket` is the L2 module for an Amazon S3 bucket.

    L2 modules may also define supporting resources needed by the primary resource. Some services have more than one L2 module in the Construct Library for organizational purposes.

* **Patterns or L3.** Patterns declare multiple resources to create entire AWS architectures for particular use cases. All the plumbing is already hooked up, and configuration is boiled down to a few important parameters. In the AWS Construct Library, patterns are in separate modules from L1 and L2 constructs.

The AWS CDK's core module (usually imported into code as core or cdk) contains constructs used by the AWS CDK itself as well as base classes for constructs, apps, resources, and other AWS CDK objects.

## Installation

See the [Getting Started](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html) for complete details.

### Install Node.js and the `aws-cdk` 

Install [Node.js 10.3.0](https://nodejs.org/en/download/) or later.

``` bash

# Install node
brew install node

# Install the aws-cdk globally using the node package manager (npm)
npm install -g aws-cdk

# Validate the version of the cdk installed
cdk --version

```

### Install the AWS Toolkit for Visual Studio

Install the [AWS Toolkit for Visual Studio Code](https://aws.amazon.com/visualstudiocode/) which is an open-source plug-in for Visual Studio Code that makes it easier to create, debug, and deploy applications on AWS. The toolkit provides an integrated experience for developing AWS CDK applications, including the AWS CDK Explorer feature to list your AWS CDK projects and browse the various components of the CDK application.

### Install the SAM CLI

Install the [SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) to use with the AWS CDK to test Lambda functions locally.  

``` bash
# tap the aws/tap so we can install it
brew tap aws/tap

# Install the aws-sam-cli
brew install aws-sam-cli

# Validate the version
sam --version

# Upgrade the aws-sam-cli
brew upgrade aws-sam-cli
```

See [AWS CDK tools > SAM CLI](https://docs.aws.amazon.com/cdk/latest/guide/tools.html#sam) for more information.

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

# To manually create a virtualenv on MacOS and Linux:
python -m venv .env

# activate the virtualenv
source env/bin/activate

# install the packages from requirements.txt
pip install -r requirements.txt

# list the stacks
cdk ls

# create the cloudformation
cdk synth

# install the aws-s3 module
pip install aws-cdk.aws-s3

```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt` 
command.

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

# Synthesize CloudFormation stacks
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

    TODO

### Destroying the app's resources

    TODO

## Next steps

    TODO

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
 
