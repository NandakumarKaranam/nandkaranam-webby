def get_length(dna):
    ''' (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    '''
    return len(dna)



def is_longer(dna1, dna2):
    ''' (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    '''
    return get_length(dna1) > get_length(dna2)



def count_nucleotides(dna, nucleotide):
    ''' (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    '''
    count = 0
    for char in dna :
        if char == nucleotide :
            count = count + 1

    return count



def contains_sequence(dna1, dna2):
    ''' (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    
    '''
    if dna1.find(dna2) != -1 :
        return True
    else :
        return False

def is_valid_sequence(dna):
    ''' (str) -> bool

    Return True if and only if DNA sequence dna is a valid sequence having only
    'A' 'T' 'G' 'C'.

    >>> is_valid_sequence('ATGCC')
    True
    >>> is_valid_sequence('atgcc')
    False
    '''

    flag = True
    for char in dna:
        if char != 'A' and char != 'T' and char != 'G' and char != 'C':
            flag = False
            return flag
        else :
            continue

    return flag

def insert_sequence(dna1 , dna2 , index):
    ''' (str, str, int) -> str
    Retutn new DNA sequence with dna2 inserted in dna1 at position index in dna1

    >>>insert_sequence('CCGG', 'AT', 2)
    CCATGG

    '''
    
    return dna1[:index]+dna2+dna1[index:]
  

def get_complement(nucleotide):
    ''' (str) -> str

    Return the complementary nucleotide of nucleotide argument

    >>>get_complement('A')
    T
    >>>get_complement('C')
    G

    '''
    if nucleotide == 'A' :
        return 'T'
    elif nucleotide == 'T' :
        return 'A'
    elif nucleotide == 'G' :
        return 'C'
    else :
        return 'G'

def get_complementary_sequence(dna):
    ''' (str) -> str

    Return the complementary sequence of dna

    >>get_complementary_sequence('ATGG')
    TACC

    '''
    compl = ''
    for char in dna:
        compl = compl+get_complement(char)

    return compl


