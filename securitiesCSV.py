import pandas as pd
import os

def main():
    df = pd.DataFrame(columns=['Symbol', 'Company'])
    directory = os.getcwd()
    security_directory = directory + '/data/securities'
    for file in os.listdir(security_directory):
        decoded =  os.fsdecode(file)
        current_file = os.path.join(security_directory, decoded)
        print(current_file)
        selected_value = 1
        if 'nasdaqtraded' in decoded:
            selected_value = 2
        with open(current_file, 'r') as f:
            next(f)
            for line in f:
                split = line.split('|')
                df = df.append(
                    {
                        'Symbol': split[-1*selected_value].replace('\n',''),
                        'Company': split[selected_value]
                    }, ignore_index=True
                )    
    df = df.drop_duplicates(keep='first').reset_index(drop=True)
    df.to_csv(security_directory+'.csv', encoding="utf-8", index = False)

if __name__=='__main__':
    main()
