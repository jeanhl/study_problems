def check_seq(biglist, smalllist):
    # checks to see if the elements in small list are in big list
    # elements must be in order
    # big list will always be larger than small list
    len_to_check = len(biglist) - len(smalllist) + 1
    for bi in range(len_to_check):
        for si in range(len(smalllist)):
            print biglist[bi+si], smalllist[si]
            if biglist[bi+si] == smalllist[si]:
                if si == len(smalllist)-1:
                    return True
            else:
                break
    return False        
    
