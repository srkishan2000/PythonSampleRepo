def sphere_volume(radius):
    '''
    Calculation of a Sphere Volume using its radius
    '''
    
    # Volume of sphere formulae is : 4/3 * pi * radius cube
    pi = 22/7
    volume = (4/3)*(pi)*(radius ** 3)
    print(volume)
    
sphere_volume(5)
sphere_volume(7)
sphere_volume(2)
