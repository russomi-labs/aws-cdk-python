#!/usr/bin/env python3

from aws_cdk import core

from lib.HSCDKstack import HSCDKStack


app = core.App()
HSCDKStack(app, "hscdkstack")

app.synth()
