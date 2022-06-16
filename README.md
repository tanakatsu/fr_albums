## Fr albums

### How to use

Install packages
```
$ pip install -r requirements.txt
```

Activate Amazon rekognition
- Create IAM user and give it `AmazonRekognitionFullAccess` permission
- Get AWS\_SECRET\_ACCESS\_KEY

Set enviroment variables
```
$ export AWS_ACCESS_KEY_ID=xxx
$ export AWS_SECRET_ACCESS_KEY=xxx
```

Prepare contents
```
### Assumed structure ###

# face template files (one face in one picture)
template_dir/
    user1.jpg
    user2.jpg
    user3.jpg
    ...

# face recognition target pictures
target_pictures_dir/
    album1/
        al1_pic1.jpg
        al1_pic2.jpg
        al1_pic3.jpg
        ...
    album2/
        al2_pic1.jpg
        al2_pic2.jpg
        al2_pic3.jpg
        ...
```

All set, Here we go!
```
$ python fr_all_albums.py -o output_dir template_dir target_pictures_dir
```
