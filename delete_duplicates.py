import logging

logging.basicConfig(level=logging.INFO)


def read_file():

    global strs

    return open('animelist.txt', 'r',encoding="iso-8859-1",errors="ignore").read().split("\n")


def main():


    output=open('output.txt', 'w')
    strs=read_file()

    seen_strings=[]
    before_length=len(strs)

    for str in strs:

        str=str.strip()
        getVals = list([val for val in str if val.isalnum() or val==" "])
        result = "".join(getVals).lower()
        
        if(result!="" and result not in seen_strings):
            logging.debug(result)
            seen_strings.append(result)
            output.write(result+"\n")       

    after_length=len(seen_strings)

    

    logging.info(f"\nNumber of words (beginning): {before_length}\nNumber of words (beginning):{after_length}")


if __name__ == "__main__":
    main()