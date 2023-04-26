import numpy as np
import csv

def gradeInfo(filename, numExams, hwWeight):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    data = np.array(data)
    data = data[4:-9]
    data[data=='']=0
    data = data[4:-9][:,0:5]

    
    data = data.astype(float)

    
    hw1_avg = np.mean(data[:,1])

    
    hw2_grades = data[:,2]
    sort_indices = np.argsort(hw2_grades)[::-1]
    hw2_sorted = np.vstack((data[sort_indices,0], 
    hw2_grades[sort_indices])).T

    
    hw1_90plus = np.where(data[:,1] >= 90)[0]
    hw3_90plus = np.where(data[:,3] >= 90)[0]
    hw1_hw3_90plus = np.intersect1d(hw1_90plus, hw3_90plus)
    hw1_hw3_90plus_ids = data[hw1_hw3_90plus,0]


    hw1_80below = np.where(data[:,1] <= 80)[0]
    hw2_90plus = np.where(data[:,2] >= 90)[0]
    hw1_80below_hw2_90plus = np.intersect1d(hw1_80below, hw2_90plus)
    num_students = len(hw1_80below_hw2_90plus)

    hw_scores = data[:,1:numExams+1]
    exam_scores = data[:,numExams+1:]
    hw_avg = np.mean(hw_scores, axis=1)
    exam_avg = np.mean(exam_scores, axis=1)
    overall_avg = hw_avg * hwWeight + exam_avg * (1-hwWeight)
    overall_avg = np.around(overall_avg * 100, decimals=1)
    student_ids = data[:,0]
    grades = np.vstack((student_ids, overall_avg)).T

    return (hw1_avg, hw2_sorted, hw1_hw3_90plus_ids, num_students, grades)

hw1_avg, hw2_sorted, hw1_hw3_90plus_ids, num_students, grades = (gradeInfo('./f4.csv', 1, 0.4))
print(hw1_avg, hw2_sorted, hw1_hw3_90plus_ids, num_students, grades)