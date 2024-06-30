# Image Tagger

Keyword-tag images with a local LLM and use fuzzy match with a search query to find and display image matches.

![example output](img/output.jpg)

## Example Use
Tag all photos in the specified directory:
```
python cli.py -t ~/Desktop/photos/
```
Query images for a keyword and return matches:
```
python cli.py -s mountains 
```

## Note
- Needs an ollama server running to tag images with keywords (but not to search stored keywords); ensure ollama is installed and run `ollama serve`.
- Will attempt to install the chosen default LLM llava:7b through ollama if it is not already installed.
- The tagging doesn't work very well (though it used to work better 2 months ago?)
- Perhaps it would work better with a different, particularly larger, model, but I can't run >7B parameter models locally. Otherwise it's a simple change. 

![example images](img/images.jpg)
