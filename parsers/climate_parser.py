'''
###############################    Structure of files    #################
*precipitation.txt*

USH00011084 1890 -9999    -9999    -9999    -9999    -9999    -9999    -9999    -9999    -9999    -9999    -9999      170  2 -9999
USH00011084 1891   550  2   561  2   575  2   165  2   275  2   670  2   425  2   172  2   200  2     0  2   930  2   525  2  5048
USH00011084 1892  1245  2   440  2   256  2   160  2   380  2   780  2  1226  2  1355  2   300  2   100  2   165  2 -9999    -9999


*temp_max.txt* & *temp_min.txt*

USH00011084 1889 -9999    -9999    -9999    -9999    -9999    -9999      944E     927E     919E   -9999    -9999      767E   -9999
USH00011084 1890   734E     768E     719E     817E     870E   -9999      940E     932E     890E     810E     738E     651E   -9999
USH00011084 1891   623E     745E   -9999      816E     879E     962E   -9999      932E     897E     796E     691E     634  3 -9999
USH00011084 1892   553  3   706  3   722  3   832  3   851  3   926  3   894  3   946  3   896  3   880  3   729  3   623E     796E
#############################################################################################



###############################    QUICK NOTES    ############################
This is at the beginning of each line: USH00011084
The last 6 characters (011084) correspond to the zip code
#############################################################################################



###############################     GOAL    ###############################
1) Remove first 5 characters of each line -> this will preserve the zip code as column 0
2) Remove special identifiers (a-z occurring after numerical values, integers occurring between columns)
3) Replace -9999 with NANAN
4) Replace all spaces (of variable length) with commas
        EX) input:  4   5 6  9
            output: 4,5,6,9
#############################################################################################
'''

import codecs
import re


'''
climate_dict contains the elements
1) key = type of weather file
2) value[0] = input .txt file
3) value[1] = output .txt file
'''
climate_dict = {'precipitation' : ['precipitation.txt', 'precipitation_parsed.txt'],
           'temp_max' : ['temp_max.txt', 'temp_max_parsed.txt'],
           'temp_min' : ['temp_min.txt', 'temp_min_parsed.txt']}


'''
int_jump() generates a list of integers to be excluded from the output file
We will work with this later on when we write the output file
More information can be found about these special identifier in the documentation
'''
def int_jump():
    output = [22, 23, 24]
    for i in range(1, 13):
        output.append(output[0] + 9 * i)
        output.append(output[0] + 9 * i + 1)
        output.append(output[0] + 9 * i + 2)
    # output represents the positions to exclude
    return output


for climate_file in climate_dict:

    data_in = r"/Users/patrickboland4/p_code/projects/factors_influencing_corn_prices/data/" + climate_dict[climate_file][0]
    data_parsed = r"/Users/patrickboland4/p_code/projects/factors_influencing_corn_prices/data/" + climate_dict[climate_file][1]

    with codecs.open(data_parsed, 'w', encoding = 'utf-8') as out:
        with codecs.open(data_in, encoding = 'utf-8') as f:

            targ_range = list(set(range(5, 130)) - set(int_jump()))
            targ_range.sort()


            for line in f.readlines():

                newline = re.sub('-9999', 'NANAN', line)
                otherline = ''
                for char in targ_range:
                     otherline += (newline[char])
                out_line = re.sub(' +', ',', otherline)
                out.write(out_line)
                out.write('\n')

