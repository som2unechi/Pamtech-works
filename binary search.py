def binary_search(sequence, item):
    begin_index=0
    end_index=len(sequence)-1

    while begin_index<=end_index:
        mindpoint=begin_index + (end_index-begin_index)//2
        mindpoint_value=sequence[mindpoint]
        if mindpoint_value==item:
            return mindpoint+1
        elif item<mindpoint_value:
            end_index=mindpoint-1

        else:
            begin_index = mindpoint+1

    return None
sequence_a= range(1,1100)
item=int(input('your input here'))
print(len(sequence_a))
print(binary_search(sequence_a,item))
print(int(len(sequence_a)/2))
