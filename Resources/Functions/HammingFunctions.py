def get_Hamming_Distance(answer, sequence, metric):
    cont=0
    for i in range(len(answer)):
        if(sequence.is_satisfied()==True):
            return metric
        if(cont>metric+1):
            sequence.change_satisfied(True)
            return metric
        if answer[i]!=sequence.get_char(i):
            cont=cont+1
    return cont

def min_Hamming_Distance(sequence,threshold):
    value=int(float(threshold)*float((sequence[0].get_len()-1)))
    return value