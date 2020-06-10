def display(count,inp):
    ret=''
    if '1' in inp:
        if count==1:
            ret += "# "
        elif count==2:
            ret += "# "
        elif count==3:
            ret += "# "
        elif count==4:
            ret += "# "
        elif count==5:
            ret += "# "
    if '2' in inp:
        if count==1:
            ret += "### "
        elif count==2:
            ret += "  # "
        elif count==3:
            ret += "### "
        elif count==4:
            ret += "#   "
        elif count==5:
            ret += "### "
    if '3' in inp:
        if count==1:
            ret += "### "
        elif count==2:
            ret += "  # "
        elif count==3:
            ret += "### "
        elif count==4:
            ret += "  # "
        elif count==5:
            ret += "### "
    if '4' in inp:
        if count==1:
            ret += "# # "
        elif count==2:
            ret += "# # "
        elif count==3:
            ret += "### "
        elif count==4:
            ret += "  # "
        elif count==5:
            ret += "  # "
    if '5' in inp:
        if count==1:
            ret += "### "
        elif count==2:
            ret += "#   "
        elif count==3:
            ret += "### "
        elif count==4:
            ret += "  # "
        elif count==5:
            ret += "### "
    if '6' in inp:
        if count==1:
            ret += "### "
        elif count==2:
            ret += "#   "
        elif count==3:
            ret += "### "
        elif count==4:
            ret += "# # "
        elif count==5:
            ret += "### "
    if '7' in inp:
        if count==1:
            ret += "### "
        elif count==2:
            ret += "  # "
        elif count==3:
            ret += "  # "
        elif count==4:
            ret += "  # "
        elif count==5:
            ret += "  # "
    if '8' in inp:
        if count==1:
            ret += "### "
        elif count==2:
            ret += "# # "
        elif count==3:
            ret += "### "
        elif count==4:
            ret += "# # "
        elif count==5:
            ret += "### "
    if '9' in inp:
        if count==1:
            ret += "### "
        elif count==2:
            ret += "# # "
        elif count==3:
            ret += "### "
        elif count==4:
            ret += "  # "
        elif count==5:
            ret += "###"
    if '0' in inp:
        if count==1:
            ret += "### "
        elif count==2:
            ret += "# # "
        elif count==3:
            ret += "# # "
        elif count==4:
            ret += "# # "
        elif count==5:
            ret += "### "
#    print(ret)
    return ret

def mannageip(inp):
    for count in range(1,6):
        fin=''
        conn=''
        for let in inp:
            conn=display(count,let)
            fin+=conn
        print(fin)

inp=input("Enter a series of Number: ")
mannageip(inp)
