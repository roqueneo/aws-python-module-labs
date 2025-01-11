import re

def analize_file():
    with open('resources/preproinsulin-seq.txt', 'r') as preproinsulin_file:
        raw_text = preproinsulin_file.read()
        
    print(f'Raw text: {raw_text}\n')

    cleaned_text = re.sub(r'(?i)ORIGIN', '', raw_text)
    cleaned_text = cleaned_text.replace('//', '')
    
    cleaned_sequence = re.sub(r'[^a-zA-Z]', '', cleaned_text).lower()
    
    seq_length = len(cleaned_sequence)
    print(f'Result: {cleaned_sequence}\nLength: {seq_length}')
    
    if seq_length != 110:
        print('Warning: 110 characters where expected\n')
    else:
        print('Right result!\n')
        
    with open('resources/preproinsulin-seq-clean.txt', 'w') as preproinsulin_seq_clean_file:
        preproinsulin_seq_clean_file.write(cleaned_sequence)
        
    lsinsulin = cleaned_sequence[0:24]
    binsulin = cleaned_sequence[24:54]
    cinsulin = cleaned_sequence[54:89]
    ainsulin = cleaned_sequence[89:110]
    
    with open('resources/lsinsulin-seq-clean.txt', 'w') as lsinsulin_seq_clean_file:
        lsinsulin_seq_clean_file.write(lsinsulin)        
    
    with open('resources/binsulin-seq-clean.txt', 'w') as binsulin_seq_clean_file:
        binsulin_seq_clean_file.write(binsulin)        
        
    with open('resources/cinsulin-seq-clean.txt', 'w') as cinsulin_seq_clean_file:
        cinsulin_seq_clean_file.write(cinsulin)        
        
    with open('resources/ainsulin-seq-clean.txt', 'w') as ainsulin_seq_clean_file:
        ainsulin_seq_clean_file.write(ainsulin)  
        
    print(f"lsinsulin: {len(lsinsulin)}, expected characters 24")
    print(f"binsulin: {len(binsulin)}, expected characters 30")
    print(f"cinsulin: {len(cinsulin)}, expected characters 35")
    print(f"ainsulin: {len(ainsulin)}, expected characters 21")      
    
    print("Process completed!!!")  
        
analize_file()