def most_freq(given_list):
    most_repeat=1
    for i in given_list:
        total=given_list.count(i)
        if total>most_repeat:
            most_repeat=total
            most_repeat_number=i
            
    return most_repeat_number
        
