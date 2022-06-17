#!/bin/bash

if [ $# != 2 ]; then
  echo "Usage: crop_all_faces.sh input_dir output_dir"
  exit 1
fi

input_dir=$1
output_dir=$2

files=(`ls -1 ${input_dir}/*.jpg`)
for file_name in "${files[@]}"; do
    echo [${file_name}]
    python crop_face.py $file_name $output_dir
done
