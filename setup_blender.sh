#/bin/bash

curl "https://mirror.clarkson.edu/blender/release/Blender2.92/blender-2.92.0-linux64.tar.xz" --output /tmp/blender.tar.xz
tar -xf /tmp/blender.tar.xz -C ./
mv blender-2.92.0-linux64/ blender

