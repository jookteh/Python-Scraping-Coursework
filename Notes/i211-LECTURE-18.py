import urllib.request
import re


for digit_1 in range(0,9):
    for digit_2 in range(0,9):
        for digit_3 in range(0,9):
            for digit_4 in range(0,9):

                url= "http://cgi.soic.indiana.edu/~ebigalee/secret_vault.cgi?"
                url += "groupname=Group+20&num1="+str(digit_1)+"&num2="+str(digit_2)+"&num3="+str(digit_3)+"&num4="+str(digit_4)


                web_page = urllib.request.urlopen(url)
                lines = web_page.read()

                if str(lines).find("Wrong") == 139:
                    # DO nothing
                    print("Wrong: "+str(digit_1)+","+str(digit_2)+","+str(digit_3)+","+str(digit_4))
                else:
                    print("Sucsess Combo: "+str(digit_1)+","+str(digit_2)+","+str(digit_3)+","+str(digit_4))
                    break




                web_page.close()






