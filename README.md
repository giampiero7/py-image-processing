# Python scripts for simple image transformations
Handy when working with icons, like this one:

![img.png](example-imgs/img.png) (img.png)

## opacity.py
Changes the opacity of the image multiplying the alpha channel of each pixel for the specified value.

Example:

    $ python opacity.py img.png 0.4

![img_opacity_0.4.png](example-imgs/img_opacity_0.4.png) (img_opacity_0.4.png)

## tint.py
Changes the color of the image to the specified RGB value keeping the alpha unchanged.

Example:

    $ python tint.py img_opacity_0.4.png 10 20 200

![img_opacity_0.4_tinted.png](example-imgs/img_opacity_0.4_tinted.png) (img_opacity_0.4_tinted.png)

## negative.py
Transforms the colors of the image to their negative, alpha unchanged.

Example:

    $ python negative.py img_opacity_0.4_tinted.png

![img_opacity_0.4_tinted_negative.png](example-imgs/img_opacity_0.4_tinted_negative.png) (img_opacity_0.4_tinted_negative.png)

## invert.py
Inverts the opacity of an image.

Examples:

    $ python invert.py img_opacity_0.4_tinted.png

![img_opacity_0.4_tinted_inverted.png](example-imgs/img_opacity_0.4_tinted_inverted.png) (img_opacity_0.4_tinted_inverted.png)

    $ python invert.py img.png

![img_inverted.png](example-imgs/img_inverted.png) (img_inverted.png)

## white_to_transparent.py
Converts the white pixels of an image to transparent ones

Example:

![img_white.png](example-imgs/img_white.png) (img_white.png)

    $ python white_to_transparent.py img_white.png

![img_white_transp.png](example-imgs/img_white_transp.png) (img_white_transp.png)

## Tips
You can process more images at the same time

Examples:

Change the opacity of 'img.png' and 'img2.png'

    $ python opacity.py img.png img2.png 0.4

Change the opacity of all the png files in the 'icons' folder

    $ python opacity.py icons/*.png 0.4
