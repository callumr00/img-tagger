Keyword-tag images with a local LLM (default llava:7b) and use fuzzy match with a search query to find and display image matches.

![example output](img/example.jpg)

### Example Use
Tag all photos in the specified directory.
```
python cli.py -t ~/Desktop/photos/
```
Query images for a keyword and return matches.
```
python cli.py -s mountains 
```

### Note
- Needs an ollama server running to tag images with keywords (but not to search stored keywords). Ensure ollama is installed and run `ollama serve`
- It doesn't work very well, though it used to (2 months ago) work better...

![dog (not a donut, mushroom, pizza, burger, toast, or bread)](img/1.jpg)
Donut,Mushroom,Pizza,Burger,Toast,Bread

![swimmer (not dkny, luxury, designer, or fashion)](img/2.jpg)
dkny,luxury,designer,fashion

![alpaca (not donut, crab cake, or cake))](img/3.jpg)
donut,crab cake,cake

- Perhaps it would work better with a different (larger) model, but I can't run >7B parameter models locally. Otherwise it's a simple change. 
