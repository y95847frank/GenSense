# GenSense
[Natural Language Processing Laboratory](http://nlg.csie.ntu.edu.tw) at National Taiwan University

## Overview
With the aid of recently proposed word embedding algorithms, the study of semantic similarity has progressed and advanced rapidly. However, many natural language processing tasks need sense level representation. To address this issue, some researches propose sense embedding learning algorithms. In this paper, we present a generalized model from existing sense retrofitting model. The generalization takes three major components: semantic relations between the senses, the relation strengths and the semantic strengths. In the experiment, we show that the generalized model can outperform previous approaches in three types of experiment: semantic relatedness, contextual word similarity and semantic difference.

## Requirements
1. Python3
2. Numpy

## Data
1. Word vector file

    A file containing a pre-trained word vector model. In word vector model, each line has a word vector as follows :
        `the -1.0 0.1 0.2`

    p.s. You can download pre-trained word vector in [Word2Vec](https://code.google.com/archive/p/word2vec/) or [GloVe](https://nlp.stanford.edu/projects/glove/).

2. Lexicon file (provided in `lexicon/`)

    It's an ontology file that contains senses and its' synonyms/antonyms. Each line represents a sense and all it's synonyms/antonyms. The format is :
        `
        Synonym:
        <word>%<sense>#<weight> <synonym-word1>%<sense>#<weight> <synonym-word2>%<sense>#<weight> ...
        Antonym:
        <word>%<sense>#<weight> <antonym-word1>%<sense>#<weight> <antonym-word2>%<sense>#<weight> ...
        
        <sense>: from 0 to the maximum number of senses of the <word>
        <weight>: 1.0, 0.6 or 0.3.
                1.0 for the nearest synonym/antonym relation (1.0 also for itself)
                0.3 for the farthest synonym/antonym relation
        `

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
$ python we_sensesim.py sense_vec_file
```
This program will show the Spearman correlation coefficient of the AvgSim/MaxSim scores on each dataset.
In `eval_data/` directory, there are MEN, MTurk, RW, WS353 datasets. You can add more evaluation dataset to test your word vector on your own.


## Reference
- Pennington, J. et al. 2014. Glove: Global vectors for word representation.
- Jauhar, S.K. et al. 2015. Ontologically grounded multi-sense representation learning for semantic vector space models.
- M. Faruqui, J. Dodge, S.K. Jauhar, C. Dyer, E. Hovy and N.A. Smith et al. 2015. Retrofitting word vectors to semantic lexicons.

## How to cite this resource
Please cite the following paper when referring to GenSense in academic publications and papers.

Yang-Yin Lee, Ting-Yu Yen, Hen-Hsen Huang, Yow-Ting Shiue, and Hsin-Hsi Chen. 2018. GenSense: A Generalized Sense Retrofitting Model. In Proceedings of the 27th International Conference on Computational Linguistics (COLING 2018), August 20-26, 2018, Santa Fe, New Mexico, USA.

## Contact
Feel free to [contact me](mailto:tyyen@nlg.csie.ntu.edu.tw) if there's any problems.

