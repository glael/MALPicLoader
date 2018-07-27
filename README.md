# MALPicLoader
Gets url for anime or manga picture and formats it like this: 

```css
#more34611{background-image: url(https://myanimelist.cdn-dena.com/images/anime/12/83498.jpg);}
```

Because of removal of api, every page has to be loaded. (this is slow, but it's the only way (probably*))

To use: change userName and listType variables, run using python3
(you will probably have to install beautifulsoup4 (using pip)





* The mobile list displays pictures, so if I could figure out how to fetch that with python, this process would be a lot faster. (AKA I'm too lazy to figure out how to do user agents)
