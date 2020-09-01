# netflix
#Added support for HBO and some Hulu functionality.

This python script skips Netflix episode intros. Every .25 seconds it searches for ![Image of Skip Intro](https://raw.githubusercontent.com/kickinslowly/netflix/master/skip.PNG) on screen, where skip.png is the current design of the skip intro button for netflix. If 'skip.png' is found, move mouse to skip_img and click. Then go back to searching every .25 seconds.

I was getting OSError when I ctrl+alt+tabbed, so the code has a try/except clause for OSError. If OSError, print to console and then go back to searching for skip_img.

Notes* I am still learning python and this was a random idea that came to me while binging Netflix and being lazy. I used the insipiration for a quick learning project implementation. It was supririsngly easy to create. I have read that there are Chrome plugins that can do the same thing, but again, this was a learning project for me and I also think it's fun to use my own code.

Enjoy!

