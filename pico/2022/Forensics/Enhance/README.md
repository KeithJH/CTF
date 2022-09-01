# Enhance!
## Description
- **Tags**:
    - picoCTF 2022
    - Forensics
- **Author**: LT 'Syreal' Jones


Download this image file and find the flag.
* [Download image file](https://artifacts.picoctf.net/c/137/drawing.flag.svg)


## Exploration

The file provided appears to be an SVG file, which is essentially XML.
```
$ file drawing.flag.svg
drawing.flag.svg: SVG Scalable Vector Graphics image
```

SVG files are essentially XML files so we can take a look through the text to see if anything stands out.

```
$ less drawing.flag.svg
```

And it seems like the flag is broken up between different `tspan`s.
```
$ grep tspan drawing.flag.svg
       id="text3723"><tspan
         id="tspan3748">p </tspan><tspan
         id="tspan3754">i </tspan><tspan
         id="tspan3756">c </tspan><tspan
         id="tspan3758">o </tspan><tspan
         id="tspan3760">C </tspan><tspan
         id="tspan3762">T </tspan><tspan
         id="tspan3764">F { R E D A C T E D </tspan><tspan
         id="tspan3752">R E D A C T E D }</tspan></text>
```

And if we want to go a bit overboard we can script extracting the text and removing unnecessary whitespace.
```
$ ./drawing.flag.py
picoCTF{REDACTED}
```