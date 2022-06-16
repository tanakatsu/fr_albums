#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3
import sys

class Fr():
    def __init__(self, region="us-west-2"):
        self.client = boto3.client('rekognition', region_name=region)

    def detect_facs(self, sourceFile):
        imageSource = open(sourceFile, 'rb')

        response = self.client.detect_faces(
                       Image={'Bytes': imageSource.read()})
        return response


    def compare_faces(self, sourceFile, targetFile, th=80):
        imageSource = open(sourceFile,'rb')
        imageTarget = open(targetFile,'rb')

        response = self.client.compare_faces(SimilarityThreshold=th,
                                      SourceImage={'Bytes': imageSource.read()},
                                      TargetImage={'Bytes': imageTarget.read()})
        return response

