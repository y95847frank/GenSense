# GenSense
[Natural Language Processing Laboratory](http://nlg3.csie.ntu.edu.tw) at National Taiwan University

## Overview

## Requirements
1. Python3
2. Numpy

## Data
1. Word vector file

    A file containing a pre-trained word vector model. In word vector model, each line has a word vector as follows :
        `the -1.0 0.1 0.2`

    p.s. You can download pre-trained word vector in [Word2Vec](https://code.google.com/archive/p/word2vec/) or [GloVe](https://nlp.stanford.edu/projects/glove/).

2. Lexicon file (provided in `thesaurus_ontology/`)

    It's an ontology file that contains words and its' synonyms. Each line represents a word and all it's synonyms. The format is :
        `<wordsense><weight> <neighbor-1><weight> <neighbor-2><weight> ...`

    ps. I used [Thesaurus-API](https://github.com/Manwholikespie/thesaurus-api) to parse the ontology.

3. Word similarity evaluation dataset (provided in `eval_data/`)

## Program Execution

```
$ python all-joint_retrofit.py -i word_vec_file -s synonym_lexicon_file -a antonym_lexicon_file -n num_iter -o out_vec_file
$ python synonym-joint_retrofit.py -i word_vec_file -s synonym_lexicon_file -n num_iter -o out_vec_file
$ python antonym-joint_retrofit.py -i word_vec_file -a antonym_lexicon_file -n num_iter -o out_vec_file

-i : path of word vectors input file
-s : path of synonym ontology file
-a : path of antonym ontology file
-n : number of iterations (default : n=5)
-o : path of output file
```

Example : 
```
python all-joint_retrofit.py -i glove.txt -s lexicon/synonym_ontology.txt -a lexicon/antonym_ontology.txt -n 5 -o out.txt
```

## Evaluation

```
$ python we_sensesim.py word_vec_file
```
This program will show the cosine similarity score of the word vector on each dataset.
In `eval_data/` directory, there are MEN, MTurk, RW, WS353 datasets. You can add more evaluation dataset to test your word vector on your own.


## Reference
- Pennington, J. et al. 2014. Glove: Global vectors for word representation.
- Jauhar, S.K. et al. 2015. Ontologically grounded multi-sense representation learning for semantic vector space models.
- M. Faruqui, J. Dodge, S.K. Jauhar, C. Dyer, E. Hovy and N.A. Smith et al. 2015. Retrofitting word vectors to semantic lexicons.

## License

## Contact
Feel free to [contact me](mailto:b03902052@ntu.edu.tw) if there's any problems.

