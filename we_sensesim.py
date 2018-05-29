import numpy as np
import sys
import utils
import os

from collections import defaultdict
from nltk.corpus import wordnet as wn
from scipy.spatial.distance import cosine
from scipy.spatial.distance import correlation
from numpy.linalg import norm
from scipy.stats import spearmanr, pearsonr
from utils import trim
import pdb

"""
	Sense embedding format: see https://github.com/sjauhar/SenseRetrofit
    Use ',' to seperate Datasets
"""
def run(path, fname):
    '''
    if len(sys.argv) != 3:
        print("Usage: python we_sensesim.py SenseEmbedding Datasets")
        exit(0)
    '''
    #wvs = utils.readWordVecs(os.path.expanduser(full_path))
    wvs = utils.readWordVecs(sys.argv[1])
    print("Finish reading vector!")
    wvssen = {}
    s_list = defaultdict(list)
    for sense in wvs:
        wvssen[sense.split("%")[0]] = ''
        s_list[sense.split("%")[0]].append(sense)
    mean_vector = np.mean(wvs.values(), axis=0)
    
    spear_score_max = []
    spear_score_avg = []
    spear_score_my = []
    f_name = []

    for name in fname:
        full_path = os.path.join(path, name)
        filenames = os.path.expanduser(full_path).split(',')
        pairs, scores = utils.readDataset(filenames[0], no_skip=True)
        #f_name.append(filenames[0])
        #print("Pair number for %s: %d"%(filenames[0], len(pairs)))
        coefs_max = []
        coefs_avg = []
        coefs_my = []
        missing = 0
        for pair in pairs:
            vecs0 = []
            trimed_p0 = trim(pair[0], wvssen)
            if trimed_p0 not in wvssen:
                vecs0.append(mean_vector)
                missing += 1
                #print trimed_p0,
            else:
                for sense in s_list[trimed_p0]:
                    vecs0.append(wvs[sense])
                '''
                for sense in wvs:
                    word = sense.split("%")[0]
                    if trimed_p0 == word:
                        vecs0.append(wvs[sense])
                '''
            vecs1 = []
            trimed_p1 = trim(pair[1],wvssen)
            if trimed_p1 not in wvssen:
                vecs1.append(mean_vector)
                missing += 1
                #print trimed_p1,
            else:
                for sense in s_list[trimed_p1]:
                    vecs1.append(wvs[sense])
                '''
                for sense in wvs:
                    word = sense.split("%")[0]
                    if trimed_p1 == word:
                        vecs1.append(wvs[sense])
                '''
            '''
                max_value and avg_value: see "Multi-Prototype Vector-Space Models of Word Meaning" section 3.2 Measuring Semantic Similarity
                http://www.cs.utexas.edu/~ml/papers/reisinger.naacl-2010.pdf
            ''' 
            max_value = max([1-cosine(a,b) for a in vecs0 for b in vecs1])
            avg_value = np.mean([1-cosine(a,b) for a in vecs0 for b in vecs1])
            dist_list = [np.linalg.norm(a-b) for a in vecs0 for b in vecs1]
            en_list = [1-cosine(a,b) for a in vecs0 for b in vecs1]
            en_value = en_list[dist_list.index(min(dist_list))]

            coefs_max.append(max_value)
            coefs_avg.append(avg_value)
            coefs_my.append(en_value)
            
        spear_max = spearmanr(scores, coefs_max)
        pearson_max = pearsonr(scores, coefs_max)
        spear_avg = spearmanr(scores, coefs_avg)
        pearson_avg = pearsonr(scores, coefs_avg)
        spear_my = spearmanr(scores, coefs_my)
        pearson_my = pearsonr(scores, coefs_my)
        spear_score_max.append(spear_max[0])
        spear_score_avg.append(spear_avg[0])
        spear_score_my.append(spear_my[0])

    #fw = open('result/result_all_g50.csv', 'a')
    #fw.write('type,')
    print 'type     \t',
    for i in range(len(fname)):
        print fname[i].split('.')[0],
        #fw.write(fname[i].split('.')[0]+',')
    
    print '\nspear max\t',
    #fw.write('\nspear max,')
    for i in range(len(fname)):
        print '%.04f,' % (spear_score_max[i]),
        #fw.write('%.03f,'%(spear_score_max[i]))
    
    print '\nspear avg\t',
    #fw.write('\nspear avg,')
    for i in range(len(fname)):
        print '%.04f,' % (spear_score_avg[i]),
        #fw.write('%.03f,'%(spear_score_avg[i]))
    
    print '\nspear my\t',
    #fw.write('\nspear my,')
    for i in range(len(fname)):
        print '%.04f,' % (spear_score_my[i]),
        #fw.write('%.03f,'%(spear_score_my[i]))
    #fw.write('\n')
    
    #print("%s : smax %.03f / pmax %.03f / savg %.03f / pavg %.03f || missing : %d"
    #    % (name, spear_max[0], pearson_max[0], spear_avg[0], pearson_avg[0], missing))

if __name__ == "__main__":
    #run('~/sim_data', ['EN-MEN.txt', 'EN-RW.txt', 'EN-SIM999.txt'])
    run('~/sim_data', ['EN-MEN-n.txt', 'EN-MEN-l.txt', 'EN-TRUK.txt', 'EN-RG-65.txt', 'EN-RW.txt', 'EN-SIM999.txt', 'EN-WS353.txt', 'EN-WS353-s.txt', 'EN-WS353-r.txt'])

