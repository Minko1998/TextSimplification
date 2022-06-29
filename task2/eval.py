import sys
import json
from write_to_csv import csv_writer
# string to string we can run BLEU, or SARI (with source)
#from evaluate import load   
run_number = 10
random_pos_algo = 'Algorithm'

qrel_path = 'simpletext_task2_decorated_run.json'
run_path = f'runs/UAms_TASK2_AutomaticRun{random_pos_algo}{run_number}.json'
#source_path = sys.argv[3]


qrel_json = json.load(open(qrel_path))
run_json = json.load(open(run_path))
#source_json = json.load(open(source_path), encoding='utf-8')

# (1) Use lists, and per concept: "metabolic stress" is one term.

print('Qrels (terms):', len(qrel_json))
print('Run (terms):', len(run_json))

qrel, run = {}, {}

# Create dictionary with ID and list of terms.
#print(qrel['G01.2_1448624402_1']) 
#['biases', 'decision-making']
def json2dict(js, sent_key):
    d = {}
    for el in js:
        id_, snt = el['snt_id'], el[sent_key]
        if id_ in d:
            d[id_].append(snt)
        else:
            d.setdefault(id_, []).append(snt)
    return d

qrel, run = json2dict(qrel_json, 'term'), json2dict(run_json, 'term')
#qrel, run, source = json2dict(qrel_json, 'simplified_snt'), json2dict(run_json, 'simplified_snt'), json2dict(source_json, 'source_snt')

print('Qrels (sentences):', len(qrel))
print('Run (sentences):', len(run))

# This will fail if qrel key not in run...
eval_tuples = [(run[k], qrel[k]) for k in qrel]
#print(eval_tuples)

print('Evaluate on (sentences):', len(eval_tuples))

print('EVAL ON LIST OF CONCEPTS IN QRELS')

total_precision = 0
total_recall = 0
total_fmeasure = 0
for e in eval_tuples:
    cnt = 0
    for i in e[0]:
        if i in e[1]:  # Element of the qrels list (no sub part match).
            cnt += 1
    pre = cnt/len(e[0])
    rec = cnt/len(e[1])
    total_precision += pre
    total_recall += rec
    if (pre+rec>0):
        total_fmeasure += 2*pre*rec/(pre+rec)

total_precision /= len(eval_tuples)
total_recall /= len(eval_tuples)
total_fmeasure /= len(eval_tuples)

results = [random_pos_algo, run_number ,round(total_precision, 5),  round(total_recall, 5), round(total_fmeasure, 5), round(2*total_precision*total_recall/(total_precision + total_recall), 5)]

csv_writer('answers_unbroken_strings', results)

print('Precision', round(total_precision, 5))
print('Recall   ', round(total_recall, 5))
print('F1       ', round(total_fmeasure, 5))
print('Macro F1 ', round(2*total_precision*total_recall/(total_precision + total_recall), 5))


# (2) Use strings, and whitespace separation: "metabolic stress" is two terms.

print('EVAL ON STRING OF TERMS IN QRELS')

# Simply turn the list of terms into a space separated string...
def list2string(l):
    return ' '.join(l).lower() 

eval_tuples2 = [(list2string(run[k]), list2string(qrel[k])) for k in qrel]

#print(eval_tuples2)

total_precision = 0
total_recall = 0
total_fmeasure = 0
for e in eval_tuples2:
    cnt = 0
    for i in e[0].split():
        if i in e[1]:   #String i somewhere in qrel string (substring match).
            cnt += 1
    pre = cnt/len(e[0].split())
    rec = cnt/len(e[1].split())
    total_precision += pre
    total_recall += rec
    if (pre+rec>0):
        total_fmeasure += 2*pre*rec/(pre+rec)

total_precision /= len(eval_tuples2)
total_recall /= len(eval_tuples2)
total_fmeasure /= len(eval_tuples2)

results = [random_pos_algo, run_number ,round(total_precision, 5),  round(total_recall, 5), round(total_fmeasure, 5), round(2*total_precision*total_recall/(total_precision + total_recall), 5)]

csv_writer('answers_broken_strings', results)


print('Precision', round(total_precision, 5))
print('Recall   ', round(total_recall, 5))
print('F1       ', round(total_fmeasure, 5))
print('Macro F1 ', round(2*total_precision*total_recall/(total_precision + total_recall), 5))
