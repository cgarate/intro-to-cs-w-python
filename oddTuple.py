def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    # Your Code Here
    tupResult = ()
    for i in range(len(aTup)):
      if i % 2 == 0:
        tupResult = tupResult + (aTup[i],)

    return tupResult

print(oddTuples((1,"carlos",2,3,4,"Javier")))
