S-Box Analyser
=============
*S-Box Analyser*
is a toolkit to analyse and study the properties of **any** given substitution box.

Consider **Data Encryption Standard**. DES had been secure for over 20 years until Matsui developed a [technique](https://www.wikiwand.com/en/Linear_cryptanalysis) to break the cipher. The S-boxes of DES, however, haven't been released officially yet. Hence, a tool is needed to sudy and analyse substitution boxes. 

Using the look-up table of an S-Box, S-Box Analyser gets the following properties for every ***out***-bit boolean function:

- Alegbraic Normal Form
- Truth Table
- Sequence
- Walsh Hamadard Coefficients
- Non-linearity
- Degree
- Terms present in the boolean function

#### Table of Contents
  - main.py : Gateway to the toolkit.
  - properties.py : A place where all properties are being calculated. 
  - tables : Where one stores the look-up tables.
  - results: The analysis reports for every substitution box.
  - README.md : File that explains this stuff.
---
#### Setting up the thing
1. Place the S-Box look-up tables in *tables* named as sbox_*[number]*.txt as already done for DES.
2. Run ``` python main.py ```
3. The required results will be stored in *results* as sbox_*[number]*.txt

**Note**: 
1. The files in *tables* might have different structure. Make sure to change line 132 of *properties.py* accordingly.
2. The digits in each term denote the subscript of variable. Presence of '0' denotes 1 in the boolean function. Thus, Y<sub>i</sub> is denoted by i.
3. The txt files already included here are for the DES S-Boxes. Make sure to delete the previous files before analysing new S-Boxes.

#### Using the Code
Using the script is pretty simple. 
User can use *main.py* to operate on the toolkit through shell. Alternatively, one can import the properties module to study specific properties.

```
import properties

with open("sbox_analyser/tables/sbox_1.txt", 'r') as table:
	look_up = table.read()
look_up = look_up.split()

rows = [ look_up[17:33], look_up[34:50], look_up[51:67], look_up[68:84] ] #Should be changed according to format of txt.

fn_map = function_generate(rows)

for i in xrange(OUT):
    print 'X' + str(i) + '\n:'
    print fn_map[i]
```
##### Version: 1.0
Coming up next: 
1. Correlation Immunity Order
2. Resiliency Order
3. Algebraic Immunity Order
4. LSFR Analyser


#### Contribution
Feel free to report errors and submit pull requests. Contributions are welcome.
