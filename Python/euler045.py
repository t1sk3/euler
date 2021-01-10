def P(n):
    return (n*(3*n-1))/2
 
def H(n):
    return (n*(2*n-1))
     
def main():
    i = 144; j = 166
    got_it = False
    while not got_it:
        hexz = H(i)
        i += 1
        while 1:
            pen = P(j)
            if pen < hexz:
                j += 1
            elif pen > hexz:
                break
            else:
                print(pen)
                got_it = True
                break

if __name__ == "__main__":
    main()