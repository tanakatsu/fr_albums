#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3
import sys
from .util import get_resized_img_bytes


class Fr():
    def __init__(self, region="us-west-2"):
        self.client = boto3.client('rekognition', region_name=region)

    def detect_faces(self, sourceFile):
        imageSource = open(sourceFile, 'rb')

        response = self.client.detect_faces(
                       Image={'Bytes': imageSource.read()})
        return response


    def compare_faces(self, sourceFile, targetFile, th=80, maxsize=2048):
        imageSource = open(sourceFile,'rb')
        imageSourceBytes = imageSource.read()

        # Rekognition accepts less than 5MB images. So, we'll shrink image size.
        imageTargetBytes = get_resized_img_bytes(targetFile, maxsize)

        response = self.client.compare_faces(SimilarityThreshold=th,
                                      SourceImage={'Bytes': imageSourceBytes},
                                      TargetImage={'Bytes': imageTargetBytes})
        return response

