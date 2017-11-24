
from gaitanalysis.motek import DFlowData

import os
import pandas
import yaml
import numpy as np
import scipy.stats as stats
import pylab as plt
import math



def load(trial_number,trials_dir):

    if trial_number < 10:
        zeros = '00'
    else:
        zeros = '0'
    trial_str = zeros + str(trial_number)
    trial_dir = 'T' + trial_str
    mocap_file = 'mocap-' + trial_str + '.txt'
    record_file = 'record-' + trial_str + '.txt'
    meta_file = 'meta-' + trial_str + '.yml'

    mocap_file_path = os.path.join(trials_dir, trial_dir, mocap_file)

    record_file_path = os.path.join(trials_dir, trial_dir, record_file)
    meta_file_path = os.path.join(trials_dir, trial_dir, meta_file)


    return mocap_file_path, record_file_path, meta_file_path


def getPDF(item):
    item.sort()
    pdf = stats.norm.pdf(item, np.mean(item), np.std(item))
    return item,pdf




script_path = os.path.realpath(__file__)
src_dir = os.path.dirname(script_path)

root_dir = os.path.realpath(os.path.join(src_dir, '..'))
root_dir = '../perturbed-data-paper/raw-data'
mass = []
height = []
age = []
gender = []
l1 = range(6,36)
l2 = range(40,81)

files =  l1+l2
for index in files:
    dflow_data = DFlowData(*load(index,root_dir))
    if 'subject' in dflow_data.meta.keys():
        if 'mass' in dflow_data.meta['subject'].keys():
            mass.append(dflow_data.meta['subject']['mass'])
            height.append(dflow_data.meta['subject']['height'])
            age.append(dflow_data.meta['subject']['age'])

            gender.append(dflow_data.meta['subject']['gender'])


print np.mean(mass)
print np.mean(height)




plt.figure(1)

x,y = getPDF(mass)
plt.subplot(221)
plt.plot(x, y)
plt.title('Mass Distribution')
plt.xlabel('mass [kg]')
plt.grid(True)

x,y = getPDF(height)
plt.subplot(222)
plt.plot(x, y)
plt.title('Height Distribution')
plt.xlabel('height [m]')
plt.grid(True)

x,y = getPDF(age)
plt.subplot(223)
plt.plot(x, y)
plt.title('Age Distribution')
plt.xlabel('age [yr]')
plt.grid(True)

plt.subplot(224)
objects = ('Male', 'Female')
y_pos = np.arange(len(objects))
gender_count = [gender.count('male'), gender.count('female')]
plt.bar(y_pos, gender_count, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.title('Gender')

plt.show()



