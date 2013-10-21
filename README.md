stegasaurus
===========

A couple of neat little scripts for hiding text inside PNGs.

How does this work?
===================

Every pixel of an image is made of three bytes: one each for the red, green, and blue levels. That gives you 2^24 possible colours a pixel can be, which is plenty to illustrate anything the human eye can see. In fact, it's more than enough, which is why this works. We can change the lower-order bits of the pixels without their colours being perceptibly changed. That gives us 3 bits per pixel to use for things besides colour information. These programs write use that space to store text.

The cool thing is, since the changes to these lower-order bits aren't detectable by the human eye (or even rendered by most monitors), no one looking at the image can even tell there's a message hidden in it! Neat.
